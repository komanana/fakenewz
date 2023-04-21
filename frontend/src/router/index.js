import Vue from 'vue'
import VueRouter from 'vue-router'
import SurveyBuilder from '../views/SurveyBuilder.vue'
import Index from "../views/Index"
import Login from '../views/login'
import Signup from '../views/signup'
import User from '../views/userProfile'
import MySurvey from '../views/mySurvey'
import forgetPassword from '../views/forgetPassword'
import resetPassword from '../views/resetPassword'
import verifyEmail from '../views/verifyEmail'
import survey from '../views/survey';
import SurveyTaker from "../components/SurveyTaker/SurveyTaker";
import Success from "../components/SurveyTaker/Success";
import MultipleChoice from "../components/SurveyTaker/MultipleChoice";
import Bin from "../views/Bin"

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/build-survey',
  //   name: 'Survey Builder',
  //   component: SurveyBuilder
  // },
  {
    path: '/build-survey/:id',
    name: 'Survey Builder',
    component: SurveyBuilder,
    props: true

  },
  {
    path: '/preview/:id',
    name: 'preview',
    component: SurveyTaker,
  },
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    name: "login",
    path: '/login',
    component: Login,
    meta: {
      title: 'login',
      isAuth: false
    }
  },
  {
    name: "signup",
    path: '/signup',
    component: Signup,
    meta: {
      title: 'register',
      isAuth: false
    }
  },
  {
    name: "user",
    path: '/user',
    component: User,
    meta: {
      title: 'userProfile',
      isAuth: true
    }
  },
  {
    name: "mySurvey",
    path: '/my_survey',
    component: MySurvey,
    meta: {
      title: 'My survey',
    }
  },
  {
    name: "forget_password",
    path: '/forget',
    component: forgetPassword,
  },
  {
    name: "reset_password",
    path: '/password_reset_confirm',
    component: resetPassword,
  },
  {
    name: "Bin",
    path: '/Bin',
    component: Bin,
  },
  {
    name: "verify_email",
    path: '/verification/email',
    component: verifyEmail,
  },
  {
    name: "survey",
    path: '/survey/:id',
    component: survey
  },
  {
    path: '/surveytaker/:code',
    name: "surveytaker",
    component: SurveyTaker,
  },
  {
    path: '/success',
    name: "Success",
    component: Success
  },
]

const router = new VueRouter({
  mode: "history",
  routes: routes,
  base: __dirname,
})

export default router
