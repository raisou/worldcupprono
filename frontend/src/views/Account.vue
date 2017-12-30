<template>
  <div class="card">
    <div class="card-header">
      Mon compte
    </div>
    <div class="card-body">
      <h5 class="card-title">Username: {{ me.username }}</h5>
      <h5 class="card-title">Email: {{ me.email }}</h5>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'account',
  computed: mapState([
    'me'
  ])
}
</script>

<style scoped>
</style>
