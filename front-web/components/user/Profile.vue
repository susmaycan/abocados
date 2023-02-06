<template>
  <div>
    <div class="d-flex justify-center flex-column align-center">
      <user-image :src="user.picture" width="150" height="150" />
      <a-title><a-icon name="fa-solid fa-at" />{{ user.username }}</a-title>
      <p v-if="user.name">
        {{ user.name }}
      </p>
      <a-button
        v-if="$device.isDesktop"
        outlined
        class="mb-2"
        icon="fa-solid fa-pen"
        @click="$router.push({ name: 'account-edit' })"
      >
        {{ $t('edit_profile') | capitalize }}
      </a-button>
    </div>
    <div v-if="$device.isMobile">
      <recipe-list-short-layout
        class="my-2"
        :title="$t('my_recipes') | capitalize"
        :recipes="recipes"
        :empty-message="$t('recipe_list_empty') | capitalize"
        @all="$router.push({ name: 'recipes' })"
      />
      <recipe-list-short-layout
        class="my-2"
        :title="$t('favourites') | capitalize"
        :recipes="favourites"
        :empty-message="$t('favourites_empty_message') | capitalize"
        @all="$router.push({ name: 'favourites' })"
      />
    </div>
    <div v-else>
      <a-tabs :items="desktopItems">
        <a-tabs-item key="my_recipes">
          <recipe-list-short-layout
            class="my-2"
            :title="$t('my_recipes') | capitalize"
            :recipes="recipes"
            :empty-message="$t('recipe_list_empty') | capitalize"
            @all="$router.push({ name: 'recipes' })"
          />
        </a-tabs-item>
        <a-tabs-item key="favourites">
          <recipe-list-short-layout
            class="my-2"
            :title="$t('favourites') | capitalize"
            :recipes="favourites"
            :empty-message="$t('favourites_empty_message') | capitalize"
            @all="$router.push({ name: 'favourites' })"
          />
        </a-tabs-item>
      </a-tabs>
    </div>
  </div>
</template>
<script>
export default {
  name: 'UserProfile',
  props: {
    user: {
      type: Object,
      default: null,
    },
    recipes: {
      type: Array,
      default: [],
    },
    favourites: {
      type: Array,
      default: [],
    },
  },
  data() {
    return {
      desktopItems: [this.$t('my_recipes'), this.$t('favourites')],
    }
  },
}
</script>
<style scoped>
.account-settings-button {
  font-size: 1.5em;
}
</style>
