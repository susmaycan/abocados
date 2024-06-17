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
    <user-profile
      v-if="user"
      :user="user"
      :recipes="recipes"
      :favourites="favourites"
    />
  </page-layout>
</template>
<script>
export default {
  name: 'Account',
  middleware: ['auth-custom'],
  data() {
    return {
      user: {},
      recipes: [],
      favourites: [],
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      this.user = await this.$api.auth.getUser()
      const data = await this.$api.user.sublist(this.user.id, { limit: 4 })
      this.recipes = data.results
      const favouriteData = await this.$api.favourite.list(this.user.id)
      this.favourites = favouriteData.results
    },
  },
}
</script>
