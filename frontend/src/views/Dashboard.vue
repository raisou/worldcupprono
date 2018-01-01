<template>
  <div class="card">
    <div class="card-header">
      Dashboard
    </div>
    <div class="card-body">
      <b-row>
        <group v-for="(group, index) in groups"
               :key="`group-${index}`"
               :name="group"></group>
      </b-row>
    </div>
  </div>
</template>


<script>
  import Group from '../components/Group.vue'

  export default {
    name: 'dashboard',
    data () {
      return {
        groups: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
      }
    },
    components: { Group },
    beforeMount () {
      if (this.$store.state.matchs.length === 0) {
        this.$store.dispatch('getMatchs')
      }
    }
  }
</script>

<style scoped>

</style>
