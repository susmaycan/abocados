<template>
  <v-toolbar flat class="d-none d-md-block">
    <v-toolbar-title class="clickable" @click="onClick('index')">
      <div class="d-flex align-center">
        <app-logo width="40" height="50" /> <span class="font-weight-bold">{{ $t('app_name') }}</span>
      </div>
    </v-toolbar-title>
    <a-button
      v-for="item in itemsLeft"
      v-show="(item.logged && isLoggedIn) || (!item.logged && !isLoggedIn)"
      :key="item.title"
      class="mx-2"
      :icon="item.icon"
      text
      @click="onClick(item.path)"
    >
      {{ $t(item.title) | capitalize }}
    </a-button>
    <v-spacer />
    <a-button
      v-for="item in itemsRight"
      v-show="(item.logged && isLoggedIn) || (!item.logged && !isLoggedIn)"
      :key="item.title"
      class="mx-2"
      :icon="item.icon"
      text
      @click="onClick(item.path)"
    >
      {{ $t(item.title) | capitalize }}
    </a-button>
  </v-toolbar>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      sidebar: false,
      itemsRight: [
        { title: 'login', path: 'login', icon: 'fa-solid fa-arrow-right-to-bracket', logged: false },
        { title: 'register', path: 'register', icon: 'fa-solid fa-user-plus', logged: false },
        { title: 'recipe_book', path: 'recipes', icon: 'fa-solid fa-bookmark', logged: true },
        { title: 'account', path: 'account', icon: 'fa-solid fa-user', logged: true }
      ],
      itemsLeft: [
        { title: 'search_recipes', path: 'search', icon: 'fa-solid fa-magnifying-glass', logged: true }
      ]
    }
  },
  computed: {
    isLoggedIn () {
      return this.$store.state.user.loggedIn
    }
  },
  methods: {
    onClick (path) {
      this.$router.push({ name: path })
    }
  }
}
</script>
