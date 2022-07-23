<template>
  <page-layout :back="true">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-heart" />
        {{ $t("favourites") | capitalize }}
      </a-title>
      <p>{{ $t('favourites_subtitle') | capitalize }}</p>
    </template>
    <recipe-list-layout
      :recipes="recipes"
      :empty-message="$t('favourites_empty_message')"
      :next="!!next"
      :previous="!!previous"
      @search="search"
      @toggle-favourite="toggleFavourite"
    />
  </page-layout>
</template>
<script>
import { mapState } from 'vuex'
export default {
  name: 'FavouriteList',
  middleware: ['auth-custom'],
  data () {
    return {
      recipes: null,
      previous: null,
      next: null
    }
  },
  computed: {
    ...mapState('user', ['user'])
  },
  mounted () {
    this.getData()
  },
  methods: {
    async getData (queryParams) {
      const data = await this.$api.favourite.list(this.user.id, queryParams)
      this.recipes = data.results
      this.previous = data.previous
      this.next = data.next
    },
    search (pageFilter) {
      this.getData({ page: pageFilter })
    },
    toggleFavourite (recipeId, value) {
      const recipeIndex = this.recipes.findIndex(recipe => recipeId === recipe.id)
      if (recipeIndex !== -1) {
        this.recipes.splice(recipeIndex, 1)
      }
    }
  }
}
</script>
