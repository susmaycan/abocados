<template>
  <page-layout :title="$t('add_meal')">
    <meal-form
      :errors="errors"
      :date="date"
      :global-error="globalError"
      @submit=" onSubmit"
    />
  </page-layout>
</template>
<script>
export default {
  name: 'AddMeal',
  middleware: ['auth-custom'],
  data () {
    return {
      errors: {},
      globalError: null,
      date: null
    }
  },
  mounted () {
    const queryDate = this.$route?.query?.date
    if (queryDate && !isNaN(new Date(queryDate).getTime())) {
      this.date = queryDate
    }
  },
  methods: {
    onSubmit (form) {
      this.$api.meal.create(form)
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
