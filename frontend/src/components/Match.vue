<template>
  <tr>
    <td>
      <span class="flag-icon flag-icon-squared" :class="'flag-icon-' + match.team_domicile.code | lower"></span>
    </td>
    <td class="text-right">
        {{ match.team_domicile.name }}
    </td>
    <td class="text-center">
      {{ match.score_domicile | default_if_null(0) }}
      -
      {{ match.score_visitor | default_if_null(0) }}
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
  export default {
    name: 'match',
    props: ['match']
  }
</script>

<style scoped>

</style>
