<template>
  <li class="nav-item">
    <router-link class="nav-link"
                 @mouseover.native="hover = true"
                 @mouseleave.native="hover = false"
                 :to="{ name: 'board', params: { boardId: board.id } }">
      <span v-if="board.is_owner" title="Vous êtes le créateur de ce tableau">
        <icon class="owner" name="certificate"></icon>
      </span>
      {{ board.name }}
      <div class="board-icons float-right">
        <icon class="edit"
              name="edit"
              v-if="board.is_owner"
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
  import confirmationmodal from '@/services/confirmationmodal.js'

  export default {
    name: 'Board',
    data () {
      return {
        hover: false
      }
    },
    props: ['board'],
    methods: {
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
