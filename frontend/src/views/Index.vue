<template>
    <div>
        <div class="page1">
            <el-container class="content-box">
                <el-aside  width="500px" class="content-aside">
                    <h1>{{ $t("g5.Welcome to fakenewz Survey Platform!") }}</h1>
                    <p>{{ $t("home.title1") }}</p>
                    <p>{{ $t("home.title2") }}</p>
                    <p>{{ $t("home.title3") }}</p>
                    <div>
                        <el-button plain icon="el-icon-s-promotion" @click="getStart">{{ $t("home.getStart") }}</el-button>
                        <el-button type="info" icon="el-icon-edit" @click="goToAnchor">{{ $t("home.learnMore") }}</el-button>
                    </div>
                </el-aside>
                <el-main class="video-container" style="text-align: right">
                    <youtube class="youtube-video" video-id="mlQuOl2ZVFY" ref="youtube" width="100%" ></youtube>
                </el-main>
            </el-container>
        </div>

        <div class="page2" v-if="true">
            <div class="content-box">
                <div class="subtitle">
                    <h1>{{ $t("home.functionIntro") }}</h1>
                </div>
                <el-carousel :interval="4000" type="card" height="270px">
                    <div class="carousel-box">
                        <el-carousel-item v-for="item in images" :key="item.title">
                            <h1>{{$t(item.title)}}</h1>
                            <el-container>
                                <el-aside width="250px">
                                    <ul v-for="i in item.info" :key="i">
                                        <li>{{$t(i)}}</li>
                                    </ul>
                                </el-aside>
                                <el-main>
                                    <img id="carousel-img" :src="item.url" height="200px"/>
                                </el-main>
                            </el-container>
                        </el-carousel-item>
                    </div>
                </el-carousel>
            </div>
        </div>

        <div id="page3" v-if="true">
            <div class="content-box">
                <div class="subtitle">
                    <h1>{{ $t("home.learnMoreTitle") }}</h1>
                    <p>{{ $t("home.learnMoreDes") }}</p>
                </div>
                <el-container>
                    <el-aside width="400px" style="margin-left: 80px">
                        <h1>1. {{ $t("home.step1Title") }}</h1>
                        <ul>
                            <li>{{ $t("home.step1Des1") }}</li>
                            <li>{{ $t("home.step1Des2") }}</li>
                            <li>{{ $t("home.step1Des3") }}</li>
                        </ul>
                        <lottie :options="defaultOptions3"
                                :width="240"
                                :height="240"
                                style="position: relative;left: 100px;bottom: 60px"/>
                    </el-aside>
                    <el-main style="text-align: right">
                        <img src="./images/surveybuild.png" alt="" style="width: 600px">
                    </el-main>
                </el-container>

            </div>
        </div>

        <div class="page2" v-if="true">
            <div class="content-box">
                <el-container>
                    <!-- <el-aside width="600px" style="margin-left: 30px"> -->
                    <el-aside width="600px">
                        <img src="./images/publish.png" alt="" style="width: 500px">
                    </el-aside>
                    <el-main>
                        <h1>2. {{ $t("home.step2Title") }}</h1>
                        <ul>
                            <li>{{ $t("home.step2Des1") }}</li>
                            <li>{{ $t("home.step2Des2") }}</li>
                            <li>{{ $t("home.step2Des3") }}</li>
                        </ul>
                        <lottie :options="defaultOptions"
                                :width="200"
                                :height="200"
                                style="position: relative;left: 100px;bottom: 20px"/>
                    </el-main>
                </el-container>

            </div>
        </div>

        <div class="page1" v-if="true">
            <div class="content-box">
                <el-container>
                    <el-aside width="500px">
                        <div style="margin-left: 80px">
                            <h1>3. {{ $t("home.step3Title") }}</h1>
                            <ul>
                                <li>{{ $t("home.step3Des1") }}</li>
                                <li>{{ $t("home.step3Des2") }}</li>
                                <li>{{ $t("home.step3Des3") }}</li>
                            </ul>
                        </div>
                        <lottie :options="defaultOptions2"
                                :width="200"
                                :height="200"
                                style="position: relative;left: 100px;bottom: 20px"/>
                    </el-aside>
                    <el-main style="text-align: right">
                        <img src="./images/result.png" alt="" style="width: 600px">
                    </el-main>
                </el-container>

            </div>
        </div>
    </div>
</template>

<script src="vue-youtube/dist/vue-youtube.js"></script>
<script>
import VueYoutube from 'vue-youtube'
import Vue from "vue";
import * as animationData from '@/assets/publish.json'
import * as animationData2 from '@/assets/analyse.json'
import * as animationData3 from '@/assets/create.json'

Vue.use(VueYoutube)

