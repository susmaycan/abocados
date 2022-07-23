<template>
  <a-select
    :value="selectedRating"
    :errors="errors"
    :items="ratingList"
    :label="$t('rating')"
    item-text="name"
    item-value="id"
    v-bind="$attrs"
    @input="onInput"
  />
</template>

<script>
export default {
  name: 'RatingSelector',
  props: {
    errors: {
      type: [String, Array],
      default () { return [] }
    },
    initialValue: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      ratingList: [
        { name: '1 ⭐️', id: '1' },
        { name: '2 ⭐️⭐️', id: '2' },
        { name: '3 ⭐️⭐️⭐️', id: '3' },
        { name: '4 ⭐️⭐️⭐️⭐️', id: '4' },
        { name: '5 ⭐️⭐️⭐️⭐️⭐️', id: '5' }
      ],
      selectedRating: null
    }
  },
  watch: {
    initialValue () {
      this.selectedRating = this.initialValue
    }
  },
  mounted () {
    this.selectedRating = this.initialValue
  },
  methods: {
    onInput (value) {
      let finalValue = value
      if (value === undefined || value === null) {
        finalValue = ''
      }
      this.selectedRating = finalValue
      this.$emit('input', this.selectedRating)
    }
  }

}
</script>
