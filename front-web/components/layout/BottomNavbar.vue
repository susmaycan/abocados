<template>
  <v-bottom-navigation
    v-model="value"
    class="bottom-nav"
    fixed
    color="primary"
  >
    <a-button
      v-for="item in items"
      :key="item.title"
      :value="item.title"
      class="mx-1 bottom-nav-item-button"
      :icon="item.icon"
      text
      @click="onClick(item.path)"
    />
  </v-bottom-navigation>
</template>

<script>
import { mapState } from 'vuex'

const PATH_LIST = {
  INDEX: 'index',
  SEARCH: 'search',
  RECIPES: 'recipes',
  ACCOUNT: 'account'
}

export default {
  name: 'BottomNavbar',
  data () {
    return {
      value: 'home',
      items: [
        {
          title: 'home',
          path: PATH_LIST.INDEX,
          icon: 'fa-solid fa-home',
          logged: true
        },
        {
          title: 'search_recipes',
          path: PATH_LIST.SEARCH,
          icon: 'fa-solid fa-magnifying-glass',
          logged: true
        },
        {
          title: 'recipe_book',
          path: PATH_LIST.RECIPES,
          icon: 'fa-solid fa-bookmark',
          logged: true
        },
        {
          title: 'account',
          path: PATH_LIST.ACCOUNT,
          icon: 'fa-solid fa-user',
          logged: true
        }
      ]
    }
  },
  computed: {
    ...mapState('user', ['loggedIn'])
  },
  mounted () {
    const currentItem = this.items.find(item => item.path === this.$route.name)
    this.value = currentItem ? currentItem.title : 'home'
  },
  methods: {
    onClick (path) {
      this.$router.push({ name: path })
    }
  }
}
</script>
<style scoped>
.bottom-nav-item-button {
  font-size: 1em !important;
}
</style>
