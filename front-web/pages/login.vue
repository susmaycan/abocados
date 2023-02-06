<template>
  <page-layout>
    <template #title>
      <app-logo v-if="$device.isMobile" width="100" height="100" />
      <a-title>
        {{ $t('welcome_back') | capitalize }}
      </a-title>
      <p>{{ $t('login_to_your_account') | capitalize }}</p>
    </template>
    <auth-login-form
      @submit="onSubmit"
      @recover-password="goToPasswordRecoveryPage"
      :errors="errors"
    />
    <template #footer>
      <div class="text-center">
        <p class="clickable">
          {{ $t('dont_have_account') }}
          <span class="font-weight-bold" @click="goToRegisterPage">{{
            $t('sign_up_here')
          }}</span>
        </p>
      </div>
    </template>
  </page-layout>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  middleware: ['logged-auth'],
  data() {
    return {
      errors: null,
    }
  },
  methods: {
    ...mapActions(['loadCategories']),
    async onSubmit(form) {
      try {
        const data = await this.$api.auth.login(form)
        if (data) {
          this.$store.commit('user/setUser', data)
          this.loadCategories()
          this.$router.push({
            name: 'index',
          })
        }
      } catch (response) {
        this.errors = response
      }
    },
    goToPasswordRecoveryPage() {
      this.$router.push({
        name: 'password-request',
      })
    },
    goToRegisterPage() {
      this.$router.push({
        name: 'register',
      })
    },
  },
}
</script>
