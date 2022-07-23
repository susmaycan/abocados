<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t("change_password") | capitalize }}
      </a-title>
      <p> {{ $t("change_password_message") | capitalize }}</p>
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
        {{ $t("go_home") | capitalize }}
      </a-button>
    </div>
    <div v-else-if="check.success">
      <v-form
        ref="update-password-form"
        v-model="valid"
      >
        <a-password-input
          :errors="submit.errors.password"
          :show-confirm-password="true"
          @input="onInputChanges('password', $event)"
        />

        <div v-if="submit.globalErrors.length > 0" class="my-3">
          <a-alert type="error">
            <p v-for="error in submit.globalErrors" :key="error">
              {{ error }}
            </p>
          </a-alert>
        </div>
        <a-button
          :disabled="!valid"
          full-width
          color="secondary"
          class="my-2"
          @click="onSubmit"
        >
          {{ $t('reset_password') | capitalize }}
        </a-button>
      </v-form>
    </div>
    <div v-else-if="checkErrors">
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
        {{ $t("reset_password_again") | capitalize }}
      </a-button>
    </div>
  </page-layout>
</template>

<script>
export default {
  name: 'Update',
  middleware: ['logged-auth'],
  data () {
    return {
      form: {
        password: null
      },
      check: {
        success: false,
        errors: []
      },
      submit: {
        errors: {},
        success: false,
        globalErrors: []
      },
      valid: false,
      token: null,
      userId: null
    }
  },
  computed: {
    checkErrors () {
      if (!this.check.errors || this.check.errors.length === 0) {
        return null
      }
      if (Array.isArray(this.check.errors)) {
        return this.check.errors.join('\n')
      }
      return this.check.errors
    }
  },
  async mounted () {
    const { token, user } = this.$route.query
    this.token = token
    this.userId = user
    if (!token || !user) {
      this.$router.replace({ name: 'index' })
    }
    try {
      await this.$api.auth.passwordRecoveryCheck({ token: this.token, user: this.userId })
      this.check = {
        success: true,
        errors: []
      }
    } catch (response) {
      this.check = {
        success: false,
        errors: response?.data?.non_field_errors || response?.data || []
      }
    }
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
      this.submit.errors[key] = null
    },
    async onSubmit () {
      if (this.valid) {
        try {
          await this.$api.auth.passwordRecoveryConfirm({ token: this.token, user: this.userId, password: this.form.password })
          this.submit = {
            errors: {},
            success: true,
            globalErrors: []
          }
        } catch (response) {
          this.submit = {
            errors: response?.data,
            success: false,
            globalErrors: response?.data?.non_field_errors || []
          }
        }
      }
    }
  }
}
</script>
