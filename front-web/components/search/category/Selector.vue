<template>
  <div class="text-left">
    <a-label>{{ name | capitalize }}:</a-label>
    <vertical-scroll-container class="py-3">
      <div v-for="category in categories" :key="category.id">
        <search-category-filter
          :selected="isSelected(category.id)"
          :category="category"
          @click="onClick(category.id)"
        />
      </div>
    </vertical-scroll-container>
  </div>
</template>
<script>
export default {
  name: 'CategorySearchSelector',
  props: {
    categories: {
      type: Array,
      default() {
        return []
      },
    },
    name: {
      type: String,
      default: '',
    },
    categoryFilters: {
      type: Array,
      default() {
        return []
      },
    },
  },
  methods: {
    isSelected(id) {
      return this.categoryFilters?.includes(id)
    },
    onClick(id) {
      if (this.isSelected(id)) {
        this.$emit('unselect', id)
      } else {
        this.$emit('select', id)
      }
    },
  },
}
</script>
