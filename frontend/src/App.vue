<template>
  <div id="app">
    <navbar/>

    <b-container fluid>
      <b-row>
        <b-col cols="3">
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
import Boardlist from './components/Boardlist.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: { Navbar, Boardlist }
}
</script>

<style>
</style>
