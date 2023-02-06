<template>
  <div class="text-left">
    <a-label>{{ $t('rating') | capitalize }}:</a-label>
    <vertical-scroll-container class="py-3">
      <div v-for="rating in ratingList" :key="rating">
        <search-filter-container
          :selected="isSelected(rating)"
          @click="selectRating(rating)"
        >
          <span>
            {{ rating | capitalize }}
            <a-icon name="fa-solid fa-star" />
          </span>
        </search-filter-container>
      </div>
    </vertical-scroll-container>
  </div>
</template>

<script>
export default {
  name: 'RatingSearchSelector',
  props: {
    errors: {
      type: [String, Array],
      default() {
        return []
      },
    },
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      ratingList: ['1', '2', '3', '4', '5'],
    }
  },
  methods: {
    isSelected(selectedRating) {
      return this.value === selectedRating
    },
    selectRating(value) {
      const inputValue = this.isSelected(value) ? null : value
      this.$emit('input', inputValue)
    },
  },
}
</script>
