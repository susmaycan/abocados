<template>
  <page-layout :back="false">
    <div class="d-flex justify-end">
      <a-button
        v-if="$device.isMobile"
        class="account-settings-button"
        text
        icon="fa-solid fa-gear"
        @click="$router.push({ name: 'account-settings' })"
      />
    </div>
    <div v-if="user" class="d-flex justify-center flex-column align-center">
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
        {{ $t("edit_profile") | capitalize }}
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
  </page-layout>
</template>
<script>
export default {
  name: "Account",
  middleware: ["auth-custom"],
  data() {
    return {
      user: {},
      recipes: [],
      favourites: [],
      desktopItems: [this.$t("my_recipes"), this.$t("favourites")],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    async getData() {
      this.user = await this.$api.auth.getUser();
      const data = await this.$api.user.sublist(this.user.id, { limit: 4 });
      this.recipes = data.results;
      const favouriteData = await this.$api.favourite.list(this.user.id);
      this.favourites = favouriteData.results;
    },
  },
};
</script>
<style scoped>
.account-settings-button {
  font-size: 1.5em;
}
</style>
