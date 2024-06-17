<template>
  <a-alert v-if="errors.length > 0" type="error">
    <p v-for="error in errors" :key="error">
      {{ error }}
    </p>
  </a-alert>
</template>
<script>
export default {
  name: 'FormErrors',
  props: {
    errors: {
      type: Array,
      default: [],
    },
  },
}
</script>
