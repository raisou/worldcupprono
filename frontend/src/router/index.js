import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
import Home from '@/views/Home'
import Login from '@/views/Login'
import Board from '@/views/Board'
import Account from '@/views/Account'
import Register from '@/views/Register'
import Dashboard from '@/views/Dashboard'
import PasswordReset from '@/views/PasswordReset'
import UserActivation from '@/views/UserActivation'
import PasswordResetConfirm from '@/views/PasswordResetConfirm'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'registration',
      component: Register
    },
    {
      path: '/activate/:uid/:token',
      name: 'userActivation',
      component: UserActivation
    },
    {
      path: '/password-reset',
      name: 'passwordReset',
      component: PasswordReset
    },
    {
      path: '/password-reset/confirm/:uid/:token',
      name: 'passwordResetConfirm',
      component: PasswordResetConfirm
    },
    {
      path: '/account',
      name: 'account',
      component: Account,
      meta: { label: 'Mon compte', requiresAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: { label: 'Mes pronos', requiresAuth: true }
    },
    {
      path: '/board/:boardId',
      name: 'board',
      component: Board,
      meta: { label: 'Tableau', requiresAuth: true }
    },
    {
      path: '*',
      redirect: { name: 'home' }
    }
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
