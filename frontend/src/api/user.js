import axios from 'axios'

export default {
  addAuthorizationHeader (token) {
    return {
      headers: { Authorization: `JWT ${token}` }
    }
  },
  getUserInfo (state) {
    return axios.get('/api/auth/me/', this.addAuthorizationHeader(state.token))
  },
  resetPassword (email) {
    return axios.post('/api/auth/password/reset/', email)
  },
  confirmResetPassword (password) {
    return axios.post('/api/auth/password/reset/confirm/', password)
  }
}
