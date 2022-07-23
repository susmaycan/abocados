<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t("welcome_back") | capitalize }}
      </a-title>
      <p>{{ $t('login_to_your_account') | capitalize }}</p>
    </template>
    <v-form
      ref="login-form"
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
      <a-password-input
        :errors="errors.password"
        @input="onInputChanges('password', $event)"
      />
      <div class="d-flex justify-end">
        <p class="font-weight-bold clickable" @click="goToPasswordRecoveryPage">
          {{ $t('forgot_password') | capitalize }}
        </p>
      </div>

      <a-alert v-if="globalErrors.length > 0" type="error">
        <span v-for="error in globalErrors" :key="error">
          {{ error | capitalize }}
        </span>
      </a-alert>

      <a-button
        color="secondary"
        :disabled="!valid"
        full-width
        @click="onSubmit"
      >
        {{ $t('login') }}
      </a-button>
    </v-form>
    <template #footer>
      <div class="text-center">
        <p class="clickable">
          {{ $t('dont_have_account') }} <span class="font-weight-bold" @click="goToRegisterPage">{{ $t('sign_up_here') }}</span>
        </p>
      </div>
    </template>
  </page-layout>
</template>

<script>
import RulesMixin from '@/utils/mixins/rules'

export default {
  name: 'Login',
  mixins: [RulesMixin],
  middleware: ['logged-auth'],
  data () {
    return {
      valid: false,
      form: {
        email: null,
        password: null
      },
      errors: {},
      globalErrors: [],
      rules: {
        email: [
          this.required,
          this.emailFormat
        ]
      }
    }
  },
  methods: {
    async onSubmit () {
      if (this.valid) {
        this.showPassword = false
        try {
          const data = await this.$api.auth.login(this.form)
          if (data) {
            this.$store.commit('user/setUser', data)
            this.$router.push({
              name: 'index'
            })
          }
        } catch (response) {
          this.globalErrors = response?.data?.non_field_errors || []
          this.errors = response?.data
        }
      }
    },
    onInputChanges (key, value) {
      this.form[key] = value
      this.errors[key] = null
    },
    goToPasswordRecoveryPage () {
      this.$router.push({
        name: 'password-request'
      })
    },
    goToRegisterPage () {
      this.$router.push({
        name: 'register'
      })
    }
  }

}
</script>
