<template>
  <b-navbar toggleable="md" type="dark" variant="dark">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#">Worldcuppronos</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#">Mes pronos</b-nav-item>
        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>Prénom Nom</em>
          </template>
          <b-dropdown-item href="#">Mon compte</b-dropdown-item>
          <b-dropdown-item href="#">Déconnection</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
  nav {
    margin-bottom: 15px;
  }
</style>
