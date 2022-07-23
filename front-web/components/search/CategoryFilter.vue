<template>
  <filter-container :selected="selected" @click="onClick">
    <a-image :src="category.picture" height="40" width="40" />
    <span class="category-filter-title">
      {{ category.name | capitalize }}
    </span>
  </filter-container>
</template>

<script>

export default {
  name: 'CategoryFilter',
  props: {
    category: {
      type: Object,
      required: true
    },
    selected: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    onClick () {
      this.$emit('click', this.category.id)
    }
  }
}
</script>

<style scoped>
.category-filter-title {
  font-size: 15px;
  font-weight: bold;
}
</style>
