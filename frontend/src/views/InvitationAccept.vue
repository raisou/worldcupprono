<template>
</template>

<script>
  import Invitation from '@/api/invitation'
  import message from '@/services/message'

  export default {
    created () {
      Invitation.acceptToken(this.$route.params.token, this.$store.state)
      .then(() => {
        message.success('Invitation acceptée')
        const boardId = this.$route.params.boardId
        this.$store.dispatch('getBoards')
        this.$router.push({name: 'board', params: { boardId }})
      })
      .catch(() => {
        message.displayGenericError()
        this.$router.push({name: 'home'})
      })
    }
  }
</script>
