<template>
  <div class="card">
    <div class="card-header text-muted">
      Tableaux
    </div>
    <b-list-group>
      <b-list-group-item v-for="board in boards"
                         :key="board.id"
                         @click="redirect(board)">
        <span v-if="board.is_owner">+</span>
        {{board.name}}
      </b-list-group-item>
      <b-list-group-item>
        <b-form-input
          type="text"
          placeholder="Ajouter un tableau"
          v-model="newBoard"
          @keyup.enter.native="createBoard">
        </b-form-input>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
  import {mapState} from 'vuex'

  export default {
    name: 'BoardList',
    data () {
      return {
        newBoard: ''
      }
    },
    computed: mapState([
      'boards'
    ]),
    methods: {
      createBoard: function () {
        this.$store.dispatch('saveBoard', this.newBoard)
        this.newBoard = ''
      },
      redirect: function (board) {
        this.$router.push({ name: 'board', params: { boardId: board.id } })
      }
    },
    beforeMount () {
      this.$store.dispatch('getBoards')
    }
  }
</script>

<style scoped>
  .card {
    margin-bottom: 15px;
  }
  .list-group-item {
    border: none;
  }
</style>
