<template>
  <v-form ref="update-password-form" v-model="valid">
    <form-password-input
      :errors="formErrors.password"
      :show-confirm-password="true"
      @input="onInputChanges('password', $event)"
    />

    <form-errors :errors="globalErrors" />

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
</template>

<script>
import FormMixin from '@/mixins/form'

export default {
  name: 'UpdatePasswordForm',
  mixins: [FormMixin],
}
</script>
