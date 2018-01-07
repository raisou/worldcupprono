<template>
  <form class="password-reset-confirm"
        v-on:submit.prevent="resetPasswordConfirm">
    <h2 class="form-register-heading">Confirmation de réinitialisation</h2>

    <div class="form-group">
      <label for="password"
             class="sr-only">
        Nouveau mot de passe
      </label>
      <input id="password"
             class="form-control"
             type="password"
             placeholder="Nouveau mot de passe"
             v-model="newPassword">
    </div>
    <div class="form-group row">
      <div class="col">
        <button class="btn btn-primary"
                type="submit">
          Confirmer réinitialisation
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
        newPassword: ''
      }
    },
    methods: {
      resetPasswordConfirm () {
        if (!this.newPassword) {
          message.error('Veuillez entrer un nouveau mot de passe')
          return
        }
        User.confirmResetPassword({
          uid: this.$route.params.uid,
          token: this.$route.params.token,
          new_password: this.newPassword
        })
        .then(() => {
          message.success('Mot de passe réinitialisé avec succès')
          this.$router.push({name: 'login'})
        })
        .catch(err => {
          if (err.response.status === 400) {
            message.error('Lien expiré')
          } else {
            message.displayGenericError()
          }
        })
      }
    }
  }
</script>
