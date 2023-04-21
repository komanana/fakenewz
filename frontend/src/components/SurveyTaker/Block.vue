<template>
  <div class="block-class">
    <div class="title">
      <h1>{{ blockData.title }}</h1>
    </div>
    <p style="white-space: pre-line" class="block_description">{{ blockData.description }}</p>
    <div class="questionBlock">
      <div v-for="(item,index) in blockData.questionData.questions" :key="blockData.questionData.questions.id" class="question">
        <RankOrder v-if="item.type ==='Rank order'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <MatrixTable v-if="item.type ==='Matrix table'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <Sliders v-if="item.type ==='Sliders'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <Groups v-if="item.type ==='Groups'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <MultipleChoice v-if="item.type ==='Multiple choice'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <TextEntry v-if="item.type ==='Text entry'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <NumberScale v-if="item.type ==='Number scale'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <NewsPost v-if="item.type ==='News post'" :question="item" :index="index" @updateQuestion="updateQuestion" :ref="'block'+blockIndex+'question'+index"/>
        <ButtonRow v-if="item.type ==='Button row'" :question="item" :index="index" @updateQuestion="updateQuestion" @updateJumpBlockId="updateJumpBlockId" :ref="'block'+blockIndex+'question'+index"/>
      </div>
    </div>
  </div>

</template>
<script>
import MultipleChoice from "@/components/SurveyTaker/MultipleChoice";
import TextEntry from "@/components/SurveyTaker/TextEntry";
import NumberScale from "@/components/SurveyTaker/NumberScale";
import ButtonRow from "@/components/SurveyTaker/ButtonRaw";
import NewsPost from "@/components/SurveyTaker/NewsPost";
import RankOrder from "@/components/SurveyTaker/RankOrder";
import MatrixTable from "@/components/SurveyTaker/MatrixTable";
import Sliders from "@/components/SurveyTaker/Sliders";
import Groups from "@/components/SurveyTaker/Groups";

export default {
  name: "Block",
  components: {ButtonRow, NumberScale, TextEntry, MultipleChoice,NewsPost,RankOrder,MatrixTable,Sliders,Groups},
  props: {
    block: Object,
    index: Number,
    currentId: Number,
    uuid: String
  },
  data() {
    return {
      createTime: "",
      endTime: "",
      blockData: {},
      answerData: {
        // "uuid": "",
        "block_id": 0,
        "response_questions": []
      },
      blockIndex: 0,
      jumpBlockId: 0
    };
  },
  methods: {
    updateQuestion(data, index) {
      console.log("updateQuestion ", data)
      this.answerData.response_questions[index] = data;

      for(let i = 0; i < this.answerData.response_questions[index].response_question_answer.length; i++){
        this.answerData.response_questions[index].response_question_answer[i].uuid = this.answerData.uuid + index + i
      }
      this.endTime = new Date()
      console.log(this.endTime)
      if (this.currentId !== this.block.id) {
        this.createTime = null
        this.endTime = null
      }
      this.answerData.createTime = this.createTime;
      this.answerData.endTime = this.endTime;

      this.$emit("updateBlock", this.answerData, this.blockIndex);
    },
    updateJumpBlockId(id){
      this.jumpBlockId = id
      this.$emit("updateJumpBlockId", this.jumpBlockId)
    },
    checkValidity(){
      let validity = true
      for (let i = 0; i < this.blockData.questionData.questions.length; i++) {
        if (!this.$refs['block' + this.blockIndex + 'question' + i][0].checkValidity()) {
          validity = false
        }
      }
      return validity
    }
  },
  watch:{
    currentId:function (currentId){
      if (this.currentId === this.block.id) {
        this.createTime = new Date()
        this.answerData.createTime = this.createTime;
      }
    }
  },
  created() {
    if (this.currentId === this.block.id) {
      this.createTime = new Date()
      this.answerData.createTime = this.createTime;
    }
    this.blockData = this.block;
    this.blockIndex = this.index;
    this.answerData = {
      "uuid": this.uuid + this.index,
      "block_id": this.blockData.id,
      "response_questions": []
    };
  },
  mounted() {
    console.log("CHILD SEND EMIT",this.answerData )
    this.$emit("updateBlock", this.answerData, this.blockIndex);

    const script = document.createElement('script')
    script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit'
    document.body.appendChild(script)
    
    window.googleTranslateElementInit = function () {
      new window.google.translate.TranslateElement({
        pageLanguage: 'auto',
        includedLanguages: 'zh-CN,ja,kn,hi,ur,en',
        layout: window.google.translate.TranslateElement.InlineLayout.HORIZONTAL
      }, 'google_translate_element');
    }

    window.googleTranslateElementInit.apiKey = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDNkS57Mf3MxnIg\nPt0Rgl/6ydyBxqqfFyi5eTTOsT1hYmB6l9gBsA1UHpYGgff7fmWv079OqI1zApBI\nf7pbgwGCIdYdpCei+3qr7/7MFNyXn4DIN6tQXyEAF+3XmcbMdQHlF1Z9f7aEamTV\noox91MOyGb/1c+IdGAh5Bt8Pl1HfdJGcxeuvwK3xssOviUd51Q7EkBAxsScNrEUL\nXKA9RsVUc0r07SFyPEjhF39+/sQd/F4xprL6PXIahYTpouSQeGbxjLHXtOajvFnK\nhJS7eOGdZIhXK20ta8AhrGLs+Kl4NnP08H6H04gfxE1qMqBmkEf6JKEBdlVlTq+O\n6DASkIhXAgMBAAECggEABbaZcZJe2OKA4va5Z6T+KYtNnrUERVQH0EWoqbSCo3zN\nMmDg6GJfgkdenYY7kudF3972uRt7PpMO8ECILQxjyxG9rbR+RBG58lyrw3+PerGC\nXJnVToeh9EH70S+mCKIk+MrXzaF99pVFsCvKjf7sMur/M+RMQrIETS0szep9pGcd\nQywofSDseSWOe8LJccOad6X0A5+7/vNqH7JCFeIYZOi4aWySH64mVzLwN0b+FKa4\nBYxtQR7XO8tKqgW+KFUZLaF1NvIHKyVt8R6wb3VX8/VL+Qkrls+LFTKgm7LiClOM\nyPdegQB/G5meWpoBFZ95bHeyuoRlYh2u8RnkFPMY4QKBgQD+S+crY7NotbbPHWiE\nOhavHL2RqhX93c5dUhpCZ802NQzoZBDXBBOZJPSLsHRQ8gXozxG6uRxJmO/0zhjd\n5NUeI1hlen+rFTOuPctNV19R+mnidofZ/E6KPP0ZKUTXhThSlrHfFizzlr8cDumU\n3GynYUjqiAfZFOgoouVGeCBpCwKBgQDO8bY4ERRAZQuYZCgbLfbQwrJyJPOuqVTI\n4I8InfI2LmwgvnbNfK+vcXD5bIZS3tSh9vzWDNUpdvTkQEeciLvB2sOdNh1S2a5J\nN6R2uMqUaUF+THgy2x56RhycIVpKPaR1XkYouBCQE0R/HK3FoAl95ybABt5F1m9F\na0FnmBmlZQKBgQCIzNx3gxMo6ViG4xMuzvEVEykIC6/4+jHiEiD+SEklODTRb8N/\naDoC0NadrzdjtE9phrvK73pAPX4Y/CZ0eH4N0IXlUZkMuEMtISEVYkNtHoGHyqwa\noJi/1T9zIbhfGNPL2jWmBY/5GseEmKEf69Sn1rYbNULDjXO3KKqe1lDZMQKBgQDO\nHRy6dvhOstV7sLXpbDxZ7LFC0t8KZYkWkeKkWHw3zsDPVCSLwdZRzZESPC8FNv9d\nWdy1bQ6aP+rls8gfdmhbSgJvAMjwDfNy5UKfJKpQaw1aN9u3+1o9ursgHnAJZZ/5\nbi4+vCVy+l3MpMnG/gC2L5X+yFh2An/NCmiYP3u7qQKBgDDIbhvBbUD1AcCWgzFW\nQ4sIVCUscXBdM6gv1bCfYO4RYu3ye2xSp5CWMvT8BKogtrnKOXomO3UFJKTWMJCV\nOQwZ+kYEA7tuSTne33UKVaJ8HeuyRSBv9GMkPjgsewAALi/H+qtiOesmcyiEx/MG\n1Jo7lIDtHbiYhE1fd4PDKJeU"
  }
}
</script>

