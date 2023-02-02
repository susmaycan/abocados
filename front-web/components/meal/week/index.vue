<template>
  <vertical-scroll-container v-if="selectedDay" class="align-center">
    <a-button
      text
      icon="fa-solid fa-circle-left"
      class="pagination-button"
      @click="onPreviousDay"
    />
    <meal-week-day
      v-for="day in week"
      :key="day.key"
      :day="day"
      :selected="day.time === selectedDay.time"
      @click="selectDay"
    />
    <a-button
      text
      icon="fa-solid fa-circle-right"
      class="pagination-button"
      @click="onNextDay"
    />
  </vertical-scroll-container>
</template>
<script>
import { getDate } from '@/utils/functions'

export default {
  name: 'MealWeek',
  props: {
    selectedDay: {
      type: [Object],
      default: null,
    },
  },
  computed: {
    week() {
      const weekArray = []
      const today = this.selectedDay
      for (let i = 0; i < 7; i++) {
        const day = getDate(
          new Date(today.year, today.date.getMonth(), today.day + i)
        )
        weekArray.push(day)
      }
      return weekArray
    },
  },
  methods: {
    selectDay(date) {
      this.$emit('select', date)
    },
    onPreviousDay() {
      const newDate = new Date(
        this.selectedDay.year,
        this.selectedDay.date.getMonth(),
        this.selectedDay.day - 1
      )
      this.$emit('select', newDate)
    },
    onNextDay() {
      const newDate = new Date(
        this.selectedDay.year,
        this.selectedDay.date.getMonth(),
        this.selectedDay.day + 1
      )
      this.$emit('select', newDate)
    },
  },
}
</script>
