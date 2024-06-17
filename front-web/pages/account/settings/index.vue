<template>
  <page-layout :title="$t('settings') | capitalize">
    <div v-if="user" class="d-flex justify-start flex-column align-center">
      <user-image :src="user.picture" width="100" height="100" />
      <h2 class="font-weight-bold">@{{ user.username }}</h2>
      <a-button
        text
        icon="fa-solid fa-pen"
        @click="$router.push({ name: 'account-edit' })"
      >
        {{ $t('edit_profile') | capitalize }}
      </a-button>
    </div>

    <div>
      <div
        v-for="section in sections"
        :key="section.name"
        class="clickable setting-section d-flex align-baseline p-2"
        @click="$router.push({ name: section.path })"
      >
        <a-icon class="section-icon" :name="section.icon" />
        <div class="ml-3">
          <p class="font-weight-bold">
            {{ $t(section.name) | capitalize }}
          </p>
        </div>
        <a-icon class="ml-auto" name="fa-solid fa-circle-arrow-right" />
      </div>
    </div>

    <template #footer>
      <a-button
        color="secondary"
        full-width
        class="mt-3"
        icon="fa-solid fa-right-from-bracket"
        @click="onLogOut()"
      >
        {{ $t('logout') | capitalize }}
      </a-button>
    </template>
  </page-layout>
</template>
<script>
export default {
  name: 'Settings',
  middleware: ['auth-custom'],
  data() {
    return {
      user: {},
      sections: [
        {
          name: 'account_settings',
          icon: 'fa-solid fa-user',
          path: 'account-settings-account',
        },
        {
          name: 'application_settings',
          icon: 'fa-solid fa-wrench',
          path: 'account-settings-app',
        },
      ],
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    onLogOut() {
      this.$store.dispatch('user/removeUserData')
      this.$router.push({ name: 'index' })
    },
    async getData() {
      this.user = await this.$api.auth.getUser()
    },
  },
}
</script>
<style scoped>
.section-icon {
  font-size: 2em;
}
.setting-section {
  border: 1px solid black;
  border-radius: 10px;
  margin: 1em 0;
  padding: 0.5em 2em;
}
.setting-section:hover {
  border: 1px solid white;
  background-color: black;
  color: white;
}
</style>
