<template>
  <b-col cols="12" md="6">
    <div class="card">
      <div class="card-header">
        Groupe {{ name }}
      </div>
      <b-list-group>
        <match v-for="match in filterMatchByGroup(matchs)"
               :key="match.id"
               :match="match">
        </match>
      </b-list-group>
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
        let name = this.name
        return this.matchs.filter(match => {
          return match.stage.match(name)
        })
      }
    }
  }
</script>

<style scoped>
  div.card {
    margin-bottom: 15px;
  }
</style>
