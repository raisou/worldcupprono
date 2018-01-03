import axios from 'axios'

export default {
  addAuthorizationHeader (token) {
    return {
      headers: { Authorization: `JWT ${token}` }
    }
  },
  getMatchs (state) {
    return axios.get('/api/matchs/', this.addAuthorizationHeader(state.token))
  },
  saveProno (prono, state) {
    return axios.post(
      '/api/pronos/',
      prono,
      this.addAuthorizationHeader(state.token)
    )
  },
  updateProno (id, prono, state) {
    return axios.put(
      '/api/pronos/' + id + '/',
      prono,
      this.addAuthorizationHeader(state.token)
    )
  }
}
