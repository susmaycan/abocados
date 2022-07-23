<template>
  <home-logged v-if="loggedIn" :recipes="recipes" :categories="categories" />
  <home-guest v-else />
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Homepage',
  data () {
    return {
      recipes: [],
      categories: []
    }
  },
  computed: {
    ...mapState('user', ['loggedIn'])
  },
  mounted () {
    if (this.loggedIn) {
      this.getData()
    }
  },
  methods: {
    async getData () {
      const data = await this.$api.recipe.list({ limit: 4 })
      this.recipes = data.results

      const response = await this.$api.category.list({ limit: 10 })
      this.categories = response.results
    }
  }
}
</script>
