<template>
  <h2 class="a-subtitle">
    <slot />
  </h2>
</template>

<script>
export default {
  name: 'ATitle'
}
</script>
<style scoped>
.a-subtitle {
  font-family: 'Poppins', 'Roboto';
}
</style>
