<template>
  <v-form ref="register-form" v-model="valid">
    <form-text-input
      :value="form.username"
      :errors="formErrors.username"
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
      :errors="formErrors.email"
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
      :errors="formErrors.password"
      @input="onInputChanges('password', $event)"
    />
    <form-errors :errors="globalErrors" />

    <a-button
      :disabled="!valid"
      class="my-2"
      color="secondary"
      full-width
      @click="onSubmit"
    >
      {{ $t('register') | capitalize }}
    </a-button>
  </v-form>
</template>

<script>
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'

export default {
  name: 'RegisterForm',
  mixins: [RulesMixin, FormMixin],
  data() {
    return {
      rules: {
        username: [
          this.required,
          (v) => this.minLength(v, 3),
          (v) => this.maxLength(v, 20),
        ],
        email: [this.required, this.emailFormat, (v) => this.maxLength(v, 64)],
      },
    }
  },
}
</script>
