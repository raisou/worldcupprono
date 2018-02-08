import axios from 'axios'
import {addAuthenticationHeader} from '@/api/jwt.js'

export default {
  getUserInfo (state) {
    return axios.get('/api/auth/me/', addAuthenticationHeader(state.token))
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
