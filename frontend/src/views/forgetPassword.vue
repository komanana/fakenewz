<template>
    <div>
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <div class = "main">
            <!-- forgot password block -->
            <div class = "window">
                <p class = "title">{{ $t("g5.Forgot your password?") }}</p>
                <img alt="" class="line" src="imagesine.png" />
                <p class = "msg">{{ $t("g5.Please enter your email") }}</p>
                <input class="email-box" type="text" v-model="email"/>
                <img alt="" class="line-bottom" src="imagesine.png" />
                <button class = "submit" @click="handleSubmit">{{ $t("g5.SUBMIT") }}</button>
                <!-- <p class="havenoaccount">{{ $t("g5.Dont have an account?") }}</p> -->
                <p class="havenoaccount">{{ 'Resend an confirmation email'}}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "forgetPassword",
    data() {
        return {
            email: "",
        };
    },
    methods: {
        //EMAIL format basic check
        checkEmail(){
            const email = this.email
            const atIndex = this.email.toString().indexOf('@')
            if(!(atIndex > -1)){
                alert('Please use the email address')
            }
        },
        handleSubmit() {
            this.$axios
                .post("account/password/reset/", {
                    email: this.email,
                    lang: localStorage.getItem("lang") || "en",
                })
                .then((res) => {
                    alert(
                        "The password reset email was sent sucessfully, please check your email!",
                        res
                    );
                    // console.log(res);
                    this.$router.replace({ name: "login" });
                })
                .catch((error) => {
                    alert("Failed, please check if your email is valid.", error);
                    window.location.reload();
                });
        },
    },
};
</script>

<style scoped>
.main {
    position: relative;
    height: 800px;
}

.background {
    width: 100%;
    height: 800px;
    position: relative;
}
.copyright {
    color: white;
    position: absolute;
    left: 560px;
    bottom: 0px;
    display: center;
    text-align: center;
}
.window {
    background-color: white;
    border-radius: 16px;
    padding: 20px 0 18px;
    border: 2px solid black;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 999;
}
.title {
    font-family: "Arial";
    font-size: 24px;
    font-weight: 700;
    line-height: normal;
    color: black;
    margin-bottom: 39px;
    margin-left: 90px;
}
.line {
    width: 432px;
    margin-bottom: 23px;
}

.line-bottom {
    width: 432px;
    margin-top: 20px;
    margin-bottom: 30px;
}
.msg {
    width: 400px;
    font-family: "Arial";
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    color: dimgray;
    margin-bottom: 9px;
    margin-left: 15px;
}
.email-box {
    width: 396px;
    height: 32px;
    background-color: white;
    margin-bottom: 30px;
    margin-left: 15px;
    border-radius: 4px;
    border: 2px solid linen;
}
.submit {
    background: none;
    border: 1px solid black;
    margin-bottom: 18px;
    margin-left: 13px;
    border-radius: 8px;
    padding: 13px 172px;
    font-family: "Arial";
    display: flex;
    align-items: center;
    font-size: 16px;
    font-weight: 400;
    line-height: normal;
}
.submit:hover {
    opacity: 0.7;
    cursor: pointer;
}
.havenoaccount {
    width: 180px;
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    color: dimgray;
    margin-right: 26px;
}
</style>