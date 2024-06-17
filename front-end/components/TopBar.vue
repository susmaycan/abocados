<script setup lang="ts">
const links = [
  {
    label: 'Profile',
    avatar: {
      src: 'https://avatars.githubusercontent.com/u/739984?v=4',
    },
    badge: 100,
  },
  {
    label: 'Installation',
    icon: 'i-heroicons-home',
    to: '/getting-started/installation',
  },
  {
    label: 'Vertical Navigation',
    icon: 'i-heroicons-chart-bar',
    to: '/components/command-palette',
  },
  {
    label: 'Command Palette',
    icon: 'i-heroicons-command-line',
    to: '/components/command-palette',
  },
]
</script>

<template>
  <div class="flex items-center">
    <div>abocados</div>
    <div class="ml-auto">
      <theme-switcher />
    </div>
  </div>
</template>
