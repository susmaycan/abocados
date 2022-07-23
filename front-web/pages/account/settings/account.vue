<template>
  <page-layout :title="$t('account_settings') | capitalize">
    <p>{{ $t('account_settings_description') }}</p>
    <h2>{{ $t('edit_email') | capitalize }}</h2>
    <v-form
      ref="email-form"
      v-model="validEmail"
    >
      <a-input
        :value="form.email"
        :errors="errors.email"
        :rules="rules.email"
        :success="success.email"
        :label="$t('email')"
        full-width
        @input="onInputChanges('email', $event)"
      >
        <template #icon-left>
          <a-icon name="fa-solid fa-at" />
        </template>
      </a-input>
      <a-button
        :disabled="!validEmail"
        @click="onSubmitEmail"
      >
        {{ $t('edit') | capitalize }}
      </a-button>
    </v-form>
    <h2>{{ $t('edit_password') | capitalize }}</h2>
    <v-form
      ref="password-form"
      v-model="validPassword"
    >
      <a-password-input
        :show-confirm-password="true"
        :success="success.password"
        :errors="errors.password"
        @input="onInputChanges('password', $event)"
      />
      <a-button
        :disabled="!validPassword"
        @click="onSubmitPassword"
      >
        {{ $t('edit') | capitalize }}
      </a-button>
    </v-form>
    <template #footer>
      <a-button
        color="error"
        full-width
        class="mt-3"
        icon="fa-solid fa-trash"
        @click="$router.push({ name: 'account-delete' })"
      >
        {{ $t('delete_account') | capitalize }}
      </a-button>
    </template>
  </page-layout>
</template>
<script>
import { capitalize } from 'lodash'
import RulesMixin from '@/utils/mixins/rules'

export default {
  name: 'AccountSettings',
  mixins: [RulesMixin],
  middleware: ['auth-custom'],
  data () {
    return {
      user: {},
      form: {
        email: null,
        password: null,
        confirmPassword: null
      },
      errors: [],
      success: {},
      rules: {
        email: [
          this.required,
          this.emailFormat,
          v => this.maxLength(v, 64)
        ]
      },
      validPassword: false,
      validEmail: false
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    onDelete () {
      this.$router.push({ name: 'account-delete' })
    },
    async getData () {
      this.user = await this.$api.auth.getUser()
      this.form.email = this.user.email
    },
    onInputChanges (key, value) {
      this.form[key] = value
      this.errors[key] = null
    },
    onSubmitPassword () {
      if (this.validPassword) {
        this.$api.user.update(this.user.id, { password: this.form.password })
          .then((data) => {
            if (data.id) {
              this.success.password = capitalize(this.$t('successfully_saved'))
            }
          })
          .catch(({ response }) => {
            this.globalErrors = response?.data?.non_field_errors || []
            this.errors = response?.data
            this.success.email = null
          })
      }
    },
    onSubmitEmail () {
      if (this.validEmail) {
        this.$api.user.update(this.user.id, { email: this.form.email })
          .then((data) => {
            if (data.id) {
              this.success.email = capitalize(this.$t('successfully_saved'))
            }
          })
          .catch(({ response }) => {
            this.globalErrors = response?.data?.non_field_errors || []
            this.errors = response?.data
            this.success.password = null
          })
      }
    }
  }
}
</script>
