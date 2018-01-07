import Auth from '../api/auth'
import message from '../services/message'

var loginMixin = {
  methods: {
    signIn () {
      if (this.formIsValid()) {
        Auth.login({username: this.username, password: this.password})
          .then(response => {
            this.$store.dispatch('login', {token: response.token})
            this.$router.push({name: 'home'})
          })
          .catch(err => {
            if (err.response && err.response.status === 400) {
              message.error(err.response.data.non_field_errors[0])
            } else {
              message.displayGenericError()
            }
          })
      }
    }
  }
}

export default loginMixin
