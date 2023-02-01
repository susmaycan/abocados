<template>
  <div class="text-left">
    <div class="d-flex justify-space-between align-center">
      <a-label>{{ $t('duration') | capitalize }}:</a-label>
      <span>{{ $t('min') | uppercase }}</span>
    </div>
    <vertical-scroll-container class="py-3">
      <div v-for="duration in durationList" :key="duration">
        <search-small-filter-container
          :selected="isSelected(duration)"
          @click="selectDuration(duration)"
        >
          <span>
            {{ duration | capitalize }}
            <a-icon name="fa-solid fa-clock" />
          </span>
        </search-small-filter-container>
      </div>
    </vertical-scroll-container>
  </div>
</template>

<script>
export default {
  name: 'DurationSearchSelector',
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
      durationList: ['10', '15', '30', '45', '60'],
    }
  },
  methods: {
    isSelected(selectedDuration) {
      return this.value === selectedDuration
    },
    selectDuration(value) {
      const inputValue = this.isSelected(value) ? null : value
      this.$emit('input', inputValue)
    },
  },
}
</script>
