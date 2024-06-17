<template>
  <v-badge
    v-bind="$attrs"
    :value="show"
    :content="count"
    overlap
  >
    <slot />
  </v-badge>
</template>

<script>
export default {
  name: 'ABadge',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    count: {
      type: Number,
      default: null
    }
  }
}
</script>
