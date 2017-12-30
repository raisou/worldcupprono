<template>
  <div id="app">
    <navbar v-if="isAuthenticated()" />
    <message />

    <b-container fluid>
      <b-row>
        <b-col cols="3" v-if="isAuthenticated()">
          <boardlist />
        </b-col>
        <b-col>
          <router-view />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Message from './components/Message.vue'
  import Boardlist from './components/Boardlist.vue'

  export default {
    name: 'app',
    components: { Navbar, Boardlist, Message },
    methods: {
      isAuthenticated () {
        return true
      }
    }
  }
</script>

<style>
</style>
