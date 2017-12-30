<template>
  <b-alert :show="dismissCountDown"
           dismissible
           :variant="message.status"
           @dismissed="dismissCountdown=0"
           @dismiss-count-down="countDownChanged">
    {{ message.text }}
  </b-alert>
</template>

<script>
  import {mapState} from 'vuex'

  export default {
    data () {
      return {
        dismissSecs: 5,
        dismissCountDown: 0
      }
    },
    computed: mapState([
      'message'
    ]),
    methods: {
      countDownChanged (dismissCountDown) {
        this.dismissCountDown = dismissCountDown
      },
      showAlert () {
        this.dismissCountDown = this.dismissSecs
      }
    },
    watch: {
      'message.text': {
        handler: function (val) {
          // we dont want trigger on cleanMessage
          if (val !== '') {
            this.showAlert()
          }
        },
        deep: true
      }
    }
  }
</script>

<style scoped>
  div.alert {
    position: fixed;
    top: 20px;
    left: 10%;
    width: 80%;
    z-index: 5000;
  }
</style>
