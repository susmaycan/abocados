<template>
  <div class="recipe-card">
    <recipe-image width="120" height="120" :src="recipe.picture" />
    <div class="mx-2">
      <h3 class="recipe-card-title">
        {{ recipe.name }}
      </h3>
      <div class="d-flex align-stretch justify-start">
        <span
          v-if="recipe.duration"
          class="mr-2"
        ><a-icon name="fa-solid fa-clock" /> {{ recipe.duration }}
          {{ $t("min") }}</span>
        <recipe-rating :rating="recipe.rating" />
      </div>
    </div>
  </div>
</template>

<script>
import mixin from '@/mixins/global'

export default {
  name: 'RecipeCard',
  mixins: [mixin],
  props: {
    recipe: {
      type: Object,
      required: true
    },
    showFavourite: {
      type: Boolean,
      default: true
    },
    showSelect: {
      type: Boolean,
      default: false
    },
    selected: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    rating () {
      return parseInt(this.recipe.rating)
    }
  }
}
</script>

<style scoped>
.recipe-card {
  margin: 0.7em 1em;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.recipe-card-title {
  margin: 0.25em 0;
  font-weight: bold;
}
</style>
