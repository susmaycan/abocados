<template>
  <a-button
    v-if="favourite"
    fab
    v-bind="$attrs"
    icon="fa-solid fa-heart"
    class="favourite-recipe-button"
    @click="deleteFavourite"
  />
  <a-button
    v-else
    fab
    v-bind="$attrs"
    icon="fa-regular fa-heart"
    class="favourite-recipe-button"
    @click="addFavourite"
  />
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'RecipeCardFavourite',
  props: {
    id: {
      type: Number,
      default: null
    },
    favourite: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    ...mapState('user', ['user'])
  },
  methods: {
    addFavourite () {
      this.$api.favourite.add(this.user.id, { recipe: this.id })
      this.$emit('refresh', true)
    },
    deleteFavourite () {
      this.$api.favourite.delete(this.user.id, { recipe: this.id })
      this.$emit('refresh', false)
    }
  }

}
</script>
