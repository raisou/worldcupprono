import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import * as actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authenticated: false,
    message: '',
    token: null
  },
  actions,
  mutations
})
