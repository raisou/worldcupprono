<template>
  <div id="app">
    <navbar v-if="authenticated" />
    <message />

    <b-container fluid>
      <b-row>
        <b-col cols="12" sm="3" v-if="authenticated">
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
  form.login,
  form.register,
  form.password-reset,
  form.password-reset-confirm
  {
    max-width: 330px;
    padding: 15px;
    margin: 150px auto;
  }
  form.login .form-control,
  form.register .form-control,
  form.password-reset .form-control,
  form.password-reset-confirm .form-control
  {
    position: relative;
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
  }
  form.login .form-control:focus,
  form.register .form-control:focus,
  form.password-reset .form-control:focus,
  form.password-reset-confirm .form-control:focus
  {
    z-index: 2;
  }
  form.login input,
  form.register input,
  form.password-reset input,
  form.password-reset-confirm input
  {
    margin-bottom: 10px;
  }

  button.btn {
    cursor: pointer;
  }
  .flag-icon {
    border-radius: 15px;
    font-size: 28px;
  }
</style>
