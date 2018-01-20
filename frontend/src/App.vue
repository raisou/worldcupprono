<template>
  <div>
    <div class="app" v-if="authenticated">
      <navbar />
      <message />
      <confirmationModal />

      <div class="app-body">
        <boardlist />
        <main class="main">
          <breadcrumb :list="list" />
          <div class="container-fluid">
            <router-view></router-view>
          </div>
        </main>
      </div>
    </div>
    <div v-else>
      <message />
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import Message from '@/components/Message.vue'
  import Boardlist from '@/components/Boardlist.vue'
  import Breadcrumb from '@/components/Breadcrumb.vue'
  import ConfirmationModal from '@/components/ConfirmationModal.vue'
  import {mapState} from 'vuex'

  export default {
    name: 'app',
    components: { Navbar, Boardlist, Message, Breadcrumb, ConfirmationModal },
    computed: {
      list () {
        return this.$route.matched
      },
      ...mapState([
        'authenticated'
      ])
    },
    created () {
      this.$store.dispatch('cleanMessage')
      this.$store.dispatch('refreshToken')
    }
  }
</script>

<style lang="scss">
  // Import Main styles for this application
  @import './scss/style';

  .flag-icon {
    border-radius: 15px;
    font-size: 28px;
  }

  .fa-icon {
    vertical-align: middle;
    width: 14px;
  }

  .btn .fa-icon {
    margin-right: 0.5rem;

    &:last-child {
      margin-right: 0;
    }
  }
</style>
