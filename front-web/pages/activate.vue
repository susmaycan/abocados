<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t('account_validation') | capitalize }}
      </a-title>
    </template>
    <div v-if="success">
      <a-alert type="success">
        <p>{{ $t('account_validation_success_message') }}</p>
      </a-alert>
      <a-button
        class="my-2"
        color="secondary"
        full-width
        @click="$router.replace({ name: 'login' })"
      >
        {{ $t('login') | capitalize }}
      </a-button>
    </div>
    <div v-else>
      <a-alert type="error">
        <p>{{ $t('account_validation_error_message') }}</p>
        <span v-for="error in errors" :key="error" class="font-weight-bold">{{
          error
        }}</span>
      </a-alert>
      <a-button
        class="my-2"
        color="secondary"
        full-width
        @click="$router.replace({ name: 'index' })"
      >
        {{ $t('go_home') | capitalize }}
      </a-button>
    </div>
  </page-layout>
</template>

<script>
export default {
  name: 'Activate',
  middleware: ['logged-auth'],
  data() {
    return {
      success: false,
      errors: [],
    }
  },
  computed: {
    token() {
      return this.$route.query.token
    },
    userId() {
      return this.$route.query.user
    },
  },
  async mounted() {
    try {
      await this.$api.auth.activateAccount({
        token: this.token,
        user: this.userId,
      })
      this.success = true
      this.errors = null
    } catch (response) {
      this.success = false
      this.errors = response.non_field_errors || []
    }
  },
}
</script>
