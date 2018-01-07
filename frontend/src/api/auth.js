import axios from 'axios'

export default {
  register (credentials) {
    return axios.post('/api/auth/users/create/', credentials).then(response => {
      return response.data
    })
  },
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
