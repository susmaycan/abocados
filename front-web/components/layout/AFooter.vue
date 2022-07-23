<template>
  <v-footer
    app
  >
    <span>&copy; {{ new Date().getFullYear() }} {{ $t("app_name") | capitalize }}</span>
  </v-footer>
</template>
<script>

export default {
  name: 'AFooter'
}
</script>
