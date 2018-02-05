<template>
  <div class="card" >
    <div class="card-body">
      <div class="text-right">
        <invite-modal :board='board' :fetchData='fetchData'></invite-modal>
        <button class="btn btn-danger btn-sm"
                title="Quitter le tableau"
                v-if="!board.is_owner"
                @click="leaveBoard">
          <icon name="sign-out"></icon>
        </button>
        <button class="btn btn-danger btn-sm"
                title="Supprimer le tableau"
                v-if="board.is_owner"
                @click="deleteBoard">
          <icon name="trash-o"></icon>
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
              <b-form-input v-model="filter" placeholder="Chercher" />
              <b-input-group-button>
                <b-btn :disabled="!filter" @click="filter = ''">Effacer</b-btn>
              </b-input-group-button>
            </b-input-group>
          </b-form-group>
        </template>
      </b-table>
    </div>
  </div>
</template>


<script>
  import Board from '@/api/board'
  import message from '@/services/message'
  import InviteModal from '@/components/InviteModal'
  import confirmationmodal from '@/services/confirmationmodal.js'

  export default {
    name: 'board',
    data () {
      return {
        sortBy: 'points',
        sortDesc: false,
        filter: null,
        board: {
          users: []
        },
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
      InviteModal
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
        Board.get(this.$route.params.boardId)
        .then(response => {
          this.board = response.data
        })
        .catch(response => {
          message.displayGenericError()
        })
      },
      leaveBoard () {
        confirmationmodal.leaveBoard(this.board)
      },
      deleteBoard () {
        confirmationmodal.deleteBoard(this.board)
      }
    }
  }
</script>

<style scoped>
  fieldset#mails {
    padding-bottom: 30px;
  }
</style>
