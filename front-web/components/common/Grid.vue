<template>
  <div class="list-container" :style="cssProps">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'Grid',
  props: {
    cols: {
      type: Number,
      default: 3
    }
  },
  computed: {
    cssProps () {
      return {
        '--grid-columns': this.$device.isMobile ? 'repeat(1, 1fr)' : `repeat(${this.cols}, 1fr)`
      }
    }
  }

}
</script>

<style scoped>
.list-container {
  display: grid;
  grid-template-columns: var(--grid-columns);
  grid-gap: 1em;
  grid-auto-rows: minmax(100px, auto);
}
</style>
