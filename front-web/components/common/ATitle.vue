<template>
  <h1 class="a-title">
    <slot />
  </h1>
</template>

<script>
export default {
  name: 'ATitle'
}
</script>
<style scoped>
.a-title {
  font-family: 'Poppins', 'Roboto';
}
</style>
