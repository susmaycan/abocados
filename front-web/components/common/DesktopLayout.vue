<template>
  <div>
    <div class="d-flex justify-space-between">
      <div class="d-flex flex-column justify-start ">
        <slot name="title">
          <a-title>{{ title | capitalize }}</a-title>
        </slot>
      </div>
      <slot name="buttons" />
    </div>
    <slot name="filters" />
    <div v-if="loading">
      <loader />
    </div>
    <div v-show="!loading">
      <slot />
    </div>
    <slot name="footer" />
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  name: 'DesktopLayout',
  props: {
    title: {
      type: String,
      default: ''
    }
  },
  computed: {
    ...mapState(['loading'])
  }
}
</script>
