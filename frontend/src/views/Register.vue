<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card no-body class="mx-4">
            <form v-on:submit.prevent="register"
                  v-if="!authenticated">
              <b-card-body class="p-4">
                <h2>
                  S'enregistrer
                </h2>
                <p class="text-muted">Créer votre compte</p>

                <div class="input-group mb-3">
                  <span class="input-group-addon">
                    <icon name="user"></icon>
                  </span>
                  <input type="text"
                         class="form-control"
                         placeholder="Username"
                         autofocus
                         v-model="username" />
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-addon">
                    <icon name="envelope"></icon>
                  </span>
                  <input type="email"
                         class="form-control"
                         placeholder="Email"
                         v-model="email" />
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-addon">
                    <icon name="lock"></icon>
                  </span>
                  <input type="password"
                         class="form-control"
                         placeholder="Mot de passe"
                         v-model="password" />
                </div>

                <div class="input-group mb-3">
                  <span class="input-group-addon">
                    <icon name="lock"></icon>
                  </span>
                  <input type="password"
                         class="form-control"
                         placeholder="Confirmation de mot de passe"
                         v-model="confirmPassword" />
                </div>

                <b-button variant="primary"
                          type="submit"
                          block>
                  S'enregistrer
                </b-button>
              </b-card-body>
            </form>
            <b-card-body class="p-4"
                        v-else>
              Vous êtes déjà connecté
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import Auth from '@/api/auth'
  import message from '@/services/message'

  export default {
    data () {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    },
    computed: mapState([
      'authenticated'
    ]),
    methods: {
      formIsValid () {
        if (!this.username || !this.email || !this.password || !this.confirmPassword) {
          message.error('Tous les champs sont obligatoires')
          return false
        }
        if (this.password !== this.confirmPassword) {
          message.error('Les mots de passe de correspondent pas')
        }
        return true
      },
      register () {
        if (this.formIsValid()) {
          Auth.register({
            username: this.username, email: this.email, password: this.password
          })
          .then(() => {
            message.success("Un email d'activation vous a été envoyé")
            this.username = ''
            this.email = ''
            this.password = ''
            this.confirmPassword = ''
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
