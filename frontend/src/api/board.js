import axios from 'axios'

export default {
  all () {
    return axios.get('/api/boards/')
  },
  create (board) {
    return axios.post(
      '/api/boards/',
      {name: board}
    )
  },
  get (boardId) {
    return axios.get(
      '/api/boards/' + boardId + '/'
    )
  },
  updateName (id, board) {
    return axios.patch(
      '/api/boards/' + id + '/',
      board
    )
  },
  delete (boardId) {
    return axios.delete(
      '/api/boards/' + boardId + '/'
    )
  },
  leave (boardId) {
    return axios.post(
      '/api/boards/' + boardId + '/leave/',
      {}
    )
  },
  inviteEmails (boardId, emails) {
    return axios.post(
      '/api/boards/' + boardId + '/invite/',
      {emails: emails}
    )
  }
}
