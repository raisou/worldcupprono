import axios from 'axios'

export default {
  addAuthorizationHeader (token) {
    return {
      headers: { Authorization: `JWT ${token}` }
    }
  },
  getMatchs (state) {
    return axios.get('/api/matchs/', this.addAuthorizationHeader(state.token))
  }
}
