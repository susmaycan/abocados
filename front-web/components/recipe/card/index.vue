<template>
  <div class="recipe-card clickable" @click="!showSelect ? goToDetail() : null">
    <recipe-card-image
      :recipe="recipe"
      :show-favourite="showFavourite"
      :show-select="showSelect"
      :selected="selected"
      @toggle-favourite="toggleFavourite"
      @select="select"
    />
    <div class="mx-2">
      <h3 class="recipe-card-title">
        {{ recipe.name }}
      </h3>
      <div class="d-flex align-stretch justify-center">
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
  },
  methods: {
    goToDetail () {
      this.$router.push({ name: 'recipes-id', params: { id: this.recipe.id } })
    },
    toggleFavourite (value) {
      this.$emit('refresh', value)
    },
    select (value) {
      this.$emit('select', value)
    }
  }
}
</script>

<style scoped>
.recipe-card {
  margin: 0.7em 1em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.recipe-card:hover {
  opacity: 0.6;
}
.recipe-card-title {
  margin: 0.25em 0;
  font-weight: bold;
}
</style>
