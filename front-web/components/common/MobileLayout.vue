<template>
  <div>
    <div class="d-flex justify-space-between align-center my-2">
      <a-button
        v-if="back"
        class="top-menu-buttons"
        text
        icon="fa-solid fa-arrow-left"
        @click="goBack"
      />
      <v-menu v-if="menu" v-model="openMenu">
        <template #activator="{ on }">
          <a-button
            text
            icon="fa-solid fa-ellipsis-vertical"
            class="top-menu-buttons"
            :on="on"
          />
        </template>
        <div class="menu">
          <slot name="menu" />
        </div>
      </v-menu>
      <slot name="top-bar" />
    </div>
    <div class="mobile-container">
      <slot name="title">
        <a-title>{{ title | capitalize }}</a-title>
      </slot>
      <slot name="filters" />
      <div v-if="loading">
        <loader />
      </div>
      <div v-show="!loading" class="mobile-content">
        <slot />
      </div>
    </div>
    <slot name="footer" />
  </div>
</template>
<script>
import { mapState } from 'vuex'
import AButton from './AButton.vue'

export default {
  name: 'MobileLayout',
  components: { AButton },
  props: {
    title: {
      type: String,
      default: ''
    },
    back: {
      type: Boolean,
      default: true
    },
    menu: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      openMenu: false
    }
  },
  computed: {
    ...mapState(['loading'])
  },
  methods: {
    goBack () {
      if (window.history.length > 0) {
        this.$router.go(-1)
      } else {
        this.$router.replace({ name: 'index' })
      }
    }
  }
}
</script>
<style scoped>
.mobile-container {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow-x: hidden;
  padding: 0;
  margin-bottom: 50px;
  z-index: 100;
  /* height: 85vh; */
}
.mobile-content {
  width: 90%;
}
.menu {
  z-index: 1000;
}
.top-menu-buttons {
  font-size: 20px;
}
</style>
