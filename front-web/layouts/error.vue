<template>
  <a-error-layout :error="error" />
</template>

<script>
export default {
  layout: 'error',
  props: {
    error: {
      type: [String, Object],
      default: null,
    },
  },
}
</script>
