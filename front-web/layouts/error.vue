<template>
  <a-error-layout :error="error" />
</template>

<script>
export default {
  layout: 'error',
  props: {
    error: {
      type: String,
      default: null
    }
  }
}
</script>
