<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-bookmark" />
        {{ $t('recipe_book') | capitalize }}
      </a-title>
      <p>{{ $t('recipe_book_subtitle') }}</p>
    </template>
    <template #buttons>
      <a-button
        icon="fa-solid fa-circle-plus"
        color="secondary"
        @click="addRecipe()"
      >
        {{ $t('add_recipe') | capitalize }}
      </a-button>
    </template>
    <template #filters>
      <search-filters :init-filters="filters" @filter="filter" />
    </template>
    <recipe-list-layout
      :recipes="list"
      :empty-message="$t('recipe_list_empty')"
      :next="!!next"
      :previous="!!previous"
      @search="search"
    />
    <a-button
      v-if="$device.isMobile"
      icon="fa-solid fa-circle-plus"
      color="primary"
      fab
      class="add-recipe-mobile"
      @click="addRecipe()"
    />
  </page-layout>
</template>
<script>
import { mapState } from 'vuex'
import ListMixin from '@/mixins/list'

export default {
  name: 'RecipeList',
  mixins: [ListMixin],
  middleware: ['auth-custom'],
  computed: {
    ...mapState('user', ['user']),
  },
  methods: {
    async getData(queryParams) {
      const data = await this.$api.user.sublist(this.user.id, queryParams)
      this.setData(data)
    },
    addRecipe() {
      this.$router.push({ name: 'recipes-add' })
    },
  },
}
</script>
<style scoped>
.add-recipe-mobile {
  position: fixed;
  bottom: 40px;
  right: 20px;
  margin-bottom: 40px;
  border-radius: 50%;
}
</style>
