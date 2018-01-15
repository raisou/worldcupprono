<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body v-if="!authenticated">
                <form v-on:submit.prevent="signIn">
                  <h1>Connexion</h1>
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
                  <div class="input-group mb-4">
                    <span class="input-group-addon">
                      <icon name="lock"></icon>
                    </span>
                    <input type="password"
                           class="form-control"
                           placeholder="Mot de passe"
                           v-model="password">
                  </div>
                  <b-button variant="primary"
                            size="sm"
                            class="px-2"
                            type="submit">
                    Se connecter
                  </b-button>
                  <b-button variant="secondary"
                            size="sm"
                            class="px-2"
                            v-on:click="$router.push({name: 'registration'})">
                    S'enregistrer
                  </b-button>
                  <b-button variant="link"
                            class="px-0 text-right"
                            v-on:click="$router.push({name: 'passwordReset'})">
                    Mot de passe oublié ?
                  </b-button>
                </form>
              </b-card-body>
              <b-card-body v-else>
                Vous êtes déjà connecté
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import loginMixin from '@/mixins/login'

  export default {
    data () {
      return {
        username: '',
        password: ''
      }
    },
    mixins: [loginMixin],
    computed: mapState([
      'authenticated'
    ])
  }
</script>

<style scoped>

</style>
