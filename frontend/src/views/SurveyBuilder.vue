<template>
  <div id="app">
    <!-- <the-tool-bar /> -->
    <div class="editor-content" v-if="survey.currentPage === 'editor'">
      <the-panel-base :editorData="survey.editorData" />
      <the-work-space/>
    </div>

    <div class="flow-content" v-if="survey.currentPage === 'flow'">
      <the-flow-editor />
      <div class="button-row bottom-row">
        <button-base class="secondary standard" :title="'Cancel'" />
        <button-base class="primary standard" :title="'Save'" />
      </div>
    </div>
  </div>
</template>

<script>
import TheToolBar from "../components/SurveyBuilder/TheToolBar.vue";
import ThePanelBase from "../components/SurveyBuilder/ThePanelBase.vue";
import TheWorkSpace from "../components/SurveyBuilder/TheWorkSpace.vue";

import store from "../store/SurveyBuilder";
import TheFlowEditor from '../components/SurveyBuilder/TheFlowEditor.vue';
import ButtonBase from '../components/ButtonBase.vue';

export default {
  name: "SurveyBuilder",
  store: store,
  components: {
    TheToolBar,
    ThePanelBase,
    TheWorkSpace,
    TheFlowEditor,
    ButtonBase,
  },
  async created() {
    store.dispatch("loadSurvey", this.$route.params.id);
  },
  computed: {
    survey() {
      return store.getters["wholeSurvey"];
    },
  },

};
</script>

<style scoped>
/* TODO: fix up rtl button styling */
html:lang(ur) * {
  text-align: right;
}

#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 0px;
  width: 100%;
  /* height: calc(100vh - 112px); */
  overflow: hidden;
}

.editor-content {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  width: 100%;
  max-height: calc(100vh - 56px);
  min-height: calc(100vh - 56px);
  /* max-height: calc(100% - 112px); */
  overflow: hidden;

}

.button-row {
  display: flex;
  flex-direction: row;
  /* padding: 16px 0; */
  align-items: center;
}

.bottom-row {
  position: sticky;
  bottom: 0;
  left: 0;
  background-color: white;
  width: 100%;
  justify-content: flex-end;
  border-top: 1px solid #566370;
}
</style>