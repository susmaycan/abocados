<template>
  <div
    :class="{ 'week-day-selected': selected, 'week-day': true }"
    @click="onClick(day.date)"
  >
    <span>{{ $t(day.weekDayShort) | capitalize }}</span>
    <span class="day">
      {{ day.day }}
    </span>
    <span>{{ day.monthText | capitalize }}</span>
  </div>
</template>
<script>
export default {
  name: 'MealDay',
  props: {
    day: {
      type: Object,
      default: null,
    },
    selected: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    onClick(date) {
      this.$emit('click', date)
    },
  },
}
</script>
<style scoped>
.week-day {
  border: 1px solid var(--v-secondary-base);
  padding: 1em;
  margin: 0.5em;
  border-radius: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
}
.day {
  font-size: 20px;
  font-weight: 900;
}
.week-day:hover {
  border: 1px solid var(--v-secondary-base);
  background: var(--v-secondary-base);
  color: white;
  cursor: pointer;
}
.week-day-selected {
  background: var(--v-secondary-base);
  color: white;
}
</style>
