<template>
  <div>
    <pacman-loader :loading="loading"></pacman-loader>
    <div class="card" v-if="!loading">
      <div class="card-header">
        Tableau {{ board.name }}
      </div>
      <div class="card-body">
        <table class="table table-hover">
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in board.users" :key="user.id">
              <td>
                {{ user.username }}
              </td>
              <td>
                {{ user.email }}
              </td>
              <td>
                {{ user.points }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script>
  import Board from '../api/board'
  import message from '../services/message'
  import PacmanLoader from 'vue-spinner/src/PacmanLoader.vue'

  export default {
    name: 'board',
    data () {
      return {
        loading: false,
        board: null
      }
    },
    components: {
      PacmanLoader
    },
    created () {
      // fetch the data when the view is created and the data is
      // already being observed
      this.fetchData()
    },
    watch: {
      // call again the method if the route changes
      '$route': 'fetchData'
    },
    methods: {
      fetchData () {
        this.board = null
        this.loading = true
        Board.get(this.$route.params.boardId, this.$store.state)
        .then(response => {
          this.loading = false
          this.board = response.data
        })
        .catch(response => {
          message.displayGenericError()
        })
      }
    }
  }
</script>

<style scoped>
</style>
