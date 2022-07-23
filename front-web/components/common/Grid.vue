<template>
  <div class="list-container justify-center justify-md-start">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'Grid'
}
</script>

<style scoped>
.list-container {
  display: flex;
  row-gap: 1em;
  flex-wrap: wrap;
  align-items: stretch;
}
</style>
