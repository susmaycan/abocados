<script setup lang="ts">
const { initUserConfig } = useUserConfig()
const { initAuthentication } = useAuth()

onBeforeMount(() => {
  initAuthentication()
  initUserConfig()
})
</script>

<template>
  <div class="m-3">
    <top-bar />
    <div class="flex items-center">
      <!-- <side-bar /> -->
      <slot />
    </div>
  </div>
</template>