export default {
    data() {
        return {
            defaultOptions: { animationData:animationData.default },
            defaultOptions2: { animationData:animationData2.default },
            defaultOptions3: { animationData:animationData3.default },

            images: [
                {
                    title: 'home.cardTitle1' ,
                    info:['home.card1Info1',
                        'home.card1Info2',
                        'home.card1Info3',
                        'home.card1Info4',
                        'home.card1Info5',
                        'home.card1Info6'],
                    url: require("./images/carousels/bill payment.png")
                },
                {
                    title:'home.cardTitle2',
                    info:['home.card2Info1',
                        'home.card2Info2',
                        'home.card2Info3'],
                    url: require("./images/carousels/app development.png")
                },
                {
                    title:'home.cardTitle3',
                    info:['home.card3Info1',
                        'home.card3Info2',
                        'home.card3Info3',
                        'home.card3Info4',
                        'home.card3Info5'],
                    url: require("./images/carousels/bill payment.png")
                },
                {
                    title:'home.cardTitle4',
                    info:['home.card4Info1',
                        'home.card4Info2',
                        'home.card4Info3'],
                    url: require("./images/carousels/analytics.png")
                },
            ],
        }
    },
    methods:{

        getStart(){
            this.$router.replace('/My_Survey')
        },
        goToAnchor() {
            this.$el.querySelector('#page3').scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        },
    },

}
</script>

<style scoped>
.youtube-video{
    width: 500px;
}

#page3 {
    padding: 20px;
    background-color: #d3dce6;
    height: 500px;
    color: #566370;
}
.page1 {
    padding: 20px;
    background-color: #d3dce6;
    height: 400px;
    color: #566370;
}

.page2 {
    padding: 20px;
    background-color: #fff;
    height: 400px;
    color: #566370;
}


h1 {
    font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
    font-weight: bolder;
    font-size: 40px;
}

.content-box {
    margin: 0 120px 0 120px;
}

.content-aside {
    text-align: right;
    color: #566370;
}
.content-aside div {
    text-align: center;
    margin-top: 50px;
}

.page1 .subtitle {
    text-align: center;
}

#page3 .subtitle {
    text-align: center;
}

.page2 .subtitle {
    text-align: center;
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

#carousel-img {
    position: relative;
    bottom: 60px
}

.carousel-box h1 {
    margin-left: 20px;
    font-size: 30px;
}

.carousel-box ul {
    position: relative;
    bottom: 10px;
    left: 50px;
    font-size: 13px;
}


/* This is for mobile device screen */
@media screen and (max-width: 850px) {
    body {
        background-color:lightblue;
    }

    .video-container{
        width: 90%;
    }

    .content-box .content-aside{
        text-align: center;
    }

    el-aside{
        width: fit-content !important;
        margin-left: 0px !important;

    }
    .page1 {
        padding: 20px;
        background-color: #d3dce6;
        /*background-color: #d3dce6;*/
        height: fit-content;
        color: #566370;
    }
    /*banner fit start*/
    .el-aside.content-aside{
        width: 100% !important;
        margin:0 auto 0 auto;

    }

    .el-container{
        flex-direction: column;
    }

    #router-wrapper > div > div > section{
        margin: 0 auto 0 auto;
    }
    /*banner fit end*/

    /*colum function fit start*/
    .page2{
        height: fit-content;
    }

    #router-wrapper > div > div.page2 > div{
        margin: 0 auto 0 auto !important;
        width: 100%;
    }
    /*   colum fucntion fit end */


    /*colum1 fit start*/

    #page3{
        height: fit-content;
    }

    #page3 > div{
        margin: 0 auto 0 auto !important;
        width: 100%;
    }
    #page3 > div > section > aside > div{
        left: 0px !important;
        margin: 0 0 0 0 !important;
        bottom: 0px !important;

    }

    #page3 > div > section > aside{
        margin-left: 0px !important;
        width: 100% !important;
    }
    /*   colum1 fit end */

    /*colum2 fit start*/

    #router-wrapper > div > div:nth-child(4) > div > section > aside{
        width: 100% !important;
    }

    #router-wrapper > div > div:nth-child(4) > div > section > main > div{
        left: 0px !important;
        margin: 0 0 0 0 !important;
        bottom: 0px !important;
    }

    #router-wrapper > div > div:nth-child(4) > div > section{
        flex-direction: column-reverse;
    }
    /*   colum2 fit end */

    /*colum3 fit start*/
    #router-wrapper > div > div:nth-child(5) > div{
        margin: 0 auto 0 auto !important;
    }
    #router-wrapper > div > div:nth-child(5) > div > section > aside > div:nth-child(2){
        left: 0px !important;
        margin: 0 0 0 0 !important;
        bottom: 0px !important;
    }
    #router-wrapper > div > div:nth-child(5) > div > section > aside{
        width: 100% !important;
    }
    /*   colum3 fit end */

}


</style>
