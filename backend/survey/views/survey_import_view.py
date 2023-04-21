from django.core.mail import send_mail
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.authtoken.admin import User
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response

from surveybuilder.const import questionTypeModel
from surveybuilder.models import Survey, Question, Block, MultiChoice, ButtonQuestion, RandomSections, PostAddonfield, \
    MatrixTable, RankOrder, Sliders, Groups



@swagger_auto_schema(
    request_body=openapi.Schema(
        title="Survey configuration",
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'language': openapi.Schema(type=openapi.TYPE_STRING),
            'blocks': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT)),
            'randomSections': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT))
        }),
    operation_summary='import survey according to survey configuration file', methods=['POST'])
@api_view(["POST"])
def import_survey(request, researcher_id):
    """
    post:
    Import survey according to survey configuration file
     """
    try:
        import_survey_data(request.data, researcher_id)
        return Response({"status": "success"})
    except Exception as e:
        raise NotAcceptable(detail="Survey cannot be imported!")


@api_view(["POST"])
def send_email(request):
    if request.method == 'POST':
        subject = request.data.get('emailSubject')
        to = request.data.get('emailReciever')
        content = request.data.get('emailContent')
        email_list = to.split(",")
        print(email_list)
        try:
            send_mail(subject, content, 'cs63-1@mineserver.top', email_list)
            return Response({'status': "success"})
        except:
            return Response({'status': 'error'})


