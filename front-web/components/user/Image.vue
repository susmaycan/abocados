<template>
  <a-image class="user-image" v-bind="$attrs" :src="source" />
</template>

<script>
export default {
  name: 'UserImage',
  props: {
    src: {
      type: String,
      required: false,
      default: null,
    },
  },
  computed: {
    source() {
      return (
        this.src ||
        `https://avatars.dicebear.com/api/adventurer-neutral/${this.id}.svg`
      )
    },
  },
}
</script>

<style scoped>
.user-image {
  border-radius: 50%;
}
</style>
