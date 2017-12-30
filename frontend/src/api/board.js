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
  }
}
