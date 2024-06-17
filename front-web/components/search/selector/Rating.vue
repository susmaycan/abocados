<template>
  <search-selector
    :value="value"
    @input="selectRating"
    :filter-list="ratingList"
    :component="RatingFilter"
  >
    <template #label>
      <a-label>{{ $t('rating') | capitalize }}:</a-label>
    </template>
  </search-selector>
</template>

<script>
import RatingFilter from '@/components/search/filter/Rating'
export default {
  name: 'RatingFilter',
  props: {
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      ratingList: ['1', '2', '3', '4', '5'],
      RatingFilter,
    }
  },
  methods: {
    selectRating(value) {
      this.$emit('input', value)
    },
  },
}
</script>
