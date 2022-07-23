<template>
  <a-image
    class="recipe-image"
    v-bind="$attrs"
    :src="source"
  />
</template>

<script>
export default {
  name: 'RecipeImage',
  props: {
    src: {
      type: String,
      required: false,
      default: null
    }
  },
  computed: {
    source () {
      return this.src || `${this.$config.s3}/recipes/no_photo`
    }
  }
}
</script>

<style scoped>
.recipe-image {
  border-radius: 10px;
}
</style>
