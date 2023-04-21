<template>
    <div class = "main">
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <div class = "window">
            <!-- Reset password block -->
            <p class = "title">{{ $t("g5.Reset your password") }}</p>
            <img alt="" class="line" src="imagesine.png" />
            <p class = "msg">{{ $t("g5.Enter new password") }}</p>
            <div>
                <input class = "input-box" ref="input1" type="password" v-model="password" maxlength="30" @blur="strongPassWdCheck">
                <font-awesome-icon class="eye" v-show="show1" @click="showPassword" icon="eye" />
                <font-awesome-icon class="eye" v-show="!show1" @click="showPassword" icon="eye-slash" />
            </div>
            <p class = "msg">{{ $t("g5.Confirm your password") }}</p>
            <div>
                <input class = "input-box" ref="input2" type="password" v-model="confirmPassword" maxlength="30" @blur="repeatPasswordCheck">
                <font-awesome-icon class="eye" v-show="show1" @click="showPassword" icon="eye" />
                <font-awesome-icon class="eye" v-show="!show1" @click="showPassword" icon="eye-slash" />
            </div>
            <img alt="" class="line" src="imagesine.png" />
            <button class = "submit" @click="handleSubmit">{{ $t("g5.SUBMIT") }}</button>
        </div>
    </div>
</template>

<script>
export default {
    name:"resetPassword",
    data() {
        return{
            password: "",
            confirmPassword:"",
            uid: this.$route.query.uid,
            token: this.$route.query.token,
            show1: false,
        };
    },
    methods:{
        //Strong password check
        strongPassWdCheck(){
            const nPassword = this.password.toString()
            /**
             * At least 8 characters long
             Contains at least one uppercase letter
             Contains at least one lowercase letter
             Contains at least one digit
             */
            let StrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!.@#$%^&*()_+]).{8,}$/;
            if(!(StrongPasswordRegex.test(nPassword))){
                alert(`
          At least 8 characters long
          Contains at least one uppercase letter
          Contains at least one lowercase letter
          Contains at least one digit
          Contains at least one special character
          `)
                this.password = ''
            }
        },
        // check the repeat password
        repeatPasswordCheck(){
            if(this.password !== this.confirmPassword ){
                // alert($t());
                alert('The repeat password should be the same with the old password');
            }
        },
        handleSubmit() {
            this.$axios.post("/account/password/reset/confirm/",{
                new_password1: this.password,
                new_password2: this.confirmPassword,
                uid: this.uid,
                token: this.token,
            }).then(res => {
                alert("Congratulation, reset password successfully!",res);
                this.$router.replace({name: "login"});
            }).catch(err => {
                let error = err.response.data.Message
                let errorMessage = ''
                for (let i = 0; i < error.length; i++){
                    if (error[i] === 1){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg1")
                    }
                    if (error[i] === 2){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg2")
                    }
                    if (error[i] === 3){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg3")
                    }
                    if (error[i] === 4){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg4")
                    }
                    if (error[i] === 5){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg5")
                    }
                    if (error[i] === 6){
                        errorMessage = errorMessage + this.$t("forgetpwd.msg6")
                    }
                }
                alert(errorMessage)
            })
        },
        showPassword() {
            if (this.show1 == false) {
                this.$refs.input1.type = "text";
                this.$refs.input2.type = "text";
                this.show1 = !this.show1;
            }else{
                this.$refs.input1.type = "password";
                this.$refs.input2.type = "password";
                this.show1 = !this.show1;
            }
        }
    },
}
</script>

<style scoped>
.main {
    position: relative;
    height:800px;

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
    border: 2px solid black;
    border-radius: 16px;
    padding: 20px 0 18px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 999;
    width: 465px;
}
.title {
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
    font-size: 16px;
    font-weight: 700;
    line-height: normal;
    color: dimgray;
    margin-bottom: 9px;
    margin-left: 15px;
}
.input-box {
    width: 396px;
    height: 32px;
    background-color: white;
    margin-bottom: 30px;
    margin-left: 15px;
    border-radius: 4px;
    border: 2px solid linen;
}
.eye {
    margin-left: 11px;
    margin-right: 15px;
    cursor: pointer;
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
    opacity: .3;
    cursor: pointer;
}

</style>