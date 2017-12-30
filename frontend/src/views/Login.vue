<template>
  <div>
    <form class="form-signin"
          v-on:submit.prevent="signIn"
          v-if="!authenticated">
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
                  type="button">
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
    <p class="text-center"
       v-else>
      Vous êtes déjà connecté
    </p>
  </div>
</template>

<script>
  import Auth from '../api/auth'
  import message from '../services/message'
  import {mapState} from 'vuex'

  export default {
    data () {
      return {
        username: '',
        password: ''
      }
    },
    computed: mapState([
      'authenticated'
    ]),
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
</script>

<style scoped>
  .form-signin {
    max-width: 330px;
    padding: 15px;
    margin: 150px auto;
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
  .form-signin .form-group {
    margin-bottom: 0;
  }
</style>
