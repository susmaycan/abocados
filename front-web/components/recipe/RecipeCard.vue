<template>
  <div
    class="recipe-card clickable"
    @click="goToDetail()"
  >
    <recipe-card-image
      :recipe="recipe"
      :show-favourite="showFavourite"
      @toggle-favourite="toggleFavourite"
    />
    <div class="mx-2">
      <h3 class="recipe-card-title">
        {{ recipe.name }}
      </h3>
      <div
        class="d-flex align-stretch justify-center"
      >
        <span v-if="recipe.duration" class="mr-2"><a-icon name="fa-solid fa-clock" /> {{ recipe.duration }} {{ $t('min') }}</span>
        <a-rating :rating="recipe.rating" />
      </div>
    </div>
  </div>
</template>

<script>
import mixin from '@/utils/mixins/global'

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
    }
  },
  computed: {
    rating () {
      return parseInt(this.recipe.rating)
    }
  },
  methods: {
    goToDetail () {
      this.$router.push({ name: 'recipes-id', params: { id: this.recipe.id } })
    },
    toggleFavourite (value) {
      this.$emit('refresh', value)
    }
  }
}
</script>

<style scoped>
.recipe-card {
  margin: .7em 1em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.recipe-card:hover {
  opacity: 0.6;
}
.recipe-card-title {
  margin: .25em 0;
  font-weight: bold;
}
</style>
