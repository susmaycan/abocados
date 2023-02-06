<template>
  <search-selector
    :value="value"
    @input="selectDuration"
    :filter-list="durationList"
    :component="DurationFilter"
  >
    <template #label>
      <a-label>{{ $t('duration') | capitalize }}:</a-label>
      <span>{{ $t('min') | uppercase }}</span>
    </template>
  </search-selector>
</template>

<script>
import DurationFilter from '@/components/search/filter/Duration'
export default {
  name: 'DurationFilter',
  props: {
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      durationList: ['10', '15', '30', '45', '60'],
      DurationFilter,
    }
  },
  methods: {
    selectDuration(value) {
      this.$emit('input', value)
    },
  },
}
</script>
