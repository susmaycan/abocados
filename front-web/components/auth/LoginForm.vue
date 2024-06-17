<template>
  <v-form ref="login-form" v-model="valid">
    <form-text-input
      :value="form.email"
      :errors="formErrors.email"
      :rules="rules.email"
      :label="$t('email')"
      full-width
      @input="onInputChanges('email', $event)"
    >
      <template #icon-left>
        <a-icon name="fa-solid fa-at" />
      </template>
    </form-text-input>
    <form-password-input
      :errors="formErrors.password"
      @input="onInputChanges('password', $event)"
    />
    <div class="d-flex justify-end">
      <p class="font-weight-bold clickable" @click="goToPasswordRecoveryPage">
        {{ $t('forgot_password') | capitalize }}
      </p>
    </div>

    <form-errors :errors="globalErrors" />

    <a-button color="secondary" :disabled="!valid" full-width @click="onSubmit">
      {{ $t('login') }}
    </a-button>
  </v-form>
</template>

<script>
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'

export default {
  name: 'LoginForm',
  mixins: [RulesMixin, FormMixin],
  data() {
    return {
      rules: {
        email: [this.required, this.emailFormat],
      },
    }
  },
  methods: {
    goToPasswordRecoveryPage() {
      this.$emit('recover-password')
    },
  },
}
</script>
