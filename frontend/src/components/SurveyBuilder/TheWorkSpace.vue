<template>
  <!-- Not Flow view - normal edit view -->
  <div v-if="!flowView" class="work-space">
    <div class="survey-title">
      <h1 id="title" contenteditable="true" @focusout="handleTitleInput">
        {{ surveyTitle }}
      </h1>
      <el-button id="preview_btn" type="primary" @click="showPreview()">{{
          $t('workSpace.preview')
        }}
      </el-button>
      <el-button id="save_btn" type="success" @click="saveSurvey" @saveSurvey>{{
          $t('workSpace.save')
        }}
      </el-button>
    </div>

    <line-base class="light"></line-base>
    <button-base
        class="tertiary min"
        :icon="'fas fa-plus fa-sm'"
        :title="$t('workSpace.addNewBlock')"
        @buttonPress="$store.commit('insertNewBlock', { order: 1 })"
    ></button-base>

    <line-base class="light"></line-base>
    <div class="block-segment" v-for="block in sortedBlocks" :key="block.order">
      <builder-block :block="block"/>
      <line-base class="light"></line-base>
      <button-base
          class="tertiary min"
          :icon="'fas fa-plus fa-sm'"
          :title="$t('workSpace.addNewBlock')"
          @buttonPress="
          $store.commit('insertNewBlock', { order: block.order + 1 })
        "
      ></button-base>
      <line-base class="light"></line-base>
    </div>
    <div class="shimp"></div>
  </div>

  <!-- Flow view -->
  <div v-else class="work-space">
    <div class="survey-title">
      <h1>{{ surveyTitle }}</h1>
      <el-button id="preview_btn" type="primary" @click="showPreview()">{{
          $t('workSpace.preview')
        }}
      </el-button>
      <el-button id="save_btn" type="success">{{
          $t('workSpace.save')
        }}
      </el-button>
    </div>
    <line-base class="light"></line-base>

    <the-flow-editor/>
  </div>
</template>

<script>
import SurveyServices from '../../services/SurveyServices'

import BuilderBlock from './BuilderBlock.vue'
import ButtonBase from '../../components/ButtonBase.vue'
import LineBase from './LineBase.vue'
import store from '../../store/SurveyBuilder'

import {mapGetters} from 'vuex'
import TheFlowEditor from './TheFlowEditor.vue'

export default {
  name: 'TheWorkSpace',
  store: store,
  components: {
    LineBase,
    ButtonBase,
    BuilderBlock,
    TheFlowEditor,
  },
  computed: {
    ...mapGetters(['surveyTitle', 'editorData', 'sortedBlocks', 'flowView']),
  },
  methods: {
    /**
     * Update survey title and send to backend
     * @param e - event
     */

    async handleTitleInput(e) {
      var title = e.target.innerHTML
          .replaceAll('<br>', '')
          .replaceAll('&amp', '')
          .replaceAll('&lt', '')
          .replaceAll('&gt', '')
          .replaceAll('nbsp', '')
          .replaceAll(';', '')
      console.log(title)
      store.commit('updateSurveyTitle', title)

      // Really shouldn't hardcode which survey it is
      await SurveyServices.patchSurvey(store.state.survey.id, {
        name: title,
      })
    },

    showPreview() {
      let id = store.state.survey.id
      window.open(`/preview/${id}`, "_blank");
    },

    saveSurvey() {
      this.$message({
        message: 'Save successfully',
        type: 'success',
      })
    },
  },
}
</script>

<style scoped>
html:lang(ur) * {
  text-align: right;
}


.work-space {
  background-color: #eff2f5;
  width: 100%;
  min-height: calc(100vh - 56px);
  overflow: scroll;

  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  padding: 16px;
  align-items: center;
}

.button-row {
  padding: 8px 8px 0px 8px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
}

#title {
  color: black;
  padding: 0 8px;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  text-align: left;
  max-width: 800px;
  display: flex;
  -webkit-user-modify: read-write-plaintext-only;
  -moz-user-modify: read-write-plaintext-only;
}

.survey-title:hover > *[contenteditable='true'],
.survey-title:focus > *[contenteditable='true'] {
  background-color: white;
  outline: 0;
}

.survey-title > *[contenteditable='true'] {
  padding: 8px;
  border: 2px solid white;
  border-radius: 4px;
}

.text-with-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  align-content: center;
}

.survey-title {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.block-segment {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /*max-width: 816px;*/
  /*min-width: 816px;*/
  width: 100%;
  margin: 0 auto;
}

/*.block-segment {*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  justify-content: center;*/
/*  max-width: 816px;*/
/*  min-width: 816px;*/
/*  !*width: 100%;*!*/
/*  margin: 0 auto;*/
/*}*/
.shimp {
  display: block;
  width: 100%;
  margin-bottom: 300px;

}

@media screen and (min-width: 767px) {
  .block-segment {
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 816px;
    min-width: 816px;
    margin: 0 auto;
  }

  .shimp {
    height: 200px;
    display: none;
  }
}

#preview_btn {
  position: absolute;
  right: 2%;
  top: 100px;
  width: auto;
  font-size: small;
  z-index: 9999;
}

#save_btn {
  position: absolute;
  right: 2%;
  top: 160px;
  width: auto;
  font-size: small;
  z-index: 9999;
}

.el-button--primary {
  background: #204cdc !important;
  border-color: #204cdc !important;
  color: #e7f2fe;
}

.el-button--primary:hover {
  background: #5976d5 !important;
  border-color: #5976d5 !important;
  color: #ffffff !important;
}
</style>
