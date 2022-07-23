<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t("recover_password") | capitalize }}
      </a-title>
      <p>{{ $t('enter_email_address') | capitalize }}</p>
    </template>
    <v-form
      ref="recover-password-form"
      v-model="valid"
    >
      <a-input
        :value="form.email"
        :errors="errors.email"
        :rules="rules.email"
        :label="$t('email')"
        full-width
        @input="onInputChanges('email', $event)"
      >
        <template #icon-left>
          <a-icon name="fa-solid fa-at" />
        </template>
      </a-input>

      <div v-if="globalErrors.length > 0" class="my-3">
        <a-alert type="error">
          <p v-for="error in globalErrors" :key="error">
            {{ error }}
          </p>
        </a-alert>
      </div>
      <div v-if="success" class="my-3">
        <a-alert type="success">
          <p>{{ $t('recover_password_ok') }}</p>
        </a-alert>
      </div>

      <a-button
        :disabled="!valid"
        full-width
        color="secondary"
        class="my-2"
        @click="onSubmit"
      >
        {{ $t('send_reset_email') | capitalize }}
      </a-button>
    </v-form>
  </page-layout>
</template>

<script>
import RulesMixin from '@/utils/mixins/rules'

export default {
  name: 'RecoverPassword',
  mixins: [RulesMixin],
  middleware: ['logged-auth'],
  data () {
    return {
      valid: false,
      form: {
        email: null
      },
      errors: {},
      globalErrors: [],
      rules: {
        email: [
          this.required,
          this.emailFormat
        ]
      },
      success: false
    }
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
      this.errors[key] = null
    },
    async onSubmit () {
      if (this.valid) {
        try {
          await this.$api.auth.passwordRecoveryRequest({ email: this.form.email })
          this.success = true
        } catch (response) {
          this.globalErrors = response?.data?.non_field_errors || null
          this.errors = response?.data
        }
      }
    }
  }

}
</script>
