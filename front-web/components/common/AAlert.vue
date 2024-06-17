<template>
  <v-alert
    text
    class="font-weight-bold text-left"
    v-bind="$attrs"
  >
    <slot />
  </v-alert>
</template>

<script>
export default {
  name: 'AAlert'
}
</script>
