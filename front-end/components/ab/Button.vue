<script setup lang="ts">
defineProps<{
  icon?: string
  color?: string
  variant?: 'link' | 'solid' | 'ghost' | 'outline' | 'soft'
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  ariaLabel?: string
  leftIcon?: string
  rightIcon?: string
}>()

const emits = defineEmits(['click'])
</script>

<template>
  <u-button
    :aria-label="ariaLabel"
    :color="color || 'primary'"
    :icon="icon"
    :leading-icon="leftIcon"
    :size="size"
    :trailing-icon="rightIcon"
    :variant="variant || 'outline'"
    @click="emits('click')"
  >
    <slot />
  </u-button>
</template>
