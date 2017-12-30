import * as types from './mutation-types'

export const displayMessage = ({ commit }, payload) => {
  commit(types.SET_MESSAGE, payload)
}

export const cleanMessage = ({ commit }) => {
  commit(types.CLEAN_MESSAGE)
}
