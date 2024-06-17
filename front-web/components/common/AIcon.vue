<template>
  <span>
    <font-awesome-icon :icon="name" />
  </span>
</template>

<script>
export default {
  name: 'AIcon',
  props: {
    name: {
      type: String,
      default: ''
    }
  }
}
</script>