def import_survey_data(data, researcher_id):
    survey = Survey()
    researcher = User.objects.get(id=researcher_id)
    survey.researcher = researcher
    if 'name' in data:
        survey.name = data['name']
    if 'language' in data:
        survey.language = data['language']
    if 'consentText' in data:
        survey.consentText = data['consentText']
    if 'time_limit_minutes' in data:
        survey.time_limit_minutes = data['time_limit_minutes']
    survey.save()

    if 'blocks' in data:
        for block in data['blocks']:
            b = Block()
            b.survey = survey
            if 'title' in block:
                b.title = block['title']
            if 'description' in block:
                b.description = block['description']
            if 'order' in block:
                b.order = block['order']
            b.save()

            if 'questions' in block:
                for question in block['questions']:
                    q = Question()
                    q.block = b
                    if 'name' in question:
                        q.name = question['name']
                    if 'type' in question:
                        q.type = question['type']
                    if 'description' in question:
                        q.description = question['description']
                    if 'required' in question:
                        q.required = question['required']
                    if 'order' in question:
                        q.order = question['order']
                    if 'image' in question:
                        q.image = question['image']
                    q.save()

                    typedata = question['typedata']
                    datatype = questionTypeModel[q.type]()
                    datatype.question = q
                    if q.type == 'Text entry':
                        if 'query' in typedata:
                            datatype.query = typedata['query']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'validate' in typedata:
                            datatype.validate = typedata['validate']
                        if 'ansType' in typedata:
                            datatype.ansType = typedata['ansType']
                        datatype.save()
                    if q.type == 'Number scale':
                        if 'minTitle' in typedata:
                            datatype.minTitle = typedata['minTitle']
                        if 'middleTitle' in typedata:
                            datatype.middleTitle = typedata['middleTitle']
                        if 'maxTitle' in typedata:
                            datatype.maxTitle = typedata['maxTitle']
                        if 'interval' in typedata:
                            datatype.interval = typedata['interval']
                        if 'numberMax' in typedata:
                            datatype.numberMax = typedata['numberMax']
                        if 'numberMin' in typedata:
                            datatype.numberMin = typedata['numberMin']
                        if 'minTitleOn' in typedata:
                            datatype.minTitleOn = typedata['minTitleOn']
                        if 'midTitleOn' in typedata:
                            datatype.midTitleOn = typedata['midTitleOn']
                        if 'maxTitleOn' in typedata:
                            datatype.maxTitleOn = typedata['maxTitleOn']
                        datatype.save()
                    if q.type == 'Multiple choice':
                        if 'options' in typedata:
                            datatype.options = typedata['options']
                        if 'isDropDown' in typedata:
                            datatype.isDropDown = typedata['isDropDown']
                        if 'isCheckbox' in typedata:
                            datatype.isCheckbox = typedata['isCheckbox']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'multipleAnswers' in typedata:
                            datatype.multipleAnswers = typedata['multipleAnswers']
                        datatype.save()
                        if 'choices' in question:
                            for choice in question['choices']:
                                c = MultiChoice()
                                c.question = datatype
                                if 'order' in choice:
                                    c.order = choice['order']
                                if 'title' in choice:
                                    c.title = choice['title']
                                c.save()
                    if q.type == 'Rank order':
                        if 'options' in typedata:
                            datatype.options = typedata['options']
                        if 'isDropDown' in typedata:
                            datatype.isDropDown = typedata['isDropDown']
                        if 'isCheckbox' in typedata:
                            datatype.isCheckbox = typedata['isCheckbox']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'multipleAnswers' in typedata:
                            datatype.multipleAnswers = typedata['multipleAnswers']
                        datatype.save()
                        if 'choices' in question:
                            for choice in question['choices']:
                                c = RankOrder()
                                c.question = datatype
                                if 'order' in choice:
                                    c.order = choice['order']
                                if 'title' in choice:
                                    c.title = choice['title']
                                c.save()
                    if q.type == 'Matrix table':
                        if 'options' in typedata:
                            datatype.options = typedata['options']
                        if 'isDropDown' in typedata:
                            datatype.isDropDown = typedata['isDropDown']
                        if 'isCheckbox' in typedata:
                            datatype.isCheckbox = typedata['isCheckbox']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'multipleAnswers' in typedata:
                            datatype.multipleAnswers = typedata['multipleAnswers']
                        if 'columnConfig' in typedata:
                            datatype.columnConfig = typedata['columnConfig']
                        if 'tableConfig' in typedata:
                            datatype.tableConfig = typedata['tableConfig']
                        datatype.save()
                        if 'choices' in question:
                            for choice in question['choices']:
                                c = MatrixTable()
                                c.question = datatype
                                if 'order' in choice:
                                    c.order = choice['order']
                                if 'title' in choice:
                                    c.title = choice['title']
                                c.save()
                    if q.type == 'Sliders':
                        if 'options' in typedata:
                            datatype.options = typedata['options']
                        if 'isDropDown' in typedata:
                            datatype.isDropDown = typedata['isDropDown']
                        if 'isCheckbox' in typedata:
                            datatype.isCheckbox = typedata['isCheckbox']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'multipleAnswers' in typedata:
                            datatype.multipleAnswers = typedata['multipleAnswers']
                        if 'columnConfig' in typedata:
                            datatype.columnConfig = typedata['columnConfig']
                        if 'tableConfig' in typedata:
                            datatype.tableConfig = typedata['tableConfig']
                        if 'min' in typedata:
                            datatype.min = typedata['min']
                        if 'max' in typedata:
                            datatype.max = typedata['max']
                        if 'grid' in typedata:
                            datatype.grid = typedata['grid']
                        datatype.save()
                        if 'choices' in question:
                            for choice in question['choices']:
                                c = Sliders()
                                c.question = datatype
                                if 'order' in choice:
                                    c.order = choice['order']
                                if 'title' in choice:
                                    c.title = choice['title']
                                c.save()
                    if q.type == 'Groups':
                        if 'options' in typedata:
                            datatype.options = typedata['options']
                        if 'isDropDown' in typedata:
                            datatype.isDropDown = typedata['isDropDown']
                        if 'isCheckbox' in typedata:
                            datatype.isCheckbox = typedata['isCheckbox']
                        if 'textboxMax' in typedata:
                            datatype.textboxMax = typedata['textboxMax']
                        if 'textboxMin' in typedata:
                            datatype.textboxMin = typedata['textboxMin']
                        if 'multipleAnswers' in typedata:
                            datatype.multipleAnswers = typedata['multipleAnswers']
                        if 'columnConfig' in typedata:
                            datatype.columnConfig = typedata['columnConfig']
                        if 'tableConfig' in typedata:
                            datatype.tableConfig = typedata['tableConfig']
                        datatype.save()
                        if 'choices' in question:
                            for choice in question['choices']:
                                c = Groups()
                                c.question = datatype
                                if 'order' in choice:
                                    c.order = choice['order']
                                if 'title' in choice:
                                    c.title = choice['title']
                                c.save()
                    if q.type == 'Button row':
                        if 'numberButtons' in typedata:
                            datatype.numberButtons = typedata['numberButtons']
                        datatype.save()
                        if 'buttons' in question:
                            for button in question['buttons']:
                                bt = ButtonQuestion()
                                bt.buttonRow = datatype
                                if 'buttonText' in button:
                                    bt.buttonText = button['buttonText']
                                if 'buttonType' in button:
                                    bt.buttonType = button['buttonType']
                                if 'buttonIcon' in button:
                                    bt.buttonIcon = button['buttonIcon']
                                if 'answered' in button:
                                    bt.answered = button['answered']
                                if 'jumpBlockId' in button:
                                    bt.jumpBlockId = button['jumpBlockId']
                                bt.save()
                    if q.type == 'News post':
                        if 'articleURL' in typedata:
                            datatype.articleURL = typedata['articleURL']
                        if 'articleTitle' in typedata:
                            datatype.articleTitle = typedata['articleTitle']
                        if 'articleSource' in typedata:
                            datatype.articleSource = typedata['articleSource']
                        if 'articleImageLink' in typedata:
                            datatype.articleImageLink = typedata['articleImageLink']
                        if 'articleUser' in typedata:
                            datatype.articleUser = typedata['articleUser']
                        if 'articleStyle' in typedata:
                            datatype.articleStyle = typedata['articleStyle']
                        if 'articleSnippet' in typedata:
                            datatype.articleSnippet = typedata['articleSnippet']
                        if 'articleLikes' in typedata:
                            datatype.articleLikes = typedata['articleLikes']
                        if 'articleComments' in typedata:
                            datatype.articleComments = typedata['articleComments']
                        if 'articleShares' in typedata:
                            datatype.articleShares = typedata['articleShares']
                        if 'articleLikesOn' in typedata:
                            datatype.articleLikesOn = typedata['articleLikesOn']
                        if 'articleCommentsOn' in typedata:
                            datatype.articleCommentsOn = typedata['articleCommentsOn']
                        if 'articleSharesOn' in typedata:
                            datatype.articleSharesOn = typedata['articleSharesOn']
                        if 'numberAddon' in typedata:
                            datatype.numberAddon = typedata['numberAddon']
                        datatype.save()
                        if 'addon' in question:
                            for addon in question['addon']:
                                a = PostAddonfield()
                                a.postRow = datatype
                                if 'title' in addon:
                                    a.title = addon['title']
                                if 'icon' in addon:
                                    a.icon = addon['icon']
                                if 'count' in addon:
                                    a.count = addon['count']
                                a.save()

    if 'randomSections' in data:
        for randomSection in data['randomSections']:
            r = RandomSections()
            r.survey = survey
            if 'display' in randomSection:
                r.display = randomSection['display']
            if 'startWith' in randomSection:
                r.startWith = randomSection['startWith']
            if 'endWith' in randomSection:
                r.endWith = randomSection['endWith']
            if 'index' in randomSection:
                r.index = randomSection['index']
            r.save()
