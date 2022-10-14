<template>
  <page-layout :title="$t('edit_meal')">
    <meal-form
      :errors="errors"
      :meal="meal"
      :global-error="globalError"
      :edit="true"
      @submit=" onSubmit"
    />
  </page-layout>
</template>
<script>
import mixin from '@/utils/mixins/global'

export default {
  name: 'EditMeal',
  mixins: [mixin],
  middleware: ['auth-custom'],
  data () {
    return {
      errors: {},
      globalError: null,
      meal: null
    }
  },
  computed: {
    mealId () {
      return this.$route.params.id
    }
  },
  async mounted () {
    if (this.mealId) {
      const meal = await this.$api.meal.findOne(this.mealId)
      if (!this.isCreator(meal)) {
        this.$router.replace({ name: 'index' })
      }
      this.meal = meal
    }
  },
  methods: {
    onSubmit (form) {
      this.$api.meal.update(this.meal.id, form)
        .then((data) => {
          if (data.id) {
            this.$router.replace({ name: 'meals', query: { date: data.date } })
          }
        })
        .catch((response) => {
          this.globalError = response?.data?.message
          this.errors = response?.data
        })
    }
  }
}

</script>
