<template>
  <component :is="layoutComponent" :title="title" :back="back" :menu="menu">
    <slot slot="title" name="title" />
    <slot slot="menu" name="menu" />
    <slot slot="top-bar" name="top-bar" />
    <slot slot="buttons" name="buttons" />
    <slot slot="filters" name="filters" />
    <slot />
    <slot slot="footer" name="footer" />
  </component>
</template>
<script>
import MobileLayout from './MobileLayout.vue'
import DesktopLayout from './DesktopLayout.vue'
export default {
  name: 'PageLayout',
  props: {
    title: {
      type: String,
      required: false,
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
  computed: {
    layoutComponent () {
      return this.$device.isMobile ? MobileLayout : DesktopLayout
    }
  }
}
</script>
