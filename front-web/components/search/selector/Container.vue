<template>
  <div :class="filterClass" @click="onClick">
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    selected: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    filterClass() {
      return {
        'filter-container': true,
        'filter-container-selected': this.selected,
      }
    },
  },
  methods: {
    onClick() {
      this.$emit('click')
    },
  },
}
</script>

<style lang="scss" scoped>
.filter-container {
  width: 90px;
  height: 90px;
  padding: 0.5em;
  margin-right: 1em;
  border-radius: 10px;
  border: 1px solid var(--v-secondary-base);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.filter-container:hover {
  background-color: var(--v-secondary-base);
  border: 2px solid var(--v-secondary-base);
  color: white;
}
.filter-container-selected {
  background-color: var(--v-secondary-base);
  border: 2px solid var(--v-secondary-base);
  color: white;
}
</style>
