<template>
  <page-layout :title="$t('edit_profile') | capitalize">
    <user-form @submit="onSubmit" :data="user" :errors="errors" />
  </page-layout>
</template>

<script>
export default {
  name: 'EditUser',
  middleware: ['auth-custom'],
  data() {
    return {
      user: {},
      errors: {},
    }
  },
  computed: {
    userId() {
      return this.user.id
    },
  },
  mounted() {
    this.getData()
  },
  methods: {
    onSubmit(form) {
      this.$api.user
        .update(this.userId, form)
        .then((data) => {
          if (data.id) {
            this.getData()
            this.errors = null
          }
        })
        .catch((response) => {
          this.errors = response
        })
    },
    async getData() {
      this.user = await this.$api.auth.getUser()
    },
  },
}
</script>
