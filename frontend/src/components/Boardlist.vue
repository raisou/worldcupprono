<template>
  <div class="sidebar">
    <nav class="sidebar-nav">
      <ul class="nav">
        <li class="nav-title">
          Tableaux
        </li>
        <board v-for="board in boards"
               :key="board.id"
               :board="board">
        </board>
        <div class="sidebar-form">
          <div class="form-group">
          <input type="text"
                 class="form-control"
                 placeholder="Créer un tableau"
                 v-model="newBoard"
                 @keyup.enter="createBoard" />
          </div>
        </div>
      </ul>
    </nav>
  </div>
</template>

<script>
  import Board from '@/components/Board.vue'
  import {mapState} from 'vuex'

  export default {
    name: 'BoardList',
    data () {
      return {
        newBoard: ''
      }
    },
    components: { Board },
    computed: mapState([
      'boards'
    ]),
    methods: {
      createBoard: function () {
        this.$store.dispatch('saveBoard', this.newBoard)
        this.newBoard = ''
      }
    },
    beforeMount () {
      this.$store.dispatch('getBoards')
    }
  }
</script>

<style lang="scss">
  .sidebar .nav-link:hover {
    background-color: inherit;
    background-image: linear-gradient(right, transparent, transparent 70%, black 95%, transparent 100%);
    background-image: -webkit-linear-gradient(right, transparent, transparent 70%, black 95%, transparent 100%);
  }
</style>
