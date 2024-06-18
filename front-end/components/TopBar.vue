<script setup lang="ts">
const { isAuthenticated, logIn: authenticate, logOut } = useAuth()

const logIn = () => {
  authenticate(
    {
      name: 'Patatita',
      id: 1,
      email: 'patatita@gmail.com',
      username: 'patatita',
    },
    'patata_token'
  )
}
</script>

<template>
  <div class="flex items-center">
    <nuxt-link to="/">
      <div class="flex items-center">
        <ab-app-logo :width="30" :height="30" /> {{ $t('app_name') }}
      </div>
    </nuxt-link>

    <div class="ml-auto flex items-end gap-2">
      <ab-button v-if="!isAuthenticated" @click="logIn">{{
        $t('login')
      }}</ab-button>
      <ab-button v-if="isAuthenticated" @click="logOut">{{
        $t('logout')
      }}</ab-button>
      <lang-switcher />
      <theme-switcher />
    </div>
  </div>
</template>
