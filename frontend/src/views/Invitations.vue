<template>
  <b-row>
    <b-col cols="12" md="6">
      <div class="card">
        <div class="card-header">
          Invitations envoyées en attente
        </div>
        <b-list-group>
          <invitation v-for="invitation in filterSource(invitations, true)"
                      :key="invitation.id"
                      :invitation="invitation">
          </invitation>
        </b-list-group>
      </div>
    </b-col>
    <b-col cols="12" md="6">
      <div class="card">
        <div class="card-header">
          Invitations reçues en attente
        </div>
        <b-list-group>
          <invitation v-for="invitation in filterSource(invitations, false)"
                      :key="invitation.id"
                      :invitation="invitation">
          </invitation>
        </b-list-group>
      </div>
    </b-col>
  </b-row>
</template>


<script>
  import Invitation from '@/components/Invitation.vue'
  import {mapState} from 'vuex'

  export default {
    name: 'invitations',
    components: { Invitation },
    computed: mapState([
      'invitations'
    ]),
    methods: {
      filterSource: function (invitations, isSource) {
        return this.invitations.filter(invitation => {
          return invitation.is_source === isSource
        })
      }
    },
    beforeMount () {
      if (this.$store.state.invitations.length === 0) {
        this.$store.dispatch('getInvitations')
      }
    }
  }
</script>
