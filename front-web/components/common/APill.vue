<template>
  <v-chip v-bind="$attrs" @click:close="$emit('close')">
    <slot />
  </v-chip>
</template>

<script>
export default {
  name: 'APill'
}
</script>
