<template>
  <div id="app">
    <navbar v-if="authenticated" />
    <message />

    <b-container fluid>
      <b-row>
        <b-col cols="3" v-if="authenticated">
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
  import {mapState} from 'vuex'

  export default {
    name: 'app',
    components: { Navbar, Boardlist, Message },
    computed: mapState([
      'authenticated'
    ]),
    created () {
      this.$store.dispatch('cleanMessage')
      this.$store.dispatch('refreshToken')
    }
  }
</script>

<style>
.flag-icon {
  border-radius: 15px;
  font-size: 30px;
}
</style>
