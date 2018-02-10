<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <form v-on:submit.prevent="resetPasswordConfirm">
                  <h2>
                    Confirmation de réinitialisation
                  </h2>

                  <div class="input-group mb-3">
                    <span class="input-group-addon">
                      <icon name="lock"></icon>
                    </span>
                    <input type="password"
                           class="form-control"
                           placeholder="Nouveau mot de passe"
                           v-model="newPassword" />
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
                    Confirmer réinitialisation
                  </b-button>
                </form>
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
  import User from '@/api/user'
  import message from '@/services/message'

  export default {
    data () {
      return {
        newPassword: '',
        confirmPassword: ''
      }
    },
    methods: {
      formIsValid () {
        if (!this.newPassword) {
          message.error('Veuillez entrer un nouveau mot de passe')
          return false
        }
        if (this.newPassword !== this.confirmPassword) {
          message.error('Les mots de passe de correspondent pas')
          return false
        }
        return true
      },
      resetPasswordConfirm () {
        if (this.formIsValid()) {
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
  }
</script>
