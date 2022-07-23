<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-bookmark" />
        {{ $t("recipe_book") | capitalize }}
      </a-title>
      <p>{{ $t("recipe_book_subtitle") }}</p>
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
      <search-filters
        :init-filters="filters"
        @filter="filter"
      />
    </template>
    <recipe-list-layout
      :recipes="recipes"
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
import RouteMixin from '@/utils/mixins/route'

export default {
  name: 'RecipeList',
  mixins: [RouteMixin],
  middleware: ['auth-custom'],
  data () {
    return {
      recipes: null,
      previous: null,
      next: null,
      categories: [],
      filters: {}
    }
  },
  computed: {
    ...mapState('user', ['user'])
  },
  mounted () {
    this.setFilters()
    this.getData(this.filters)
  },
  methods: {
    async getData (queryParams) {
      const data = await this.$api.user.sublist(this.user.id, queryParams)
      this.recipes = data.results
      this.previous = data.previous
      this.next = data.next
    },
    addRecipe () {
      this.$router.push({ name: 'recipes-add' })
    },
    search (pageFilter) {
      this.getData({
        ...this.filters,
        page: pageFilter
      })
    },
    filter (queryParams) {
      this.applyFilters(queryParams)
      this.getData(queryParams)
    }
  }
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
