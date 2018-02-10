import axios from 'axios'
import {addAuthenticationHeader} from '@/api/jwt.js'

export default {
  all (state) {
    return axios.get('/api/invitations/', addAuthenticationHeader(state.token))
  },
  accept (invitationId, state) {
    return axios.post(
      '/api/invitations/' + invitationId + '/accept/',
      {},
      addAuthenticationHeader(state.token)
    )
  },
  acceptToken (token, state) {
    return axios.post(
      '/api/invitations/accept_mail/',
      {token: token},
      addAuthenticationHeader(state.token)
    )
  },
  decline (invitationId, state) {
    return axios.post(
      '/api/invitations/' + invitationId + '/decline/',
      {},
      addAuthenticationHeader(state.token)
    )
  },
  cancel (invitationId, state) {
    return axios.post(
      '/api/invitations/' + invitationId + '/cancel/',
      {},
      addAuthenticationHeader(state.token)
    )
  },
  resend (invitationId, state) {
    return axios.post(
      '/api/invitations/' + invitationId + '/resend/',
      {},
      addAuthenticationHeader(state.token)
    )
  }
}
