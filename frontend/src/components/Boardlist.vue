<template>
  <div class="sidebar">
    <div id="title" class="text-muted">
      Tableaux
    </div>
    <b-list-group>
      <b-list-group-item href="#some-link">Awesome link</b-list-group-item>
      <b-list-group-item href="#" active>Link with active state</b-list-group-item>
      <b-list-group-item href="#">Action links are easy</b-list-group-item>
      <b-list-group-item>
        <b-form-input v-model="newBoard"
          type="text"
          placeholder="Enter your name"></b-form-input>
        <p>Value: {{ newBoard }}</p>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  name: 'Boardlist',
  data () {
    return {
      newBoard: ''
    }
  }
}
</script>

<style scoped>
  .sidebar {
    padding: 15px;
    background-color: rgba(0,0,0,.03);
    border: 1px solid rgba(0,0,0,.125);
  }
  .sidebar #title {
    margin-bottom: 15px;
  }
  .sidebar .list-group-item {
    border: none;
  }
</style>
