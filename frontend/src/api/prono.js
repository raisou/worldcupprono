import axios from 'axios'
import {addAuthenticationHeader} from '@/api/jwt.js'

export default {
  getMatchs (state) {
    return axios.get('/api/matchs/', addAuthenticationHeader(state.token))
  },
  saveProno (prono, state) {
    return axios.post(
      '/api/pronos/',
      prono,
      addAuthenticationHeader(state.token)
    )
  },
  updateProno (id, prono, state) {
    return axios.put(
      '/api/pronos/' + id + '/',
      prono,
      addAuthenticationHeader(state.token)
    )
  }
}
