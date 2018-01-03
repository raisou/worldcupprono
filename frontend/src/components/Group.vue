<template>
  <b-col cols="12" xl="6">
    <div class="card">
      <div class="card-header">
        Groupe {{ name }}
      </div>
      <table class="table table-hover">
        <tbody>
          <match v-for="match in filterMatchByGroup(matchs)"
                 :key="match.id"
                 :match="match">
          </match>
        </tbody>
      </table>
    </div>
  </b-col>
</template>


<script>
  import Match from '../components/Match.vue'
  import {mapState} from 'vuex'

  export default {
    name: 'group',
    props: ['name'],
    components: { Match },
    computed: mapState([
      'matchs'
    ]),
    methods: {
      filterMatchByGroup: function (matchs) {
        return this.$_.filter(matchs, { 'stage': this.name })
      }
    }
  }
</script>

<style scoped>
  div.card {
    margin-bottom: 15px;
  }
</style>
