<template>
  <v-form ref="user-form" v-model="valid">
    <form-image
      width="150"
      height="150"
      :image="form.picture"
      type="user"
      :errors="formErrors.picture"
      @input="onInputChanges('picture', $event)"
    />
    <form-text-input
      :value="form.username"
      :label="$t('username')"
      :disabled="true"
    />
    <form-text-input
      :value="form.name"
      :errors="formErrors.name"
      :label="$t('name')"
      :counter="180"
      @input="onInputChanges('name', $event)"
    />

    <form-errors :errors="globalErrors" />

    <form-success :success="success">
      <span>{{ $t('successfully_saved') | capitalize }}</span>
    </form-success>

    <a-button
      class="mt-4"
      :disabled="!valid"
      color="secondary"
      full-width
      @click="onSubmit"
    >
      {{ $t('save') | capitalize }}
    </a-button>
  </v-form>
</template>

<script>
import FormMixin from '@/mixins/form'
export default {
  name: 'UserForm',
  mixins: [FormMixin],
}
</script>
