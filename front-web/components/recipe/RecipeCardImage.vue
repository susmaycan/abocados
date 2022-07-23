<template>
  <div
    v-if="recipe"
    class="recipe-image-container"
  >
    <recipe-image
      v-bind="$attrs"
      :src="recipe.picture"
    />
    <recipe-favourite
      v-if="!isCreator(recipe) && showFavourite"
      :id="recipe.id"
      class="recipe-favourite-button"
      :favourite="recipe.favourited"
      @refresh="toggleFavourite"
    />
  </div>
</template>

<script>
import mixin from '@/utils/mixins/global'

export default {
  name: 'RecipeCardImage',
  mixins: [mixin],
  props: {
    recipe: {
      type: Object,
      default: () => {}
    },
    showFavourite: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    toggleFavourite (value) {
      this.$emit('toggle-favourite', value)
    }
  }
}
</script>

<style scoped>
.recipe-favourite-button {
  position: absolute;
  top: 5%;
  left: 95%;
  transform: translate(-95%, -5%);
  -ms-transform: translate(-95%, -5%);
}
.recipe-image-container {
  position: relative;
}
</style>
