<template>
  <div class="text-left">
    <div class="d-flex justify-space-between align-center">
      <slot name="label" />
    </div>
    <vertical-scroll-container class="py-3">
      <div
        v-for="filter in filterList"
        :key="isObjectFilter ? filter.id : filter"
      >
        <search-selector-container
          :selected="isSelected(filter)"
          @click="selectValue(filter)"
        >
          <component :is="component" :filter="filter" />
        </search-selector-container>
      </div>
    </vertical-scroll-container>
  </div>
</template>

<script>
export default {
  props: {
    selected: {
      type: Boolean,
      default: false,
    },
    filterList: {
      type: Array,
      default: () => [],
    },
    value: {
      type: [String, Number, Array],
      default: null,
    },
    component: null,
  },
  computed: {
    isObjectFilter() {
      if (this.filterList.length > 0) {
        const possibleObject = this.filterList[0]
        return (
          typeof possibleObject === 'object' &&
          !Array.isArray(possibleObject) &&
          possibleObject !== null
        )
      }
      return false
    },
  },
  methods: {
    isSelected(selectedValue) {
      if (Array.isArray(this.value)) {
        return this.value.includes(selectedValue.id)
      }
      return this.value === selectedValue
    },
    selectValue(value) {
      let inputValue = this.isSelected(value) ? null : value

      if (Array.isArray(this.value)) {
        const elementExists = this.value.find((element) => element === value.id)
        if (elementExists) {
          inputValue = this.value.filter((element) => element !== value.id)
        } else {
          inputValue = [...this.value, value.id]
        }
      }

      this.$emit('input', inputValue)
    },
  },
}
</script>
