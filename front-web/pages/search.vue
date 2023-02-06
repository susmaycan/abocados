<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-magnifying-glass" />
        {{ $t('explore_recipes') | capitalize }}
      </a-title>
    </template>
    <template #filters>
      <search-filters :init-filters="filters" @filter="filter" />
    </template>
    <recipe-list-layout
      :recipes="list"
      :empty-message="$t('recipe_search_empty')"
      :next="!!next"
      :previous="!!previous"
      @search="search"
      @toggle-favourite="toggleFavourite"
    />
  </page-layout>
</template>
<script>
import { debounce } from 'lodash'
import ListMixin from '@/mixins/list'

export default {
  name: 'Search',
  mixins: [ListMixin],
  middleware: ['auth-custom'],
  methods: {
    getData: debounce(async function (queryParams) {
      const data = await this.$api.recipe.list(queryParams)
      this.setData(data)
    }, 750),
    toggleFavourite(recipeId, value) {
      const findRecipe = this.recipes.find((recipe) => recipeId === recipe.id)
      if (findRecipe !== -1) {
        findRecipe.favourited = value
      }
    },
  },
}
</script>
