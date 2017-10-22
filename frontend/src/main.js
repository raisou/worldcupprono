// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import store from './store'
import router from './router'
import Worldcuppronos from './Worldcuppronos'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#worldcuppronos',
  router,
  template: '<Worldcuppronos/>',
  components: { Worldcuppronos },
  store
})
