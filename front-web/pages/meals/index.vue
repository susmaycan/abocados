<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-bookmark" />
        {{ $t('meals') | capitalize }}
      </a-title>
    </template>
    <meal-list
      :selected-day="selectedDay"
      :selected-meal="selectedMeal"
      @edit="editMeal"
      @add="addMeal"
      @delete="deleteMeal"
      @select="selectDay"
    />
  </page-layout>
</template>
<script>
import RouteMixin from '@/mixins/route'
import { getDate, outputDate } from '@/utils/functions'

export default {
  name: 'MealPage',
  mixins: [RouteMixin],
  middleware: ['auth-custom'],
  data() {
    return {
      selectedDay: null,
      selectedMeal: null,
    }
  },
  mounted() {
    const queryDate = this.$route?.query?.date
    const today =
      queryDate && !isNaN(new Date(queryDate).getTime())
        ? new Date(queryDate)
        : new Date()
    this.selectedDay = getDate(
      new Date(today.getFullYear(), today.getMonth(), today.getDate())
    )
    this.getData()
  },
  methods: {
    async getData() {
      const data = await this.$api.meal.list({
        date: outputDate(this.selectedDay.date),
      })
      this.selectedMeal = data.count > 0 ? data.results[0] : null
      this.updateDateQueryParam()
    },
    addMeal() {
      this.$router.push({
        name: 'meals-add',
        query: { date: outputDate(this.selectedDay.date) },
      })
    },
    editMeal(mealId) {
      this.$router.push({ name: 'meals-edit-id', params: { id: mealId } })
    },
    async deleteMeal() {
      await this.$api.meal.delete(this.selectedMeal.id)
      this.getData()
    },
    selectDay(date) {
      this.selectedDay = getDate(date)
      this.getData()
    },
    updateDateQueryParam() {
      const { name } = this.$route

      this.$router
        .replace({
          name,
          query: { date: outputDate(this.selectedDay.date) },
        })
        .catch(() => {})
    },
  },
}
</script>
