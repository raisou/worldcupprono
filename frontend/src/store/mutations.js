import * as types from './mutation-types'

export default {
  [types.LOGIN] (state) {
    state.authenticated = true
  },
  [types.LOGOUT] (state) {
    state.authenticated = false
    state.token = null
    state.matchs = []
    state.boards = []
  },
  [types.SET_TOKEN] (state, { token }) {
    state.token = token
  },
  [types.SET_USER_INFO] (state, { user }) {
    state.me = user
  },
  [types.SET_BOARDS] (state, { boards }) {
    state.boards = boards
  },
  [types.DELETE_BOARD] (state, { id }) {
    state.boards = state.boards.filter(board => {
      return board.id !== id
    })
  },
  [types.SET_MATCHS] (state, { matchs }) {
    state.matchs = matchs
  },
  [types.SET_MESSAGE] (state, { message }) {
    state.message = message
  },
  [types.CLEAN_MESSAGE] (state) {
    state.message = { text: '', status: 'success' }
  },
  [types.SET_CONFIRMATION_MODAL] (state, { modal }) {
    state.modal = modal
  }
}
