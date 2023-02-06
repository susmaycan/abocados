<template>
  <div v-if="selectedDay" class="d-flex justify-end align-center">
    <a-button
      fab
      icon="fa-solid fa-circle-left"
      :class="previousButtonClass"
      @click="onPreviousDay"
    />
    <vertical-scroll-container class="meal-week">
      <meal-week-day
        v-for="day in week"
        :key="day.key"
        :day="day"
        :selected="day.time === selectedDay.time"
        @click="selectDay"
      />
    </vertical-scroll-container>
    <a-button
      fab
      icon="fa-solid fa-circle-right"
      :class="nextButtonClass"
      @click="onNextDay"
    />
  </div>
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
    previousButtonClass() {
      return {
        'pagination-button': !this.$device.isMobile,
        'pagination-button-mobile': this.$device.isMobile,
        previous: this.$device.isMobile,
      }
    },
    nextButtonClass() {
      return {
        'pagination-button': !this.$device.isMobile,
        'pagination-button-mobile': this.$device.isMobile,
        next: this.$device.isMobile,
      }
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
<style scoped>
.pagination-button {
  font-size: 40px;
}
.pagination-button-mobile {
  font-size: 20px;
  position: absolute;
}
.previous {
  left: 5px;
}
.next {
  right: 5px;
}
.meal-week {
  margin: 0 20px;
}
</style>
