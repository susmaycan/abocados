<template>
  <v-navigation-drawer
    v-model="drawer"
    fixed
    bottom
    temporary
    class="a-drawer"
    :disable-route-watcher="true"
    @input="onInput"
    width="50%"
  >
    <slot />
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'ADrawer',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      drawer: false
    }
  },
  watch: {
    show () {
      this.drawer = this.show
    }
  },
  mounted () {
    this.drawer = this.show
  },
  methods: {
    onInput (value) {
      this.$emit('change', value)
    }
  }
}
</script>
<style scoped>
.a-drawer {
  bottom: 0;
}
</style>
