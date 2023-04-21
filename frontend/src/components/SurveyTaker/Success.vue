<template>
  <body>

    <img :src="imgSrc" width="100%" height="100%" alt="" />

  <div class="box">
    
    <h1>
      Thanks for your participation
    <br>
    <a
    class="action-btn"
    @click="showlinkDialogVisible(code)"
    >{{ $t('g5.Share') }}
    </a>
    </h1>
    
  </div>
  

  <el-dialog
      :title="testTitle"
      :visible.sync="linkDialogVisible"
      :modal="false"
      width="30%"
      center
    >
      <el-row class="linkTop1">
        <el-col :offset="2">
          <i class="el-icon-link"></i>
          {{ $t("g5.Get the link or share on social") }}
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="18" :offset="1">
          <el-form class="form-side3">
            <el-link type="primary" @click="jumpToSurveyTaker">{{ link }}</el-link>
          </el-form>
        </el-col>
        <el-col :span="2">
          <el-button
            type="info"
            v-clipboard:copy="link"
            v-clipboard:success="onCopy"
            v-clipboard:error="onError"
            >
            {{ $t("g5.CopyLink") }}</el-button
          >
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8" :offset="8">
          <img :src="dataUrl" id="123123"/>
        </el-col>

      </el-row>
      <span slot="footer" class="dialog-footer">
        <el-button @click="downloadQR">Download QR</el-button>

        <el-button type="primary" @click="linkDialogVisible = false"
          >{{ $t("g5.Finish") }}</el-button
        >
      </span>
    </el-dialog>
  </body>
</template>

<script>
import QRCode from "qrcode";
export default {
  name: "Success",
  data(){
    return{
      imgSrc: require("./images/success.jpg"),
      link: " ",
      code:'',
      linkDialogVisible: false,
      DialogTitle: '  ',
      dataUrl: '',
    };
  },
  created() {
    this.code = this.$route.query.code;
    this.link = process.env.VUE_APP_WEBSITE + 'surveytaker/' + this.code
  },
  watch:{
    link (n,o) {
      if (n) {
        QRCode.toDataURL(n)
        .then(url => {
          console.log(url)
          this.dataUrl = url
        })
        .catch(err => {
          console.error(err)
        })
      }
    }
  },
  methods: {
    showlinkDialogVisible(code) {
      this.linkDialogVisible = true;
      this.link = process.env.VUE_APP_WEBSITE + 'surveytaker/' + code
    },
    downloadQR() {
      var base64 = this.dataUrl; // imgSrc 就是base64哈
      var byteCharacters = atob(
        base64.replace(/^data:image\/(png|jpeg|jpg);base64,/, "")
      );
      var byteNumbers = new Array(byteCharacters.length);
      for (var i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      var byteArray = new Uint8Array(byteNumbers);
      var blob = new Blob([byteArray], {
        type: undefined,
      });
      var aLink = document.createElement("a");
      aLink.download = "图片名称.jpg"; //这里写保存时的图片名称
      aLink.href = URL.createObjectURL(blob);
      aLink.click()
    },
    jumpToSurveyTaker(){
      window.open(this.link, "_blank");
      this.linkDialogVisible = false
    },
  },
}
</script>

<style scoped>

.background{

}
body{
  width:100%;
  height:100%;
  z-index:0;
  position: absolute;
}


@media (min-width: 890px) {
  h1{
    color: #ffffff;
    text-transform: uppercase;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    margin: 0;
    padding: 0;
    font-size: 10em;
    text-align: center;
    text-shadow: 0px 5px 20px rgba(0,0,0,1);
    mix-blend-mode: overlay;
  }
}
@media (max-width: 889px) {
  h1{
    color: #ffffff;
    text-transform: uppercase;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    margin: 0;
    padding: 0;
    font-size: 50px;
    text-align: center;
    text-shadow: 0px 5px 20px rgba(0,0,0,1);
    mix-blend-mode: overlay;
  }
}
.main {
  padding: 30px;
}

.el-dialog {
  z-index: 10000;
}
</style>