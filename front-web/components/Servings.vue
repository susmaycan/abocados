<template>
  <p class="servings">
    <a-icon name="fa-solid fa-utensils" class="mr-1" />
    <span class="font-weight-bold">{{ servings }}</span>
    <span v-if="parsedIntServings == 1">
      {{ $t('serving') }}
    </span>
    <span v-else>
      {{ $t('servings') }}
    </span>
  </p>
</template>

<script>

export default {
  name: 'Servings',
  props: {
    servings: {
      type: String,
      required: true
    }
  },
  computed: {
    parsedIntServings () {
      return parseInt(this.servings)
    }
  }
}
</script>

<style scoped>
.servings {
  font-size: 20px;
}
</style>
