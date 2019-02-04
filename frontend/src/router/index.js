import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import LogData from '@/components/log-data'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    }, 
    {
      path: '/daily',
      name: 'Health Information',
      component: LogData

    }
  ]
})
