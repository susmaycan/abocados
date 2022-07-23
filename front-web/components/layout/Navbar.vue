<template>
  <v-toolbar flat>
    <v-toolbar-title class="clickable" @click="onClick('index')">
      <div class="d-flex align-center">
        <app-logo width="40" height="50" />
        <span class="font-weight-bold">{{ $t("app_name") }}</span>
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
    <v-menu v-if="isLoggedIn" v-model="openMenu" offset-y>
      <template #activator="{ on }">
        <a-button text class="p-2" :on="on">
          <v-avatar color="primary" size="30" class="mr-1">
            <a-image :src="user.picture" />
          </v-avatar>
          <a-icon v-if="openMenu" name="fa-solid fa-angle-up" class="ml-1" />
          <a-icon v-else name="fa-solid fa-angle-down" class="ml-1" />
        </a-button>
      </template>
      <v-list class="p-1" :width="250">
        <v-list-item
          v-for="item in dropdownItems"
          :key="item.title"
          class="px-3"
          @click="onClick(item.path)"
        >
          <v-list-item-title>
            <a-icon :name="item.icon" class="mr-2" />
            {{ $t(item.title) | capitalize }}
          </v-list-item-title>
        </v-list-item>
        <v-divider />
        <v-list-item @click="onLogOut">
          <v-list-item-title>
            <a-icon name="fa-solid fa-right-from-bracket" class="mr-2" />
            {{ $t("logout") | capitalize }}
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Navbar",
  data() {
    return {
      sidebar: false,
      itemsRight: [
        {
          title: "login",
          path: "login",
          icon: "fa-solid fa-arrow-right-to-bracket",
          logged: false,
        },
        {
          title: "register",
          path: "register",
          icon: "fa-solid fa-user-plus",
          logged: false,
        },
        {
          title: "recipe_book",
          path: "recipes",
          icon: "fa-solid fa-bookmark",
          logged: true,
        },
      ],
      itemsLeft: [
        {
          title: "search_recipes",
          path: "search",
          icon: "fa-solid fa-magnifying-glass",
          logged: true,
        },
      ],
      dropdownItems: [
        {
          title: "profile",
          path: "account",
          icon: "fa-solid fa-user",
          logged: true,
        },
        {
          title: "settings",
          path: "account-settings",
          icon: "fa-solid fa-gear",
          logged: true,
        },
      ],
      openMenu: false,
    };
  },
  computed: {
    ...mapState("user", ["user"]),
    isLoggedIn() {
      return this.$store.state.user.loggedIn;
    },
  },
  methods: {
    onClick(path) {
      this.$router.push({ name: path });
    },
    onLogOut() {
      this.$store.commit("user/removeUser");
      this.$router.push({ name: "index" });
    },
  },
};
</script>
