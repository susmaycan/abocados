<template>
  <v-form ref="email-form" v-model="valid">
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
    <form-success :success="success">
      {{ $t('successfully_saved') | capitalize }}
    </form-success>
    <a-button :disabled="!valid" @click="onSubmit">
      {{ $t('edit') | capitalize }}
    </a-button>
  </v-form>
</template>
<script>
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'

export default {
  name: 'UserEmailForm',
  mixins: [RulesMixin, FormMixin],
  data() {
    return {
      rules: {
        email: [this.required, this.emailFormat, (v) => this.maxLength(v, 64)],
      },
    }
  },
}
</script>
