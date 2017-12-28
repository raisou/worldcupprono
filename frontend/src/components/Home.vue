<template>
  <b-container>
    <b-form-group horizontal
                  :label-cols="4"
                  description="Let us know your name."
                  label="Enter your name"
    >
       <b-form-input v-model.trim="name"></b-form-input>
    </b-form-group>

    <b-alert variant="success" :show="showAlert">
      Hello {{ name }}
    </b-alert>
  </b-container>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      name: 'Hellomoto'
    }
  },
  computed: {
    showAlert () {
      return this.name.length > 4
    }
  }
}
</script>

<style scoped>
</style>
