<template>
  <page-layout :back="true">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-heart" />
        {{ $t('favourites') | capitalize }}
      </a-title>
      <p>{{ $t('favourites_subtitle') | capitalize }}</p>
    </template>
    <recipe-list-layout
      :recipes="list"
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
import ListMixin from '@/mixins/list'
export default {
  name: 'FavouriteList',
  middleware: ['auth-custom'],
  mixins: [ListMixin],
  computed: {
    ...mapState('user', ['user']),
  },
  methods: {
    async getData(queryParams) {
      const data = await this.$api.favourite.list(this.user.id, queryParams)
      this.setData(data)
    },
    toggleFavourite(recipeId, value) {
      const recipeIndex = this.recipes.findIndex(
        (recipe) => recipeId === recipe.id
      )
      if (recipeIndex !== -1) {
        this.recipes.splice(recipeIndex, 1)
      }
    },
  },
}
</script>
