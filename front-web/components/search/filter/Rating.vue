<template>
  <span>
    {{ filter | capitalize }}
    <a-icon name="fa-solid fa-star" />
  </span>
</template>

<script>
export default {
  name: 'RatingFilter',
  props: {
    filter: {
      type: String,
      default: null,
    },
  },
}
</script>
