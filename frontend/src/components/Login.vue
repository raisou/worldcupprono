<template>
  <form class="form-signin"
        v-on:submit.prevent="signIn">
    <h2 class="form-signin-heading">Connection</h2>

    <div class="form-group">
      <label for="username"
             class="sr-only">
        Login
      </label>
      <input id="username"
             class="form-control"
             type="text"
             placeholder="Login"
             autofocus
             v-model="username" />
    </div>
    <div class="form-group">
      <label for="password"
             class="sr-only">
        Mot de passe
      </label>
      <input id="password"
             class="form-control"
             type="password"
             placeholder="Mot de passe"
             required
             v-model="password" />
    </div>
    <div class="form-group row">
      <div class="col">
        <button class="btn btn-lg btn-primary btn-block"
                type="submit">
          Sign in
        </button>
      </div>
      <div class="col">
        <button id="registerButton"
                class="btn btn-lg btn-secondary btn-block"
                type="button"
                v-on:click="register">
          Register
        </button>
      </div>
    </div>
    <div class="form-group mb-0">
      <button id="forgot-password"
              class="btn btn-link btn-sm p-0"
              type="button"
              v-on:click="$router.push({name: 'passwordReset'})">
        <small>Mot de passe oublé ?</small>
      </button>
    </div>
  </form>
</template>

<script>
  import User from '../api/user'
  import message from '../services/message'

  export default {
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      formIsValid () {
        if (!this.username || !this.password) {
          message.error('Tous les champs sont obligatoires')
          return false
        }
        return true
      },
      signIn () {
        if (this.formIsValid()) {
          const baseURL = this.baseURL
          User.login({email: this.email, password: this.password}, {baseURL})
            .then(response => {
              this.$store.dispatch('login', {token: response.token, baseURL})
              this.$router.push({name: 'home'})
            })
            .catch(err => {
              if (err.response === undefined && baseURL !== 'https://lesspass.com') {
                message.error(this.$t('DBNotRunning', 'Your LessPass Database is not running'))
              } else if (err.response && err.response.status === 400) {
                message.error(this.$t('LoginIncorrectError', 'The email and password you entered did not match our records. Please double-check and try again.'))
              } else {
                message.displayGenericError()
              }
            })
        }
      },
      register () {
        if (this.formIsValid()) {
          const baseURL = this.baseURL
          User.register({email: this.email, password: this.password}, {baseURL})
            .then(() => {
              message.success(this.$t('WelcomeRegister', 'Welcome {email}, thank you for signing up.', {email: this.email}))
              this.signIn()
            })
            .catch(err => {
              if (err.response && typeof err.response.data.email !== 'undefined') {
                if (err.response.data.email[0].indexOf('already exists') !== -1) {
                  message.error(this.$t('EmailAlreadyExist', 'This email is already registered. Want to login or recover your password?'))
                }
                if (err.response.data.email[0].indexOf('valid email') !== -1) {
                  message.error(this.$t('EmailInvalid', 'Please enter a valid email'))
                }
              } else {
                message.displayGenericError()
              }
            })
        }
      }
    }
  }
</script>

<style scoped>
  .form-signin {
    max-width: 330px;
    padding: 15px;
    margin: 0 auto;
  }
  .form-signin .form-signin-heading,
  .form-signin .checkbox {
    margin-bottom: 10px;
  }
  .form-signin .checkbox {
    font-weight: 400;
  }
  .form-signin .form-control {
    position: relative;
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
  }
  .form-signin .form-control:focus {
    z-index: 2;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
