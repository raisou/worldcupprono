<template>
  <tr>
    <td>
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_domicile.code | lower"></span>
    </td>
    <td class="text-right">
        {{ match.team_domicile.name }}
    </td>
    <td class="text-center">
      <span v-if="match.prono_id || editing">
        <span class="score"
              @click="edit()"
              v-if="!editing">
          {{ match.prono_domicile }}
        </span>
        <input type="text"
               size="1"
               v-model="match.prono_domicile"
               placeholder="0"
               v-if="editing"
               @keyup.enter="updateProno()" />
        -
        <span class="score"
              @click="edit()"
              v-if="!editing">
          {{ match.prono_visitor }}
        </span>
        <input type="text"
               size="1"
               v-model="match.prono_visitor"
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
  import Prono from '@/api/prono'
  import message from '@/services/message'

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
        if (!this.match.prono_id) {
          Prono.saveProno(
            {
              match: this.match.id,
              score_domicile: this.match.prono_domicile,
              score_visitor: this.match.prono_visitor
            },
            this.$store.state
          )
          .then(response => {
            this.match.prono_id = response.data.id
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
            this.match.prono_id,
            {
              match: this.match.id,
              score_domicile: this.match.prono_domicile,
              score_visitor: this.match.prono_visitor
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
  span.score {
    cursor: pointer;
    color: #20a8d8;
    text-decoration: underline;
    text-underline-position: under;
    text-decoration-style: dotted;
  }
</style>
