<template>
  <b-list-group-item>
    <div class="d-flex">
      <div class="p-2">
        Invitation de <b>{{ invitation.destination }}</b> au tableau <b>{{ invitation.board }}</b> le {{ invitation.created }}
      </div>
      <div class="ml-auto p-2" v-if="invitation.is_source">
        <b-button variant="default"
                  title="Renvoyer le mail d'invitation"
                  @click="resend">
          <icon name="envelope"></icon>
        </b-button>
        <b-button variant="default"
                  title="Annuler"
                  @click="cancel">
          <icon name="times"></icon>
        </b-button>
      </div>
      <div class="ml-auto p-2" v-else>
        <b-button variant="success"
                  title="Accepter"
                  @click="accept">
          <icon name="check"></icon>
        </b-button>
        <b-button variant="danger"
                  title="Refuser"
                  @click="decline">
          <icon name="times"></icon>
        </b-button>
      </div>
    </div>
  </b-list-group-item>
</template>

<script>
  export default {
    name: 'invitation',
    props: ['invitation'],
    methods: {
      accept: function () {
        this.$store.dispatch('acceptInvitation', this.invitation)
      },
      decline: function () {
        this.$store.dispatch('declineInvitation', this.invitation)
      },
      cancel: function () {
        this.$store.dispatch('cancelInvitation', this.invitation)
      },
      resend: function () {
        this.$store.dispatch('resendInvitation', this.invitation)
      }
    }
  }
</script>