<style scoped>


.title {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  white-space: nowrap;
  font-family: Arial, Helvetica, sans-serif;
}
.block_description {
  padding-left: 10px;
  word-wrap: break-word;
}



@media (min-width: 1130px) {
  .block-class {
    border: 2px solid #eff2f5;
    border-radius: 4px;
    margin: 8px;
    padding: 30px;
    background: #F7F7F7;
  }
  h1 {
    color: black;
    padding: 0 0 0 8px;
    font-family: Arial, Helvetica, sans-serif;
    font-style: normal;
    font-weight: bold;
    text-align: left;
    margin-right: 8px;
    table-layout: fixed;
    white-space:normal;
    word-wrap: break-word;

  }
  .question{
    margin-bottom: 30px;
  }
}

@media (max-width: 1129px) and (min-width: 890px) {
  .block-class {
    border: 2px solid #eff2f5;
    border-radius: 4px;
    margin: 8px;
    padding: 30px;
    background: #F7F7F7;
  }
  h1 {
    color: black;
    padding: 0 0 0 8px;
    font-family: Arial, Helvetica, sans-serif;
    font-style: normal;
    font-weight: bold;
    text-align: left;
    margin-right: 8px;
    word-break:break-all;
    white-space:normal;
    word-wrap: break-word;
  }
  .question{
    margin-bottom: 25px;
  }
}

@media (max-width: 889px) {
  .block-class {
    border: 2px solid #eff2f5;
    border-radius: 4px;
    margin: 0px;
    padding: 0px;
    background: #F7F7F7;
  }
  h1 {
    color: black;
    padding: 0 0 0 8px;
    font-size: 24px;
    font-family: Arial, Helvetica, sans-serif;
    font-style: normal;
    font-weight: bold;
    text-align: left;
    margin-right: 8px;
    word-break:break-all;
    white-space:normal;
    word-wrap: break-word;
  }
  .question{
    margin-bottom: 15px;
  }
}

</style>