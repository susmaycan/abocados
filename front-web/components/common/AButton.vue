<template>
  <v-btn
    :class="buttonClass"
    v-bind="$attrs"
    @click.stop="onClick()"
    v-on="on"
  >
    <a-icon v-if="icon" :name="icon" :class="iconClass" />
    <slot />
  </v-btn>
</template>

<script>
export default {
  name: 'AButton',
  props: {
    icon: {
      type: String,
      required: false,
      default: null
    },
    fullWidth: {
      type: Boolean,
      default: false
    },
    on: {
      type: Object,
      default: null
    }
  },
  computed: {
    iconClass () {
      return this.$slots.default ? 'mr-2' : ''
    },
    buttonClass () {
      let base = 'custom-button'
      if (this.fullWidth) { base += ' full-width' }
      return base
    }
  },
  methods: {
    onClick () {
      this.$emit('click')
    }
  }
}
</script>
<style scoped>
.custom-button {
  font-weight: 700;
}
.full-width {
  width: 100%;
}
</style>
