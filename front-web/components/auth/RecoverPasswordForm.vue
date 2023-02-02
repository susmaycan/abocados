<template>
  <v-form ref="recover-password-form" v-model="valid">
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

    <form-errors :errors="globalErrors" />

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
</template>

<script>
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'

export default {
  name: 'RecoverPasswordForm',
  mixins: [RulesMixin, FormMixin],
  data() {
    return {
      rules: {
        email: [this.required, this.emailFormat],
      },
    }
  },
}
</script>
