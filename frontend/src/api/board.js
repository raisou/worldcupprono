import axios from 'axios'
import {addAuthenticationHeader} from '@/api/jwt.js'

export default {
  all (state) {
    return axios.get('/api/boards/', addAuthenticationHeader(state.token))
  },
  create (board, state) {
    return axios.post(
      '/api/boards/',
      {name: board},
      addAuthenticationHeader(state.token)
    )
  },
  get (boardId, state) {
    return axios.get(
      '/api/boards/' + boardId + '/',
      addAuthenticationHeader(state.token)
    )
  },
  updateName (id, board, state) {
    return axios.patch(
      '/api/boards/' + id + '/',
      board,
      addAuthenticationHeader(state.token)
    )
  },
  delete (boardId, state) {
    return axios.delete(
      '/api/boards/' + boardId + '/',
      addAuthenticationHeader(state.token)
    )
  },
  leave (boardId, state) {
    return axios.post(
      '/api/boards/' + boardId + '/leave/',
      {},
      addAuthenticationHeader(state.token)
    )
  },
  inviteEmails (boardId, emails, state) {
    return axios.post(
      '/api/boards/' + boardId + '/invite/',
      {emails: emails},
      addAuthenticationHeader(state.token)
    )
  }
}
