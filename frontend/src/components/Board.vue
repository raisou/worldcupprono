<template>
  <li class="nav-item">
    <router-link class="nav-link"
                 @mouseover.native="hover = true"
                 @mouseleave.native="hover = false"
                 :to="{ name: 'board', params: { boardId: board.id } }">
      <span v-if="board.is_owner" title="Vous êtes le créateur de ce tableau">
        <icon class="owner" name="certificate"></icon>
      </span>
      <span v-if="!editing">
        {{ board.name }}
      </span>
      <input type="text"
             class="form-control"
             v-model="board.name"
             v-if="board.is_owner && editing"
             @click.prevent=""
             @keyup.enter="updateName()" />
      <div class="board-icons float-right">
        <icon class="edit"
              name="edit"
              @click.native.prevent="editBoard"
              v-if="board.is_owner && !editing"
              v-show="hover">
        </icon>
        <icon class="delete"
              name="trash-o"
              @click.native.prevent="deleteBoard"
              v-if="board.is_owner"
              v-show="hover">
        </icon>
        <icon class="leave"
              name="sign-out"
              @click.native.prevent="leaveBoard"
              v-if="!board.is_owner"
              v-show="hover">
        </icon>
      </div>
    </router-link>
  </li>
</template>

<script>
  import Board from '@/api/board.js'
  import message from '@/services/message.js'
  import confirmationmodal from '@/services/confirmationmodal.js'

  export default {
    name: 'Board',
    data () {
      return {
        editing: false,
        hover: false
      }
    },
    props: ['board'],
    methods: {
      editBoard () {
        this.editing = true
      },
      updateName () {
        Board.updateName(
          this.board.id,
          {
            name: this.board.name
          },
          this.$store.state
        )
        .then(() => {
          this.editing = false
        })
        .catch(() => {
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

<style lang="scss" scoped>

  input.form-control {
    width: 60%;
    color: #fff;
    background: #151b1f;
    border: 0;
    display: inline-block;

    &:focus {
      border-color: #8ad4ee;
      -webkit-box-shadow: 0 0 0 0.2rem rgba(32, 168, 216, 0.25);
      box-shadow: 0 0 0 0.2rem rgba(32, 168, 216, 0.25);
    }
  }

  .fa-icon {
    margin-right: 2px;

    &.owner {
      height: 12px;
    }

    &:hover {
      opacity: 0.5;
    }
  }

  .board-icons {
    display: inline-block;

    .fa-icon {
      margin-right: 10px;
    }
  }

</style>
