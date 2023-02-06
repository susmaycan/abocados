<template>
  <a-notification color="success" :display="success" :timeout="2000">
    <p><a-icon class="mr-2" name="fa-solid fa-check" /><slot /></p>
  </a-notification>
</template>
<script>
export default {
  name: 'FormSuccess',
  props: {
    success: {
      type: Boolean,
      default: false,
    },
  },
}
</script>
