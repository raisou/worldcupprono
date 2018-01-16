<template>
  <header class="app-header navbar">
    <button class="navbar-toggler mobile-sidebar-toggler d-lg-none" type="button" @click.prevent="mobileSidebarToggle">
      <span class="navbar-toggler-icon"></span>
    </button>
    <b-link class="navbar-brand" to="#"></b-link>
    <button class="navbar-toggler sidebar-toggler d-md-down-none mr-auto" type="button" @click.prevent="sidebarToggle">
      <span class="navbar-toggler-icon"></span>
    </button>
    <b-navbar-nav class="ml-auto">
      <b-nav-item class="px-3" @click="redirect('dashboard')">
        Mes pronos
      </b-nav-item>
      <b-nav-item-dropdown right no-caret>
        <template slot="button-content" v-if="me.email">
          <v-gravatar class="img-avatar" :email="me.email" default-img="mm" />
        </template>
        <b-dropdown-item @click="redirect('account')">
          <icon name="user"></icon> Mon compte
        </b-dropdown-item>
        <b-dropdown-item @click="logout()">
          <icon name="lock"></icon> Déconnexion
        </b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </header>
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
    sidebarToggle () {
      document.body.classList.toggle('sidebar-hidden')
    },
    mobileSidebarToggle () {
      document.body.classList.toggle('sidebar-mobile-show')
    },
    logout: function () {
      this.$store.dispatch('logout')
      this.$router.push('login')
    },
    redirect: function (redirectName) {
      this.$router.push({ name: redirectName })
    }
  },
  beforeMount () {
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style lang="scss" scoped>
  .app-header.navbar .navbar-brand {
    background-image: none;
  }

  .dropdown-item {
    * {
      vertical-align: middle;
    }

    svg {
      display: inline-block;
      width: 20px;
      height: 14px;
      margin-right: 10px;
      margin-left: -10px;
      color: #c2cfd6;
      text-align: center;
    }
  }
</style>
