<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-magnifying-glass" />
        {{ $t("explore_recipes") | capitalize }}
      </a-title>
    </template>
    <template #filters>
      <search-filters
        :init-filters="filters"
        @filter="filter"
      />
    </template>
    <recipe-list-layout
      :recipes="recipes"
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
import RouteMixin from '@/utils/mixins/route'

export default {
  name: 'Search',
  mixins: [RouteMixin],
  middleware: ['auth-custom'],
  data () {
    return {
      recipes: null,
      previous: null,
      next: null,
      filters: {}
    }
  },
  mounted () {
    this.setFilters()
    this.getData(this.filters)
  },
  methods: {
    getData: debounce(async function (queryParams) {
      const data = await this.$api.recipe.list(queryParams)
      this.recipes = data.results
      this.previous = data.previous
      this.next = data.next
    }, 750),
    search (pageFilter) {
      this.getData({
        ...this.filters,
        page: pageFilter
      })
    },
    filter (queryParams) {
      this.applyFilters(queryParams)
      this.getData(queryParams)
    },
    toggleFavourite (recipeId, value) {
      const findRecipe = this.recipes.find(recipe => recipeId === recipe.id)
      if (findRecipe !== -1) {
        findRecipe.favourited = value
      }
    }
  }
}
</script>
