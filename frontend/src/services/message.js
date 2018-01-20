import Store from '@/store'

export default {
  success (text) {
    const message = { text, status: 'success' }
    Store.dispatch('displayMessage', { message })
  },
  warning (text) {
    const message = { text, status: 'warning' }
    Store.dispatch('displayMessage', { message })
  },
  error (text) {
    const message = { text, status: 'danger' }
    Store.dispatch('displayMessage', { message })
  },
  displayGenericError () {
    this.error(
      "Oops! Une erreur s'est produite. Veuillez rééssayer un peu plus tard")
  }
}
