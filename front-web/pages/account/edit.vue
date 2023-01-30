<template>
  <page-layout :title="$t('edit_profile') | capitalize">
    <v-form ref="user-form" v-model="valid">
      <user-image
        :src="user.picture"
        width="150"
        height="150"
        :edition="true"
      />
      <a-modal name="user-picture-edit-modal" :display-button-actions="false">
        <template #title>
          <a-subtitle>
            <a-icon name="fa-solid fa-image" />
            {{ $t("upload_picture") | capitalize }}
          </a-subtitle>
        </template>
        <form-file-input
          :value="form.picture"
          :error-messages="errors.picture"
          :label="$t('picture')"
          accept="image/*"
          @input="onInputChanges('picture', $event)"
        />

        <template #button-actions>
          <a-button
            color="secondary"
            :disabled="!!form.picture"
            @click="submitPicture"
          >
            {{ $t("upload") | capitalize }}
          </a-button>
        </template>
      </a-modal>
      <form-text-input
        :value="user.username"
        :label="$t('username')"
        :disabled="true"
      />
      <form-text-input
        :value="form.name"
        :errors="errors.name"
        :label="$t('name')"
        :counter="180"
        @input="onInputChanges('name', $event)"
      />

      <a-alert v-if="globalErrors.length > 0" type="error">
        <p v-for="error in globalErrors" :key="error">
          {{ error }}
        </p>
      </a-alert>

      <a-notification color="success" :display="!!success" :timeout="2000">
        <p>
          <a-icon class="mr-2" name="fa-solid fa-check" />{{
            success | capitalize
          }}
        </p>
      </a-notification>

      <a-button
        class="mt-4"
        :disabled="!valid"
        color="secondary"
        full-width
        @click="submitForm"
      >
        {{ $t("save") | capitalize }}
      </a-button>
    </v-form>
  </page-layout>
</template>

<script>
export default {
  name: 'EditUser',
  middleware: ['auth-custom'],
  data () {
    return {
      valid: false,
      form: {
        name: null,
        picture: null
      },
      user: {
        id: null
      },
      errors: {},
      globalErrors: [],
      success: null
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
      this.errors[key] = null
    },
    submitPicture () {
      this.submit({ picture: this.form.picture })
    },
    submitForm () {
      if (this.valid) {
        const newForm = { ...this.form }
        delete newForm.picture
        this.submit(newForm)
      }
    },
    submit (body) {
      this.$api.user
        .update(this.user.id, body)
        .then((data) => {
          if (data.id) {
            this.getData()
            this.success = this.$t('successfully_saved')
            this.clearErrors()
          }
        })
        .catch(({ response }) => {
          this.globalErrors = response?.data?.non_field_errors || []
          this.errors = response?.data
          this.success = null
        })
    },
    async getData () {
      const data = await this.$api.auth.getUser()
      this.user = data
      this.form = { name: data.name }
    },
    clearErrors () {
      this.globalErrors = []
      this.errors = {}
    }
  }
}
</script>
