<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t('change_password') | capitalize }}
      </a-title>
      <p>{{ $t('change_password_message') | capitalize }}</p>
    </template>
    <div v-if="submit.success" class="my-3">
      <a-alert type="success">
        <p>{{ $t('reset_password_success') }}</p>
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
    <div v-else-if="!check.errors">
      <auth-update-password-form @submit="onSubmit" :errors="submit.errors" />
    </div>
    <div v-else-if="check.errors">
      <a-alert type="error">
        <p>{{ $t('password_check_error_message') }}</p>
        <span class="font-weight-bold">{{ checkErrors }}</span>
      </a-alert>
      <a-button
        class="my-2"
        color="secondary"
        full-width
        @click="$router.replace({ name: 'password-request' })"
      >
        {{ $t('reset_password_again') | capitalize }}
      </a-button>
    </div>
  </page-layout>
</template>

<script>
export default {
  name: 'UpdatePassword',
  middleware: ['logged-auth'],
  data() {
    return {
      check: {
        success: false,
        errors: null,
      },
      submit: {
        success: false,
        errors: null,
      },
    }
  },
  computed: {
    checkErrors() {
      if (
        !this.check.errors ||
        this.check.errors.length === 0 ||
        this.check.errors.non_field_errors.length === 0
      ) {
        return null
      }
      if (Array.isArray(this.check.errors)) {
        return this.check.errors.join('\n')
      }

      if (Array.isArray(this.check.errors.non_field_errors)) {
        return this.check.errors.non_field_errors.join('\n')
      }
      return this.check.errors
    },
    token() {
      return this.$route.query?.token
    },
    userId() {
      return this.$route.query?.user
    },
  },
  async mounted() {
    if (!this.token || !this.userId) {
      this.$router.replace({ name: 'index' })
    }
    try {
      await this.$api.auth.passwordRecoveryCheck({
        token: this.token,
        user: this.userId,
      })
      this.check = {
        success: true,
        errors: null,
      }
    } catch (errors) {
      this.check = {
        success: false,
        errors,
      }
    }
  },
  methods: {
    async onSubmit(form) {
      try {
        await this.$api.auth.passwordRecoveryConfirm({
          token: this.token,
          user: this.userId,
          password: form.password,
        })
        this.submit = {
          success: true,
          errors: null,
        }
      } catch (errors) {
        this.submit = {
          success: false,
          errors,
        }
      }
    },
  },
}
</script>
