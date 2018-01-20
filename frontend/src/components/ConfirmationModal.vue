<template>
  <b-modal ref="confirmationModal"
           :title="modal.title"
           :header-bg-variant="modal.variant"
           @ok="handleOk">
    <p class="my-4 text-center">
      {{ modal.text }}
    </p>
  </b-modal>
</template>

<script>
  import {mapState} from 'vuex'

  export default {
    name: 'ConfirmationModal',
    computed: mapState([
      'modal'
    ]),
    methods: {
      handleOk () {
        this.$store.dispatch(this.modal.action, this.modal.obj)
      }
    },
    watch: {
      'modal.text': {
        handler: function (val) {
          // we dont want trigger on clean
          if (val !== '') {
            this.$refs.confirmationModal.show()
          }
        },
        deep: true
      }
    }
  }
</script>
