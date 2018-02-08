<template>
  <span>
    <!-- Modal Component -->
    <b-modal id="inviteModal"
             ref="modal"
             title="Inviter des personnes au tableau"
             @ok="handleOk"
             @shown="clearEmails">
      <b-form @submit.stop.prevent="handleSubmit" novalidate>
        <b-form-input type="text"
                      v-bind:class="{'is-invalid': error}"
                      placeholder="Liste d'emails séparés par une virgule"
                      v-model="emails">
        </b-form-input>
      </b-form>
    </b-modal>

    <button v-b-modal.inviteModal
            class="btn btn-success btn-sm"
            title="Inviter des personnes">
      <icon name="user"></icon>
    </button>
  </span>

</template>

<script>
  import Board from '../api/board'
  import message from '../services/message'

  export default {
    name: 'InviteModal',
    data () {
      return {
        emails: '',
        error: false
      }
    },
    props: ['board', 'fetchData'],
    methods: {
      validateEmail: function (emails) {
        var isValid = true

        var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

        emails.forEach(function (value, key) {
          if (!re.test(value)) {
            isValid = false
          }
        })
        return isValid
      },
      clearEmails: function () {
        this.emails = ''
        this.error = false
      },
      handleOk (e) {
        // Prevent modal from closing
        e.preventDefault()
        if (!this.emails) {
          this.error = true
          message.error('Entrez au moins un email')
        } else {
          this.handleSubmit()
        }
      },
      handleSubmit () {
        let emailsList = this.emails.split(',')
        if (this.validateEmail(emailsList)) {
          Board.inviteEmails(this.board.id, emailsList, this.$store.state)
          .then(response => {
            this.fetchData()
            // this.$parent.$options.methods.someParentMethod(data)
            message.success('Invitations envoyées')
            this.clearEmails()
            this.$refs.modal.hide()
          })
          .catch(response => {
            message.displayGenericError()
          })
        } else {
          message.error('Email pas bon')
          this.error = true
        }
      }
    }
  }
</script>

<style scoped>

</style>
