<template>
  <b-navbar toggleable="md" type="dark" variant="dark">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#">Worldcuppronos</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#dashboard">Mes pronos</b-nav-item>
        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>{{ me.username }}</em>
          </template>
          <b-dropdown-item @click="redirectAccount()">Mon compte</b-dropdown-item>
          <b-dropdown-item @click="logout()">Déconnection</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'Navbar',
  computed: mapState([
    'me',
    'authenticated'
  ]),
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
      this.$router.push('login')
    },
    redirectAccount: function () {
      this.$router.push('account')
    }
  },
  beforeMount () {
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style scoped>
  nav {
    margin-bottom: 15px;
  }
</style>
