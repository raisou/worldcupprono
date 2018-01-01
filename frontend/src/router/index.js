import Vue from 'vue'
import store from '../store'
import Router from 'vue-router'
import Home from '@/views/Home'
import Login from '@/views/Login'
import Account from '@/views/Account'
import Dashboard from '@/views/Dashboard'

Vue.use(Router)

const router = new Router({
  routes: [
    { path: '/', name: 'home', component: Home, meta: { requiresAuth: true } },
    { path: '/login', name: 'login', component: Login },
    { path: '/account', name: 'account', component: Account, meta: { requiresAuth: true } },
    { path: '/dashboard', name: 'dashboard', component: Dashboard, meta: { requiresAuth: true } },
    { path: '*', redirect: { name: 'home' } }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.state.authenticated) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

export default router
