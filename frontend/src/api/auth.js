import axios from 'axios'

export default {
  login (credentials) {
    return axios.post('/api/auth/jwt/create/', credentials).then(response => {
      return response.data
    })
  },
  requestNewToken (token) {
    return axios.post('/api/auth/jwt/refresh/', token).then(response => {
      return response.data.token
    })
  }
}
