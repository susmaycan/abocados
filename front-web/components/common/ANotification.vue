<template>
  <v-snackbar
    :value="display"
    v-bind="$attrs"
    :timeout="timeout"
  >
    <slot />
  </v-snackbar>
</template>

<script>
export default {
  name: 'ANotification',
  props: {
    timeout: {
      type: Number,
      default: null
    },
    display: {
      type: Boolean,
      default: null
    }
  }
}
</script>
