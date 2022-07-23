<template>
  <page-layout :back="false">
    <template #title>
      <div v-if="!$device.isDesktop">
        <app-logo width="50" height="50" />
        <a-title>
          {{ $t("app_name") }}
        </a-title>
      </div>
      <div v-else>
        <a-title>
          {{ $t("explore") | capitalize }}
        </a-title>
      </div>
    </template>
    <recipe-list-short-layout
      class="mt-5 mb-3"
      :title="$t('explore_latest_recipes') | capitalize"
      :recipes="recipes"
      :empty-message="$t('home_recipe_list_empty') | capitalize"
      @all="$router.push({ name: 'search' })"
    />
    <category-list-short-layout
      class="mt-5 mb-3"
      :title="$t('explore_categories') | capitalize"
      :categories="categories"
    />
  </page-layout>
</template>
<script>
export default {
  name: 'LoggedHome',
  props: {
    recipes: {
      type: Array,
      default: () => []
    },
    categories: {
      type: Array,
      default: () => []
    }
  }
}
</script>
