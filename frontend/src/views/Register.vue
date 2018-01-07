<template>
  <div>
    <form class="register"
          v-on:submit.prevent="register"
          v-if="!authenticated">
      <h2 class="form-register-heading">Enregistrement</h2>

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
        <label for="email"
               class="sr-only">
          Email
        </label>
        <input id="email"
               class="form-control"
               type="text"
               placeholder="Email"
               v-model="email" />
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
               v-model="password" />
      </div>
      <div class="form-group row">
        <div class="col">
          <button class="btn btn-primary btn-block"
                  type="submit">
            S'enregistrer
          </button>
        </div>
      </div>
    </form>
    <p class="text-center"
       v-else>
      Vous êtes déjà connecté
    </p>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import Auth from '../api/auth'
  import loginMixin from '../mixins/login'
  import message from '../services/message'

  export default {
    data () {
      return {
        username: '',
        email: '',
        password: ''
      }
    },
    mixins: [loginMixin],
    computed: mapState([
      'authenticated'
    ]),
    methods: {
      formIsValid () {
        if (!this.username || !this.email || !this.password) {
          message.error('Tous les champs sont obligatoires')
          return false
        }
        return true
      },
      register () {
        if (this.formIsValid()) {
          Auth.register({
            username: this.username, email: this.email, password: this.password
          })
          .then(() => {
            message.success('Bienvenue')
            this.signIn()
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

</style>
