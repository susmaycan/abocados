<template>
  <mobile-layout :back="false">
    <template #title>
      <app-logo v-if="!loggedIn" width="200" height="200" />
      <a-title>
        {{ $t("app_name") }}
      </a-title>
    </template>
    <div>
      <p>{{ $t('guest_home_text') }}</p>
      <a-button
        color="secondary"
        class="guest-home-button"
        full-width
        @click="$router.push({ name: 'login'})"
      >
        {{ $t('login') }}
      </a-button>
      <span>{{ $t('or') }}</span>
      <a-button
        color="secondary"
        class="guest-home-button"
        full-width
        @click="$router.push({ name: 'register'})"
      >
        {{ $t('register') }}
      </a-button>
    </div>
    <template #footer>
      <language-selector class="mx-4" />
    </template>
  </mobile-layout>
</template>
<script>
import { mapState } from 'vuex'

export default {
  name: 'GuestHomepage',
  computed: {
    ...mapState('user', ['loggedIn'])
  }
}
</script>
