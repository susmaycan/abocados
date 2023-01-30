<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t("register") | capitalize }}
      </a-title>
      <p>{{ $t("create_your_account") | capitalize }}</p>
    </template>
    <v-form ref="register-form" v-model="valid">
      <form-text-input
        :value="form.username"
        :errors="errors.username"
        :label="$t('username')"
        :rules="rules.username"
        :counter="20"
        full-width
        @input="onInputChanges('username', $event)"
      >
        <template #icon-left>
          <a-icon name="fa-solid fa-user" />
        </template>
      </form-text-input>

      <form-text-input
        :value="form.email"
        :errors="errors.email"
        :rules="rules.email"
        :label="$t('email')"
        :counter="64"
        full-width
        @input="onInputChanges('email', $event)"
      >
        <template #icon-left>
          <a-icon name="fa-solid fa-at" />
        </template>
      </form-text-input>

      <form-password-input
        :show-confirm-password="true"
        :errors="errors.password"
        @input="onInputChanges('password', $event)"
      />

      <a-alert v-if="globalErrors.length > 0" type="error">
        <p v-for="error in globalErrors" :key="error">
          {{ error }}
        </p>
      </a-alert>

      <a-button
        :disabled="!valid"
        class="my-2"
        color="secondary"
        full-width
        @click="onSubmit"
      >
        {{ $t("register") | capitalize }}
      </a-button>
    </v-form>
    <template #footer>
      <div class="text-center">
        <p class="clickable">
          {{ $t("already_have_account") }}
          <span class="font-weight-bold" @click="goToLoginPage">{{
            $t("login_here")
          }}</span>
        </p>
      </div>
    </template>
  </page-layout>
</template>

<script>
import RulesMixin from '@/utils/mixins/rules'

export default {
  name: 'Register',
  mixins: [RulesMixin],
  middleware: ['logged-auth'],
  data () {
    return {
      valid: false,
      form: {
        username: null,
        email: null,
        password: null
      },
      errors: {},
      globalErrors: [],
      rules: {
        username: [
          this.required,
          v => this.minLength(v, 3),
          v => this.maxLength(v, 20)
        ],
        email: [this.required, this.emailFormat, v => this.maxLength(v, 64)]
      }
    }
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
      this.errors[key] = null
    },
    async onSubmit () {
      if (this.valid) {
        this.errors = {}
        this.globalErrors = []
        try {
          const data = await this.$api.auth.register(this.form)
          if (data.id) {
            this.$router.replace({
              name: 'account-validation',
              query: { user: data.id }
            })
          }
        } catch (response) {
          this.globalErrors = response?.data?.non_field_errors || []
          this.errors = response?.data
        }
      }
    },
    goToLoginPage () {
      this.$router.push({
        name: 'login'
      })
    }
  }
}
</script>
