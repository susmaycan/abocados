<template>
  <div>
    <meal-week :selected-day="selectedDay" @select="selectDay" />
    <div
      v-if="selectedDay"
      class="d-flex align-center justify-start my-2 text-left"
    >
      <form-date-picker
        :only-icon="true"
        :value="calendarDate"
        @input="onCalendarDateChange"
      />
      <a-subtitle class="ml-3">
        {{ $t(selectedDay.weekDay) | capitalize }}, {{ selectedDay.day }}
        {{ $t(selectedDay.monthText) | capitalize }}
      </a-subtitle>
      <a-button
        class="ml-auto"
        v-if="!selectedMeal"
        icon="fa-solid fa-circle-plus"
        color="primary"
        fab
        small
        @click="addMeal"
      />
      <div v-else class="ml-auto d-flex">
        <a-button
          icon="fa-solid fa-pen"
          color="primary"
          fab
          small
          class="mr-2"
          @click="editMeal(selectedMeal.id)"
        />
        <a-button
          icon="fa-solid fa-trash"
          color="primary"
          fab
          small
          @click="deleteMeal(selectedMeal.id)"
        />
      </div>
    </div>
    <div v-if="selectedMeal" class="text-left my-5">
      <a-subtitle>{{ $t('breakfast') | capitalize }}</a-subtitle>
      <meal-recipe-list
        :recipe-list="selectedMeal.breakfast"
        :empty-message="$t('meal_empty_recipes_breakfast')"
      />

      <a-subtitle>{{ $t('lunch') | capitalize }}</a-subtitle>
      <meal-recipe-list
        :recipe-list="selectedMeal.lunch"
        :empty-message="$t('meal_empty_recipes_lunch')"
      />

      <a-subtitle>{{ $t('dinner') | capitalize }}</a-subtitle>
      <meal-recipe-list
        :recipe-list="selectedMeal.dinner"
        :empty-message="$t('meal_empty_recipes_dinner')"
      />

      <a-modal name="delete-meal" @accept="onAcceptDelete">
        <template #title>
          <a-subtitle>
            <a-icon name="fa-solid fa-triangle-exclamation" />
            {{ $t('delete_meal') | capitalize }}
          </a-subtitle>
        </template>
        <p>
          {{ $t('delete_meal_text') }}
        </p>
      </a-modal>
    </div>
    <p v-else class="mt-5">
      {{ $t('no_meal_for_day') }}
    </p>
  </div>
</template>
<script>
import { outputDate } from '@/utils/functions'

export default {
  name: 'MealList',
  props: {
    selectedDay: {
      type: [Object],
      default: null,
    },
    selectedMeal: {
      type: [Object],
      default: null,
    },
  },
  computed: {
    calendarDate() {
      return this.selectedDay ? outputDate(this.selectedDay.date) : null
    },
  },
  methods: {
    addMeal() {
      this.$emit('add')
    },
    editMeal(mealId) {
      this.$emit('edit', mealId)
    },
    deleteMeal() {
      this.$modal.show('delete-meal')
    },
    async onAcceptDelete() {
      this.$emit('delete', mealId)
    },
    selectDay(date) {
      this.$emit('select', date)
    },
    onCalendarDateChange(value) {
      if (value && !isNaN(new Date(value).getTime())) {
        const newDate = new Date(value)
        const newSelectedDate = new Date(
          newDate.getFullYear(),
          newDate.getMonth(),
          newDate.getDate()
        )
        this.$emit('select', newSelectedDate)
      }
    },
  },
}
</script>
