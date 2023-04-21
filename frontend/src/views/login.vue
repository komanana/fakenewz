<template>
    <section>
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <div class="main">
            <div class="window">
                <p class="title">{{ $t("g5.Log in") }}</p>
<!--                <img alt="" class="line" src="imagesine.png" />-->
                <p class="msg">{{ $t("g5.Username")+' Or '+$t("g5.Email")}}</p>
                <!-- username inputbox-->
                <div class="input-container">
                    <input class="username-box" type="text" v-model="username" maxlength="30"/>
                </div>
                <p class="msg">{{ $t("g5.Password") }}</p>
                <!-- password inputbox -->
                <div class="input-container">
                    <input class="password-box" ref="input" type="password" v-model="password" maxlength="30"/>
                    <font-awesome-icon class="eye" v-show="show" @click="showPassword" icon="eye" />
                    <font-awesome-icon class="eye" v-show="!show" @click="showPassword" icon="eye-slash" />
                </div>

                <div class = "error">
                    <div id="error-message"></div>
                </div>
                <!-- forget password -->
                <a class="forgot" @click="forgetPassword">{{
                    $t("g5.Forgot your password?")
                    }}</a>
                <!-- login button -->
                <div>
                    <button @click="loginAction" class="loginButton">
                        {{ $t("g5.LOG IN") }}
                    </button>
                </div>
                <img alt="" class="line" src="imagesine.png" />
                <div class="bottom">
                    <p class="havenoaccount">{{ $t("g5.Dont have an account?") }}</p>
                    <div>
                        <button @click="signup" class="signupButton">
                            {{ $t("g5.SIGN UP") }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
// import {reqLogin} from '../api'
import pubsub from "pubsub-js";
export default {
    name: "LogIn",
    data() {
        return {
            username: "",
            password: "",
            show: false,
            // alertText: '',
            // alertShow: false,
        };
    },
    methods: {
        loginAction() {
            this.$axios
                .post("account/login/", {
                    username: this.username,
                    password: this.password,
                })
                .then((res) => {
                    // alert("Login successful", res.name);
                    //update user status
                    pubsub.publish("loginAction", true);
                    //save token on local storage
                    localStorage.setItem("token", res.data.key);
                    localStorage.setItem("username", this.username);
                    //redirect to the user profile page
                    this.$router.replace({
                        name: "mySurvey",
                    });
                })
                .catch((reason) => {
                    // alert("Login failed\n"+ JSON.stringify(reason.response.data))
                    var messages = []
                    for (var key in reason.response.data) {
                        messages.push(reason.response.data[key][0] + '<br>')
                    }

                    document.getElementById('error-message').innerHTML = this.$t('Log in failed') + ': ' + messages;

                });
        },
        forgetPassword() {
            this.$router.push({name:"forget_password",});
        },
        // async login () {
        //   let res
        //   const {username, password} = this
        //   res = await reqLogin({username, password})
        //   if (res.code === 0) {
        //     this.$router.replace({
        //       name: "user"
        //     })
        //   }
        // },
        signup() {
            this.$router.replace({
                name: "signup",
            });
        },
        showPassword() {
            if (this.show == false) {
                this.$refs.input.type = "text";
                this.show = !this.show;
            }else{
                this.$refs.input.type = "password";
                this.show = !this.show;
            }
        }
    },
    // showAlert(alertText) {
    //   this.alertShow = true
    //   this.alertText = alertText
    // }
};
</script>

<style scoped>

section{
    height: 100%;
}


.main {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    align-items: center;
    height: 100%;
    justify-content: center;
}


.window {
    background-color: white;
    border-radius: 16px;
    padding: 20px 0 18px;
    border: 2px solid black;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 70%;
    max-width: 450px;
    max-height: 520px ;
}

.input-container{
    width:100%;
}


.title {
    font-size: 24px;
    font-weight: 700;
    line-height: normal;
    color: black;
    margin-bottom: 25px;
}
.line {
    width: 100%;
    margin-bottom: 15px;
}
.msg {
    max-width: 400px;
    width: 90%;
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    color: dimgray;
    margin-bottom: 9px;
}
.username-box {
    max-width: 396px;
    width: 90%;
    height: 32px;
    background-color: white;
    margin-bottom: 20px;
    border-radius: 4px;
    border: 2px solid linen;
    margin-left: 5%;
}

.password-box {
    max-width: 366px;
    width: 80%;
    height: 32px;
    background-color: white;
    margin-bottom: 20px;
    border-radius: 4px;
    border: 2px solid linen;
    margin-left: 5%;
}
.eye {
    margin-left: 3%;
    cursor: pointer;
    width: 5%;
}
.forgot {
    font-family: "Arial";
    font-size: 14px;
    font-weight: 700;
    line-height: normal;
    color: rgba(13, 13, 209, 0.753);
    text-decoration: underline;
    margin-bottom: 31px;
    cursor: pointer;
}
.loginButton {
    background: none;
    border: 1px solid black;
    margin-bottom: 18px;
    border-radius: 8px;
    padding: 13px 100px;
    display: flex;
    align-items: center;
    font-size: 16px;
    font-weight: 400;
    line-height: normal;
}
.loginButton:hover {
    opacity: .3;
    cursor: pointer;
}
.bottom {
    display: flex;
    align-items: center;
}
.havenoaccount {
    width: 180px;
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    color: dimgray;
    margin-right: 26px;
}

.error {
    background: #FFC199; /*Change background color*/
    border-left: 9px solid #FF6600; /*Change left border color*/
    color: #2c3e50; /*Change text color*/
    width: 90%;
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    margin-bottom: 4px;
}
.signupButton {
    background: none;
    border: 1px solid black;
    border-radius: 8px;
    padding: 13px 20px 13px 20px;
    display: flex;
    align-items: center;
}
.signupButton:hover {
    opacity: .7;
    cursor: pointer;
}

@media screen and (max-width: 850px) {
    .havenoaccount{
        margin-right: 10px;

    }
    .signupButton {
        padding:10px 15px 10px 15px;
    }
}

</style>