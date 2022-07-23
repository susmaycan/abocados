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
  name: 'FilterContainer',
  props: {
    selected: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    filterClass () {
      let base = 'filter-container clickable'
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
.filter-container {
  width: 100px;
  height: 100px;
  margin-right: 1em;
  border-radius: 10%;
  border: 1px solid black;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.filter-container:hover {
  /* border: 2px solid black; */ /* uncomment for web */
}
.selected {
  border: 2px solid black;
}
</style>
