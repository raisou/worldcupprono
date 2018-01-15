<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <form v-on:submit.prevent="resetPassword">
                  <h2>
                    Mot de passe oublié
                  </h2>

                  <div class="input-group mb-3">
                    <span class="input-group-addon">
                      <icon name="envelope"></icon>
                    </span>
                    <input type="email"
                           class="form-control"
                           placeholder="Email"
                           autofocus
                           v-model="email" />
                  </div>

                  <b-button variant="primary"
                            type="submit"
                            block>
                    Réinitialiser mon mot de passe
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
