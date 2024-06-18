<script setup lang="ts">
const { colorMode, setColorMode } = useUserConfig()
const isDark = computed(() => colorMode.value === EColorMode.dark)
</script>
<template>
  <client-only>
    <ab-button
      aria-label="Theme"
      color="gray"
      :icon="isDark ? 'i-heroicons-moon-20-solid' : 'i-heroicons-sun-20-solid'"
      variant="ghost"
      @click="setColorMode(isDark ? EColorMode.light : EColorMode.dark)"
    />
    <template #fallback>
      <div class="w-8 h-8" />
    </template>
  </client-only>
</template>
