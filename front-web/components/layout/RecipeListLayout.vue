<template>
  <div>
    <div v-if="recipes && recipes.length === 0">
      <p>{{ emptyMessage || $t('recipe_list_empty') }}</p>
    </div>
    <grid v-else>
      <div v-for="recipe in recipes" :key="recipe.id">
        <recipe-card :recipe="recipe" @refresh="toggleFavourite(recipe.id, $event)" />
      </div>
    </grid>
    <div v-if="previous || next" class="d-flex justify-space-between align-center my-4">
      <a-button
        :disabled="!previous"
        text
        icon="fa-solid fa-circle-left"
        class="pagination-button"
        @click="onPrevious()"
      />
      <a-button
        :disabled="!next"
        text
        icon="fa-solid fa-circle-right"
        class="pagination-button"
        @click="onNext()"
      />
    </div>
  </div>
</template>
<script>
export default {
  name: 'RecipeListLayout',
  props: {
    recipes: {
      type: Array,
      default () { return [] }
    },
    emptyMessage: {
      type: String,
      default: null
    },
    previous: {
      type: Boolean,
      default: false
    },
    next: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      actualPage: 1
    }
  },
  methods: {
    toggleFavourite (recipeId, value) {
      this.$emit('toggle-favourite', recipeId, value)
    },
    onNext () {
      this.actualPage = this.actualPage + 1
      this.$emit('search', this.actualPage)
    },
    onPrevious () {
      this.actualPage = this.actualPage - 1
      this.$emit('search', this.actualPage)
    }
  }
}
</script>
<style scoped>
  .pagination-button {
    font-size: 40px;
  }
</style>
