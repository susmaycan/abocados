<template>
  <div class="category">
    <a-image :src="filter.picture" height="30" width="30" />
    <span>{{ filter.name | capitalize }}</span>
  </div>
</template>

<script>
export default {
  name: 'CategoryFilter',
  props: {
    filter: {
      type: Object,
      required: true,
    },
  },
}
</script>
<style scoped>
.category {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
