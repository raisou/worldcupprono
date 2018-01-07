<template>
</template>

<script>
  import User from '@/api/user'
  import message from '@/services/message'

  export default {
    created () {
      User.activate({
        uid: this.$route.params.uid,
        token: this.$route.params.token
      })
      .then(() => {
        message.success('Compte activé')
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
</script>
