<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t("register_success") | capitalize }}
      </a-title>
    </template>
    <div v-if="userId && !error">
      <p>{{ $t('register_success_message') | capitalize }}</p>
      <v-divider />
      <p>{{ $t('havent_receive_any_email') | capitalize }}</p>
      <a-button
        color="primary"
        full-width
        @click="resendEmail"
      >
        {{ $t('resend_email') }}
      </a-button>
      <a-notification color="success" :display="!error" :timeout="2000">
        <p><a-icon class="mr-2" name="fa-solid fa-envelope" />{{ $t('email_sent') | capitalize }}</p>
      </a-notification>
    </div>
    <div v-if="error" class="my-2">
      <a-alert type="error">
        <span class="font-weight-bold">{{ error }}</span>
      </a-alert>
      <a-button
        class="my-2"
        color="secondary"
        full-width
        @click="$router.replace({ name: 'index' })"
      >
        {{ $t("go_home") | capitalize }}
      </a-button>
    </div>
  </page-layout>
</template>

<script>

export default {
  name: 'AccountValidation',
  middleware: ['logged-auth'],
  data () {
    return {
      error: null,
    }
  },
  computed: {
    userId () {
      return this.$route.query.user
    }
  },
  mounted () {
    if (!this.userId) {
      this.$router.replace({ name: 'index' })
    }
  },
  methods: {
    async resendEmail () {
      try {
        await this.$api.auth.sendValidationEmail({ id: this.userId })
        this.error = null
      } catch (error) {
        this.error = error?.data
      }
    }
  }

}
</script>
