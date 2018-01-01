<template>
  <b-row>
    <b-col>
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_domicile.code | lower"></span>
      {{ match.team_domicile.name }}
      {{ match.score_domicile | default_if_null(0) }}
      -
      {{ match.score_visitor | default_if_null(0) }}
      {{ match.team_visitor.name }}
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_visitor.code | lower"></span>
    </b-col>
  </b-row>
</template>

<script>
  export default {
    name: 'match',
    props: ['match']
  }
</script>

<style scoped>

</style>
