<template>
  <v-form ref="password-form" v-model="valid">
    <form-password-input
      :show-confirm-password="true"
      :success="success"
      :errors="formErrors.password"
      @input="onInputChanges('password', $event)"
    />
    <form-success :success="success">
      {{ $t('successfully_saved') | capitalize }}
    </form-success>
    <a-button :disabled="!valid" @click="onSubmit">
      {{ $t('edit') | capitalize }}
    </a-button>
  </v-form>
</template>
<script>
import FormMixin from '@/mixins/form'

export default {
  name: 'UserPasswordForm',
  mixins: [FormMixin],
}
</script>
