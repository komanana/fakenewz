import json
import csv
import operator

from django.http import JsonResponse, HttpResponse
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from user_agents import parse

from surveybuilder.models import Survey, Question, TextboxQuestionText, Block
from surveybuilder.serializers import QuestionSerializer, SurveySerializer, \
    TextboxQuestionTextSerializer, BlockSerializer
from surveytaker.models import Response, ResponseBlock
from surveytaker.serializers import ResponseSerializer, ResponseBlockSerializer

@swagger_auto_schema(operation_summary='export response CSV file', methods=['GET'])
@api_view(['GET'])
def csv_export(request, survey_id):
    """
    get:
    Export all the responses and metadata of the survey in CSV format
    """
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Survey.DoesNotExist:
        return JsonResponse({'Message': 'The survey can\'t be found.'}, status=status.HTTP_404_NOT_FOUND)
    survey_serialized = SurveySerializer(survey)
    survey_data = survey_serialized.data
    survey_name = survey_data['name']
    responses = Response.objects.filter(survey=survey.id).order_by('id')
    if len(responses) == 0:
        return JsonResponse({'code': 999, 'message': 'No response received yet!'})
    responses_serialized = ResponseSerializer(responses, many=True)
    responses_data = responses_serialized.data
    result=[[survey_data['name']]]
    last_title=[]
    for response in responses_data:
        responses_blocks=ResponseBlock.objects.filter(response_id=response['id']).order_by('id')
        responses_blocks_serialized=ResponseBlockSerializer(responses_blocks,many=True)
        gaze_dict = {}
        click_dict = {}
        for responses_block in responses_blocks_serialized.data:
            block = Block.objects.get(pk=responses_block['block_id'])
            block_serialized=BlockSerializer(block)
            block_serialized_data=block_serialized.data
            block_name=block_serialized_data['title']
            gazeData=responses_block['gazeData']
            if gazeData != '[]':
             gaze_dict[block_name]=gazeData
            clickEvent=responses_block['clickEvent']
            click_dict[block_name]=clickEvent
        answer_json = json.loads(response['answer_json'])
        answer_row = [answer_json['respondent_identifier']]
        titles = ["respondent_identifier"]
        blocks = answer_json['response_blocks']
        for b in blocks:
            responses_questions = b['response_questions']
            for q in responses_questions:
                question_id = q['question_id']
                question = Question.objects.get(pk=question_id)
                question_serialized = QuestionSerializer(question)
                question_data = question_serialized.data
                title = 'q' + str(question_id) + '_' + question_data['name'].replace(' ', '_')
                if question_data['type'] != "Multiple choice" and \
                        question_data['type'] != "News post" \
                        and title not in titles:
                    titles.append(title)
                if question_data['type'] == "Multiple choice":
                    rqa = q['response_question_answer']
                    for i in rqa:
                        if i['title'] == 'Other':
                            answer = i['answerText']
                        elif i['answerText'] == "selected":
                            answer = 1
                        else:
                            answer = 0
                        if title + ':' + i['title'] not in titles:
                            titles.append(title + ':' + i['title'])
                        answer_row.append(answer)
                if question_data['type'] == "Button row":
                    rqa = q['response_question_answer']
                    answer = ''
                    for i in rqa:
                        if i['answerText'] == "selected":
                            answer = answer + i['title'] + ' '
                    answer_row.append(answer[:len(answer) - 1])
                if question_data['type'] == "Text entry":
                    questionText = TextboxQuestionText.objects.get(question=q['question_id'])
                    questionText_serializer = TextboxQuestionTextSerializer(questionText)
                    questionText_data = questionText_serializer.data
                    if questionText_data['ansType'] == 'Text':
                        answer = q['response_question_answer'][0]['answerText']
                    else:
                        answer = q['response_question_answer'][0]['answerDecimal']
                    answer_row.append(answer)
                if question_data['type'] == "Number scale":
                    answer = q['response_question_answer'][0]['answerText']
                    answer_row.append(answer)
                if question_data['type'] == "News post":
                    rqa = q['response_question_answer']
                    for i in rqa:
                        if i['answerText'] is not None:
                            answer = i['answerText']
                        else:
                            answer = ''
                        if title + ':' + i['title'] not in titles:
                            titles.append(title + ':' + i['title'])
                        answer_row.append(answer)
        answer_row.append(response['create_datetime'][0:10] + " " + response['create_datetime'][11:19])
        answer_row.append(response['end_datetime'][0:10] + " " + response['end_datetime'][11:19])
        answer_row.append(response['preview'])
        answer_row.append(response['completion_rate'])
        if response['camera_state']:
          answer_row.append('Valid')
        else:
          answer_row.append('Invalid')
        if 'user_agent' in answer_json:
            user_agent = parse(answer_json['user_agent'])
            answer_row.append(user_agent.device)
            answer_row.append(user_agent.os.family)
            answer_row.append(user_agent.os.version_string)
            answer_row.append(user_agent.browser.family)
            answer_row.append(user_agent.browser.version_string)
        answer_row.append(json.dumps(click_dict))
        if gaze_dict:
           answer_row.append(json.dumps(gaze_dict))
        if not gaze_dict :
           answer_row.append("Not collected")
        if 'user_action' in answer_json:
            if answer_json['user_action'] != '[]':
                answer_row.append(answer_json['user_action'])
        titles.append("create_time")
        titles.append("end_time")
        titles.append("is_preview")
        titles.append("completion_rate")
        titles.append("camera_state")
        titles.append("device")
        titles.append("os")
        titles.append("os_version")
        titles.append("browser")
        titles.append("browser_version")
        titles.append("click_event")
        titles.append("gaze_data")
        titles.append("user_action")
        if not operator.eq(titles,last_title):
         result.append(titles)
         last_title=titles
        result.append(answer_row)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + survey_name + '_export_result.csv'
    writer = csv.writer(response)
    for i in result:
        writer.writerow(i)
    return response
