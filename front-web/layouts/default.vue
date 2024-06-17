<template>
  <v-app>
    <v-main>
      <div v-if="$device.isDesktop">
        <navbar />
      </div>
      <v-container v-if="!error">
        <Nuxt />
      </v-container>
      <div v-else>
        <a-error-layout :error="error.status" />
      </div>
      <div v-if="!$device.isDesktop && loggedIn">
        <bottom-navbar />
      </div>
    </v-main>
    <a-footer v-if="$device.isDesktop" />
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'DefaultLayout',
  computed: {
    ...mapState('user', ['isLoggedIn']),
    ...mapState(['error']),
  },
  mounted() {
    if (this.loggedIn) {
      this.loadCategories()
    }
  },
  methods: {
    ...mapActions(['loadCategories']),
  },
}
</script>

<style>
.clickable {
  cursor: pointer;
}
</style>
