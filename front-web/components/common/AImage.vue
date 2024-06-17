<template>
  <img
    v-bind="$attrs"
    :height="height"
    :width="width"
    :src="src"
    class="a-image"
  >
</template>

<script>
export default {
  name: 'AButton',
  props: {
    src: {
      type: String,
      required: false,
      default: null
    },
    height: {
      type: String,
      default: '250'
    },
    width: {
      type: String,
      default: '250'
    }
  }
}
</script>
<style scoped>
.a-image {
  object-fit: cover;
}
</style>
