<template>
  <a-button
    v-if="selected"
    fab
    v-bind="$attrs"
    icon="fa-regular fa-square-check"
    @click="unselectRecipe"
  />
  <a-button
    v-else
    fab
    v-bind="$attrs"
    icon="fa-regular fa-square"
    @click="selectRecipe"
  />
</template>

<script>
export default {
  name: 'RecipeCardSelect',
  props: {
    selected: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    selectRecipe () {
      this.$emit('select', true)
    },
    unselectRecipe () {
      this.$emit('select', false)
    }
  }

}
</script>
