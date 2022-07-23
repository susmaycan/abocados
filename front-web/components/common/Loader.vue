<template>
  <div class="loader-container my-5">
    <clip-loader :loading="true" color="#8fcb42" size="24px" />
  </div>
</template>
<script>
import ClipLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'Loader',
  components: {
    ClipLoader
  }
}
</script>
<style scoped>
.loader-container {
  width: 100%;
}
</style>
