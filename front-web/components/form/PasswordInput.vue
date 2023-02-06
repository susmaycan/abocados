<template>
  <div>
    <form-text-input
      :value="password"
      :errors="errors"
      :rules="rules.password"
      :label="$t('password')"
      :type="showPassword ? 'text' : 'password'"
      full-width
      @input="onInput"
    >
      <template #icon-left>
        <a-icon name="fa-solid fa-lock" />
      </template>
      <template #icon-right>
        <span
          @click="toggleShowPassword"
        ><a-icon
          :name="showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"
        /></span>
      </template>
    </form-text-input>
    <form-text-input
      v-if="showConfirmPassword"
      :value="confirmPassword"
      type="password"
      :rules="rules.confirmPassword"
      :errors="confirmPasswordErrors"
      :label="$t('confirm_password')"
      full-width
      @input="onConfirmPasswordChange"
    >
      <template #icon-left>
        <a-icon name="fa-solid fa-lock" />
      </template>
    </form-text-input>
  </div>
</template>
<script>
import { capitalize } from 'lodash'
import RulesMixin from '@/mixins/rules'

export default {
  name: 'APasswordInput',
  mixins: [RulesMixin],
  props: {
    errors: {
      type: [String, Array, Object],
      required: false,
      default: ''
    },
    showConfirmPassword: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  data () {
    return {
      password: null,
      confirmPassword: null,
      confirmPasswordErrors: null,
      rules: {
        password: [
          this.required,
          v => this.minLength(v, 8),
          v => this.maxLength(v, 64)
        ],
        confirmPassword: [this.required]
      },
      showPassword: false
    }
  },
  methods: {
    onInput (newVal) {
      this.password = newVal
      this.$emit('input', this.password)
    },
    onConfirmPasswordChange (value) {
      this.showPassword = false
      this.confirmPassword = value
      if (this.confirmPassword !== this.password) {
        this.confirmPasswordErrors = capitalize(
          this.$t('passwords_dont_match')
        )
      } else {
        this.confirmPasswordErrors = null
      }
    },
    toggleShowPassword () {
      this.showPassword = !this.showPassword
    }
  }
}
</script>
