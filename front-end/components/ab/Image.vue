<script setup lang="ts">
defineProps<{
  src: string
  alt: string
  height?: number
  width?: number
}>()
</script>
<template>
  <img
    v-bind="$attrs"
    :alt="alt"
    class="ab-image"
    :height="height || 250"
    :src="src"
    :width="width || 250"
  />
</template>

<style scoped>
.ab-image {
  object-fit: cover;
}
</style>
