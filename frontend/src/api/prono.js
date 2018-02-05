import axios from 'axios'

export default {
  getMatchs () {
    return axios.get('/api/matchs/')
  },
  saveProno (prono) {
    return axios.post(
      '/api/pronos/',
      prono
    )
  },
  updateProno (id, prono) {
    return axios.put(
      '/api/pronos/' + id + '/',
      prono
    )
  }
}
