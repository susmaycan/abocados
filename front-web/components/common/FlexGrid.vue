<template>
  <div class="flex-list-container">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'FlexGrid'
}
</script>

<style scoped>
.flex-list-container {
  display: flex;
  row-gap: 1em;
  flex-wrap: wrap;
  align-items: stretch;
}
</style>
