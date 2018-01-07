<template>
  <form class="password-reset"
        v-on:submit.prevent="resetPassword">
    <h2 class="form-register-heading">Réinitialisation de mot de passe</h2>

    <div class="form-group">
      <label for="email"
             class="sr-only">
        Email
      </label>
      <input id="email"
             class="form-control"
             type="email"
             placeholder="Email"
             autofocus
             v-model="email">
    </div>
    <div class="form-group row">
      <div class="col">
        <button class="btn btn-primary"
                type="submit">
          Réinitialiser mon mot de passe
        </button>
      </div>
    </div>
  </form>
</template>

<script>
  import User from '@/api/user'
  import message from '@/services/message'

  export default {
    data () {
      return {
        email: ''
      }
    },
    methods: {
      resetPassword () {
        if (!this.email) {
          message.error("Vous devez indiquer l'adresse email de votre compte")
        } else {
          User.resetPassword({email: this.email})
            .then(() => {
              message.success('Si votre adresse est reconnue, vous allez bientôt recevoir un email avec les instructions à suivre')
              this.email = ''
            })
            .catch(() => {
              message.displayGenericError()
            })
        }
      }
    }
  }
</script>

<style scoped>

</style>
