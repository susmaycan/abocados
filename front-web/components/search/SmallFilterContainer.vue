<template>
  <div
    :class="filterClass"
    v-bind="$attrs"
    @click="onClick"
  >
    <slot />
  </div>
</template>

<script>

export default {
  name: 'SmallFilterContainer',
  props: {
    selected: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    filterClass () {
      let base = 'small-filter-container clickable'
      if (this.selected) {
        base += ' selected'
      }
      return base
    }
  },
  methods: {
    onClick () {
      this.$emit('click')
    }
  }
}
</script>

<style scoped>
.small-filter-container {
  width: 100px;
  height: 50px;
  margin-right: 1em;
  border-radius: 10px;
  border: 1px solid var(--v-secondary-base);
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.small-filter-container:hover {
  border: 2px solid var(--v-secondary-base);
}
.selected {
  background-color: var(--v-secondary-base);
  border: 2px solid var(--v-secondary-base);
  color: white;
}
</style>
