<template>
  <page-layout :title="$t('account_settings') | capitalize">
    <p>{{ $t('account_settings_description') }}</p>
    <section class="my-2">
      <h2>{{ $t('edit_email') | capitalize }}</h2>
      <user-form-email @submit="onSubmitEmail" :data="user" :errors="errors" />
    </section>
    <section class="my-2">
      <h2>{{ $t('edit_password') | capitalize }}</h2>
      <user-form-password
        @submit="onSubmitPassword"
        :data="user"
        :errors="errors"
      />
    </section>
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

export default {
  name: 'AccountSettings',
  middleware: ['auth-custom'],
  data() {
    return {
      user: {},
      errors: {},
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    onDelete() {
      this.$router.push({ name: 'account-delete' })
    },
    async getData() {
      this.user = await this.$api.auth.getUser()
    },
    onSubmitPassword(form) {
      this.$api.user
        .update(this.user.id, form)
        .then((data) => {
          if (data.id) {
            this.errors = null
          }
        })
        .catch((response) => {
          this.errors = response
        })
    },
    onSubmitEmail(form) {
      this.$api.user
        .update(this.user.id, form)
        .then((data) => {
          if (data.id) {
            this.errors = null
          }
        })
        .catch((response) => {
          this.errors = response
        })
    },
  },
}
</script>
