<template>
  <div class="sidebar">
    <nav class="sidebar-nav">
      <ul class="nav">
        <li class="nav-title">
          Tableaux
        </li>
        <li class="nav-item"
            v-for="board in boards"
            :key="board.id">
          <router-link class="nav-link"
                       :to="{ name: 'board', params: { boardId: board.id } }">
            <span v-if="board.is_owner">+</span>
            {{ board.name }}
          </router-link>
        </li>
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
      }
    },
    beforeMount () {
      this.$store.dispatch('getBoards')
    }
  }
</script>
