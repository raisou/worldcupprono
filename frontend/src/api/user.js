import axios from 'axios'

export default {
  addAuthorizationHeader (token) {
    return {
      headers: { Authorization: `JWT ${token}` }
    }
  },
  getUserInfo (state) {
    return axios.get('/api/auth/me/', this.addAuthorizationHeader(state.token))
  }
}
