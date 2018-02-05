import axios from 'axios'

export default {
  getUserInfo () {
    return axios.get('/api/auth/me/')
  },
  resetPassword (email) {
    return axios.post('/api/auth/password/reset/', email)
  },
  confirmResetPassword (password) {
    return axios.post('/api/auth/password/reset/confirm/', password)
  },
  activate (token) {
    return axios.post('/api/auth/users/activate/', token)
  }
}
