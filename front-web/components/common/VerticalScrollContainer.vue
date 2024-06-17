<template>
  <div
    class="vertical-scroll"
    v-bind="$attrs"
  >
    <slot />
  </div>
</template>

<script>
export default {
  name: 'Grid'
}
</script>

<style scoped>
.vertical-scroll {
  overflow-x: auto;
  display: flex;
  width: 90vw;
  padding: .5em 0;
}
</style>
