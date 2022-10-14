<template>
  <page-layout :back="false">
    <template #title>
      <a-title>
        <a-icon name="fa-solid fa-bookmark" />
        {{ $t('meals') | capitalize }}
      </a-title>
    </template>
    <vertical-scroll-container v-if="selectedDay" class="align-center">
      <a-button
        text
        icon="fa-solid fa-circle-left"
        class="pagination-button"
        @click="onPreviousWeek()"
      />
      <div v-for="day in week" :key="day.key" :class="day.time === selectedDay.time ? 'week-day-selected' : 'week-day'" @click="selectDay(day.date)">
        <p>{{ $t(day.weekDayShort) | capitalize }}</p>
        <p>{{ day.day }}</p>
      </div>
      <a-button
        text
        icon="fa-solid fa-circle-right"
        class="pagination-button"
        @click="onNextWeek()"
      />
    </vertical-scroll-container>
    <div v-if="selectedDay" class="d-flex align-center justify-space-between my-2 text-left">
      <a-subtitle>
        {{ $t(selectedDay.weekDay) | capitalize }}, {{ selectedDay.day }} {{ $t(selectedDay.monthText) | capitalize }}
      </a-subtitle>
      <a-button
        v-if="!selectedMeal"
        icon="fa-solid fa-circle-plus"
        color="primary"
        fab
        small
        @click="addMeal"
      />
      <div v-else class="d-flex">
        <a-button
          icon="fa-solid fa-pen"
          color="primary"
          fab
          small
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
    <div v-if="selectedMeal" class="text-left">
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
    <p v-else>
      {{ $t('no_meal_for_day') }}
    </p>
  </page-layout>
</template>
<script>
import { mapState } from 'vuex'
import ASubtitle from '../../components/common/ASubtitle.vue'
import RouteMixin from '@/utils/mixins/route'
import { getDate, outputDate } from '@/utils/functions'

export default {
  name: 'MealList',
  components: { ASubtitle },
  mixins: [RouteMixin],
  middleware: ['auth-custom'],
  data () {
    return {
      selectedDay: null,
      selectedMeal: null
    }
  },
  computed: {
    ...mapState('user', ['user']),
    week () {
      const weekArray = []
      const today = this.selectedDay
      for (let i = 0; i < 7; i++) {
        const day = getDate(new Date(today.year, today.date.getMonth(), today.day + i))
        weekArray.push(day)
      }
      return weekArray
    }
  },
  mounted () {
    const today = new Date()
    this.selectedDay = getDate(new Date(today.getFullYear(), today.getMonth(), today.getDate()))
    this.getData()
  },
  methods: {
    async getData () {
      const data = await this.$api.meal.list({ date: outputDate(this.selectedDay.date) })
      this.selectedMeal = data.count > 0 ? data.results[0] : null
    },
    addMeal () {
      this.$router.push({ name: 'meals-add', query: { date: outputDate(this.selectedDay.date) } })
    },
    editMeal (mealId) {
      this.$router.push({ name: 'meals-edit-id', params: { id: mealId } })
    },
    deleteMeal () {
      this.$modal.show('delete-meal')
    },
    async onAcceptDelete () {
      await this.$api.meal.delete(this.selectedMeal.id)
      this.getData()
    },
    selectDay (date) {
      this.selectedDay = getDate(date)
      this.getData()
    },
    onPreviousWeek () {
      this.selectedDay = getDate(new Date(this.selectedDay.year, this.selectedDay.date.getMonth(), this.selectedDay.day - 1))
      this.getData()
    },
    onNextWeek () {
      this.selectedDay = getDate(new Date(this.selectedDay.year, this.selectedDay.date.getMonth(), this.selectedDay.day + 1))
      this.getData()
    },
    isToday (date) {
      return date.time === this.selectedDay.time
    }
  }
}
</script>
<style scoped>
.week-day {
  border: 1px solid var(--v-secondary-base);
  padding: 1em;
  margin: .5em;
  border-radius: 10px;
}
.week-day:hover {
  border: 1px solid var(--v-secondary-base);
  background: var(--v-secondary-base);
  color: white;
  cursor: pointer;
}
.week-day-selected {
  border: 1px solid var(--v-secondary-base);
  background: var(--v-secondary-base);
  color: white;
  padding: 1em;
  margin: .5em;
  border-radius: 10px;
}

</style>
