<template>
  <b-col cols="6">
    <div class="card">
      <div class="card-header">
        Groupe {{ name }}
      </div>
      <div class="card-body">
        <match v-for="match in filterMatchByGroup(matchs)"
               :key="match.id"
               :match="match">
        </match>
      </div>
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
