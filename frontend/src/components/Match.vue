<template>
  <tr>
    <td>
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_domicile.code | lower"></span>
    </td>
    <td class="text-right">
        {{ match.team_domicile.name }}
    </td>
    <td class="text-center">
      <span v-if="match.prono || editing">
        <span @click="edit()"
              v-if="!editing">
          {{ match.score_domicile | default_if_null(0) }}
        </span>
        <input type="text"
               size="1"
               v-model="match.score_domicile"
               placeholder="0"
               v-if="editing"
               @keyup.enter="updateProno()" />
        -
        <span @click="edit()"
              v-if="!editing">
          {{ match.score_visitor | default_if_null(0) }}
        </span>
        <input type="text"
               size="1"
               v-model="match.score_visitor"
               placeholder="0"
               v-if="editing"
               @keyup.enter="updateProno()" />
      </span>
      <span v-else>
        <button class="btn btn-default btn-sm"
                @click="edit()">
          Pronostiquez
        </button>
      </span>
    </td>
    <td>
      {{ match.team_visitor.name }}
    </td>
    <td class="text-right">
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_visitor.code | lower"></span>
    </td>
  </tr>
</template>

<script>
  import Prono from '../api/prono'
  import message from '../services/message'

  export default {
    name: 'match',
    data () {
      return {
        editing: false
      }
    },
    props: ['match'],
    methods: {
      edit: function (team) {
        this.editing = true
      },
      updateProno: function () {
        if (!this.match.prono) {
          Prono.saveProno(
            {
              match: this.match.id,
              score_domicile: this.match.score_domicile,
              score_visitor: this.match.score_visitor
            },
            this.$store.state
          )
          .then(response => {
            this.match.prono = response.data.id
            this.editing = false
          })
          .catch(err => {
            if (err.response && err.response.status === 400) {
              message.error(err.response.data.non_field_errors[0])
            } else {
              message.displayGenericError()
            }
          })
        } else {
          Prono.updateProno(
            this.match.prono,
            {
              match: this.match.id,
              score_domicile: this.match.score_domicile,
              score_visitor: this.match.score_visitor
            },
            this.$store.state
          )
          .then(response => {
            this.editing = false
          })
          .catch(err => {
            if (err.response && err.response.status === 400) {
              message.error(err.response.data.non_field_errors[0])
            } else {
              message.displayGenericError()
            }
          })
        }
      }
    }
  }
</script>

<style scoped>

</style>
