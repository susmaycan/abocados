<template>
  <div>
    <p v-if="recipeList.length === 0">
      {{ emptyMessage }}
    </p>
    <grid v-else>
      <div v-for="recipe in recipeList" :key="recipe.id">
        <recipe-card-menu :recipe="recipe" />
      </div>
    </grid>
  </div>
</template>

<script>
export default {
  name: 'MealRecipeList',
  props: {
    recipeList: {
      type: Array,
      default () {
        return []
      }
    },
    emptyMessage: {
      type: String,
      default () {
        return null
      }
    }
  }
}
</script>
