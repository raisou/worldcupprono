<template>
  <div>
    <pacman-loader :loading="loading"></pacman-loader>
    <div class="card" v-if="!loading">
      <div class="card-header">
        Tableau {{ board.name }}
      </div>
      <div class="card-body">
        <div class="text-right">
          <invite-modal :board='board' :fetchData='fetchData'></invite-modal>
          <button class="btn btn-danger btn-sm">
            Quitter le tableau
          </button>
        </div>

        <b-table striped
                 hover
                 bordered
                 :items="board.users"
                 :fields="fields"
                 caption-top
                 :sort-by.sync="sortBy"
                 :sort-desc.sync="sortDesc"
                 :filter="filter">
          <template slot="table-caption">
            <b-form-group horizontal label="Classement" class="mb-0">
              <b-input-group>
                <b-form-input v-model="filter" placeholder="Type to Search" />
                <b-input-group-button>
                  <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
                </b-input-group-button>
              </b-input-group>
            </b-form-group>
          </template>
        </b-table>
      </div>
    </div>
  </div>
</template>


<script>
  import Board from '../api/board'
  import message from '../services/message'
  import InviteModal from '../components/InviteModal'
  import PacmanLoader from 'vue-spinner/src/PacmanLoader.vue'

  export default {
    name: 'board',
    data () {
      return {
        sortBy: 'points',
        sortDesc: false,
        filter: null,
        loading: false,
        board: null,
        fields: {
          'username': {
            sortable: true
          },
          'points': {
            sortable: true
          }
        }
      }
    },
    components: {
      PacmanLoader, InviteModal
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
      fetchData: function () {
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
  fieldset#mails {
    padding-bottom: 30px;
  }
</style>
