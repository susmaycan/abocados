<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t('recover_password') | capitalize }}
      </a-title>
      <p>{{ $t('enter_email_address') | capitalize }}</p>
    </template>
    <auth-recover-password-form @submit="onSubmit" :errors="errors" />

    <form-success :success="success">
      <p>{{ $t('recover_password_ok') }}</p>
    </form-success>
  </page-layout>
</template>

<script>
export default {
  name: 'RecoverPassword',
  middleware: ['logged-auth'],
  data() {
    return {
      errors: null,
      success: false,
    }
  },
  methods: {
    async onSubmit(form) {
      try {
        await this.$api.auth.passwordRecoveryRequest({
          email: form.email,
        })
        this.errors = false
        this.success = true
      } catch (response) {
        this.success = false
        this.errors = response
      }
    },
  },
}
</script>
