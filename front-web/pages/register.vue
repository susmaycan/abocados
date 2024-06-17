<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t('register') | capitalize }}
      </a-title>
      <p>{{ $t('create_your_account') | capitalize }}</p>
    </template>
    <auth-register-form @submit="onSubmit" errors="errors" />
    <template #footer>
      <div class="text-center">
        <p class="clickable">
          {{ $t('already_have_account') }}
          <span class="font-weight-bold" @click="goToLoginPage">{{
            $t('login_here')
          }}</span>
        </p>
      </div>
    </template>
  </page-layout>
</template>

<script>
export default {
  name: 'Register',
  middleware: ['logged-auth'],
  data() {
    return {
      errors: null,
    }
  },
  methods: {
    async onSubmit(form) {
      try {
        const data = await this.$api.auth.register(form)
        if (data.id) {
          this.$router.replace({
            name: 'account-validation',
            query: { user: data.id },
          })
        }
      } catch (response) {
        this.errors = errors
      }
    },
    goToLoginPage() {
      this.$router.push({
        name: 'login',
      })
    },
  },
}
</script>
