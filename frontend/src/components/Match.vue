<template>
  <b-list-group-item>
    <b-row align-h="center">
      <b-col cols="6" md="5" class="match-teams">
        <div>
          <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_domicile.code | lower"></span>
            {{ match.team_domicile.name }}
        </div>
        <div class="pt-2">
          <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_visitor.code | lower"></span>
          {{ match.team_visitor.name }}
        </div>
      </b-col>
      <b-col class="text-center" cols="6" md="5">
        <div class="text-muted">
          Le {{ match.date }}
        </div>
        <div v-if="match.is_played">
          Score final: {{ match.score_domicile }} - {{ match.score_visitor }}
        </div>
        <div :class="'text-center mt-2'" v-if="match.prono_id || editing">
          <span :class="{ score: !match.is_locked }"
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
          <span :class="{ score: !match.is_locked }"
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
        </div>
        <div :class="'text-center mt-2'" v-else>
          <button class="btn btn-default btn-sm"
                  @click="edit()">
            Pronostiquer
          </button>
        </div>
      </b-col>
    </b-row>
  </b-list-group-item>
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
        if (!this.match.is_locked) {
          this.editing = true
        }
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
  div.list-group {
    display: block;
  }

  div.score {
    display: inline-block;
  }

  span.score {
    cursor: pointer;
    color: #20a8d8;
    text-decoration: underline;
    text-underline-position: under;
    text-decoration-style: dotted;
  }

  .match-teams {
    border-right: 1px solid #333;
  }
</style>
