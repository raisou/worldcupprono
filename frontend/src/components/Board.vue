<template>
  <li class="nav-item">
    <router-link class="nav-link"
                 @mouseover.native="hover = true"
                 @mouseleave.native="hover = false"
                 :to="{ name: 'board', params: { boardId: board.id } }">
      <span v-if="board.is_owner">
        <icon name="star-o"></icon>
      </span>
      {{ board.name }}
      <div class="board-icons float-right">
        <icon class="edit" v-if="board.is_owner" v-show="hover" name="edit"></icon>
        <icon class="delete" v-if="board.is_owner" v-show="hover" name="trash-o"></icon>
        <icon class="leave" v-if="!board.is_owner" v-show="hover" name="sign-out"></icon>
      </div>
    </router-link>
  </li>
</template>

<script>
  export default {
    name: 'Board',
    props: ['board'],
    data () {
      return {
        hover: false
      }
    }
  }
</script>

<style lang="scss" scoped>

  .fa-icon {
    margin-right: 2px;
    vertical-align: middle;
  }

  .board-icons .fa-icon {
    margin-right: 10px;
    vertical-align: middle;
  }

</style>
