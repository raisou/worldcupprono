import axios from 'axios'

export default {
  addAuthorizationHeader (token) {
    return {
      headers: { Authorization: `JWT ${token}` }
    }
  },
  all (state) {
    return axios.get('/api/boards/', this.addAuthorizationHeader(state.token))
  },
  create (board, state) {
    return axios.post(
      '/api/boards/',
      {name: board},
      this.addAuthorizationHeader(state.token)
    )
  },
  get (boardId, state) {
    return axios.get(
      '/api/boards/' + boardId + '/',
      this.addAuthorizationHeader(state.token)
    )
  },
  inviteEmails (boardId, emails, state) {
    return axios.post(
      '/api/boards/' + boardId + '/invite/',
      {emails: emails},
      this.addAuthorizationHeader(state.token)
    )
  }
}
