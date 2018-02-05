import User from '@/api/user'
import Auth from '@/api/auth'
import Board from '@/api/board'
import Prono from '@/api/prono'
import router from '@/router'
import message from '@/services/message.js'
import * as types from './mutation-types'

// Auth

export const login = ({ commit }, payload) => {
  commit(types.SET_TOKEN, payload)
  commit(types.LOGIN)
}

export const logout = ({ commit }) => {
  commit(types.LOGOUT)
  router.push('/login')
}

export const refreshToken = ({ commit, state }) => {
  const token = state.token
  if (token) {
    Auth.requestNewToken({ token })
      .then(newToken => commit(types.SET_TOKEN, { token: newToken }))
      .catch(() => commit(types.LOGOUT))
  }
}

// User

export const getUserInfo = ({ commit, state }) => {
  if (state.authenticated) {
    User.getUserInfo().then(response => {
      const user = response.data
      commit(types.SET_USER_INFO, { user })
      return user
    })
  }
  return Promise.resolve([])
}

// Boards

export const saveBoard = ({ commit, state }, board) => {
  Board.create(board).then(() => {
    getBoards({ commit, state })
  })
}

export const getBoards = ({ commit, state }) => {
  if (state.authenticated) {
    return Board.all().then(response => {
      const boards = response.data
      commit(types.SET_BOARDS, { boards })
      return boards
    })
  }
  return Promise.resolve([])
}

export const leaveBoard = ({ commit }, board) => {
  Board.leave(board.id).then(() => {
    commit(types.DELETE_BOARD, board)
    message.success('Vous avez quitté le tableau ' + board.name)
  }).catch(() => {
    message.displayGenericError()
  })
}

export const deleteBoard = ({ commit }, board) => {
  Board.delete(board.id).then(() => {
    commit(types.DELETE_BOARD, board)
    message.success('Le tableau ' + board.name + ' a été supprimé')
  }).catch(() => {
    message.displayGenericError()
  })
}

// Prono

export const getMatchs = ({ commit, state }) => {
  if (state.authenticated) {
    return Prono.getMatchs().then(response => {
      let matchs = []
      response.data.forEach(function (value, key) {
        if (!value.prono) {
          value.prono = {
            id: null,
            score_domicile: 0,
            score_visitor: 0
          }
        }
        matchs.push(value)
      })
      commit(types.SET_MATCHS, { matchs })
      return matchs
    })
  }
  return Promise.resolve([])
}

export const saveProno = ({ commit }, prono) => {
  Prono.saveProno(prono)
}

// Messages

export const displayMessage = ({ commit }, payload) => {
  commit(types.SET_MESSAGE, payload)
}

export const cleanMessage = ({ commit }) => {
  commit(types.CLEAN_MESSAGE)
}

// Modal

export const displayConfirmationModal = ({ commit }, payload) => {
  commit(types.SET_CONFIRMATION_MODAL, payload)
}
