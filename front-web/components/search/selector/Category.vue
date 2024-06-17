<template>
  <search-selector
    :value="value"
    @input="selectCategory"
    :filter-list="categories"
    :component="CategoryFilter"
  >
    <template #label>
      <a-label>{{ name | capitalize }}:</a-label>
    </template>
  </search-selector>
</template>

<script>
import CategoryFilter from '@/components/search/filter/Category'
export default {
  name: 'CategorySelector',
  props: {
    value: {
      type: [Array],
      default: () => [],
    },
    name: {
      type: String,
      default: null,
    },
    categories: {
      type: [Array],
      default: () => [],
    },
  },
  data() {
    return {
      CategoryFilter,
    }
  },
  methods: {
    selectCategory(value) {
      this.$emit('input', value)
    },
  },
}
</script>
