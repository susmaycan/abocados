<script setup lang="ts">
defineProps<{
  height?: number
  width?: number
}>()
</script>
<template>
  <ab-image
    alt="abocados logo"
    :height="height"
    src="https://abocados-s3-bucket.s3.eu-west-3.amazonaws.com/logo.svg"
    :width="width"
  />
</template>
