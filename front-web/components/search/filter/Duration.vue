<template>
  <span>
    {{ filter | capitalize }}
    <a-icon name="fa-solid fa-clock" />
  </span>
</template>

<script>
export default {
  name: 'DurationFilter',
  props: {
    filter: {
      type: String,
      default: null,
    },
  },
}
</script>
