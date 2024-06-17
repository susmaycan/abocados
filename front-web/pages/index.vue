<template>
  <home-logged v-if="isLoggedIn" :recipes="recipes" :categories="categories" />
  <home-guest v-else />
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Homepage',
  data() {
    return {
      recipes: [],
      categories: [],
    }
  },
  computed: {
    ...mapGetters('user', ['isLoggedIn']),
  },
  mounted() {
    if (this.isLoggedIn) {
      this.getData()
    }
  },
  methods: {
    async getData() {
      const data = await this.$api.recipe.list({ limit: 4 })
      this.recipes = data.results

      const response = await this.$api.category.list({ limit: 10 })
      this.categories = response.results
    },
  },
}
</script>
