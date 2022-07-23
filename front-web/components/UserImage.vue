<template>
  <div v-if="edition" class="user-image-container">
    <a-image
      class="user-image user-image-edition"
      v-bind="$attrs"
      :src="source"
    />
    <a-button color="white" text icon="fa-solid fa-edit" class="user-image-edit-button" @click="editImage" />
  </div>
  <a-image
    v-else
    class="user-image"
    v-bind="$attrs"
    :src="source"
  />
</template>

<script>
export default {
  name: 'UserImage',
  props: {
    src: {
      type: String,
      required: false,
      default: null
    },
    id: {
      type: Number,
      default: null
    },
    edition: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    source () {
      return this.src ||
      `https://avatars.dicebear.com/api/adventurer-neutral/${this.id}.svg`
    }
  },
  methods: {
    editImage () {
      this.$modal.show('user-picture-edit-modal')
    }
  }
}
</script>

<style scoped>
.user-image {
  border-radius: 50%;
}
.user-image-edition {
  filter: brightness(70%);
  padding: 0;
}
.user-image-edit-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.user-image-container {
  position: relative;
}
</style>
