<template>
  <div class="card">
    <div class="card-header">
      Mon compte
    </div>
    <div class="card-body">
      <div class="float-right">
        <v-gravatar :email="me.email" default-img="mm" />
      </div>
      <h5 class="card-title">Username: {{ me.username }}</h5>
      <h5 class="card-title">Email: {{ me.email }}</h5>
      <h5 class="card-title">Points: 0</h5>
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
