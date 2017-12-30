import * as types from './mutation-types'

export default {
  [types.SET_MESSAGE] (state, { message }) {
    state.message = message
  },
  [types.CLEAN_MESSAGE] (state) {
    state.message = { text: '', status: 'success' }
  }
}
