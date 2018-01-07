<template>
  <div>
    <form class="login"
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
               v-model="password" />
      </div>
      <div class="form-group row">
        <div class="col">
          <button class="btn btn-primary btn-block"
                  type="submit">
            Se connecter
          </button>
        </div>
        <div class="col">
          <button id="registerButton"
                  class="btn btn-secondary btn-block"
                  type="button"
                  v-on:click="$router.push({name: 'registration'})">
            S'enregistrer
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
  import {mapState} from 'vuex'
  import loginMixin from '../mixins/login'

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
