// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'babel-polyfill'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'flag-icon-css/css/flag-icon.css'
import lodash from 'lodash'

Vue.use(BootstrapVue)
Vue.prototype.$_ = lodash
Vue.config.productionTip = false

// filters
Vue.filter('lower', function (value) {
  if (!value) return ''
  return value.toLowerCase()
})

Vue.filter('default_if_null', function (value, arg) {
  return value || arg
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App },
  store
})
