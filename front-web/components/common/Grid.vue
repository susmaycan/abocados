<template>
  <div :class="this.$device.isDesktop ? 'list-container-desktop' : 'list-container-mobile'">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'Grid'
}
</script>

<style scoped>
.list-container-desktop {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1em;
  grid-auto-rows: minmax(100px, auto);
}
.list-container-mobile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  row-gap: 1em;
}
</style>
