<template>
  <div
    class="category-pill clickable"
    @click="goToDetail()"
  >
    <a-image :src="category.picture" height="50" width="50" />
    <div class="category-pill-title-div">
      <p class="category-pill-title">
        {{ category.name | capitalize }}
      </p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Category',
  props: {
    category: {
      type: Object,
      required: true
    }
  },
  methods: {
    goToDetail () {
      this.$emit('click', this.category.id)
    }
  }
}
</script>

<style scoped>
.category-pill {
    width: 120px;
    height: 120px;
    margin: 1em;
    border-radius: 10%;
    padding: 1em;
    border: 1px solid black;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.category-pill:hover {
    border: 2px solid black;
}
.category-pill-title-div {
    text-align: center;
    margin-top: .5em;
}
.category-pill-title {
  font-weight: bold;
  margin-bottom: 0;
}
</style>
