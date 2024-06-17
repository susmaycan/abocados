<template>
  <div class="d-flex align-start">
    <a-icon class="orange--text" name="fa-solid fa-star" />
    <span class="ml-1">
      {{ numberedRating }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'Rating',
  props: {
    rating: {
      type: String,
      required: false,
      default: null
    }
  },
  computed: {
    numberedRating () {

      return this.rating ? parseInt(this.rating) : 0
    }
  }
}
</script>
