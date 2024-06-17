<template>
  <div class="form-image-container">
    <component
      :is="imageComponent"
      class="form-image-edition"
      :src="imageUrl"
      v-bind="$attrs"
    />
    <form-file-input
      class="form-image-edit-button"
      :value="formImage"
      :error-messages="errors"
      hide-input
      icon-left="fa-solid fa-edit"
      accept="image/*"
      @input="submitImage"
    />
  </div>
</template>

<script>
import RecipeImage from '@/components/recipe/Image'
import UserImage from '@/components/user/Image'

export default {
  name: 'FormImage',
  props: {
    image: null,
    errors: {
      type: String,
      default: null,
    },
    type: {
      type: String,
      default: 'recipe',
    },
  },
  data() {
    return {
      formImage: null,
    }
  },
  computed: {
    imageUrl() {
      if (!this.formImage) {
        return null
      }
      if (typeof this.formImage === 'string') {
        return this.formImage
      }
      return URL.createObjectURL(this.formImage)
    },
    imageComponent() {
      return this.type === 'recipe' ? RecipeImage : UserImage
    },
  },
  watch: {
    image() {
      this.formImage = this.image
    },
  },
  mounted() {
    this.formImage = this.image
  },
  methods: {
    submitImage(event) {
      this.formImage = event
      this.$emit('input', event)
    },
  },
}
</script>

<style scoped>
.form-image-edition {
  filter: brightness(70%);
  padding: 0;
}
.form-image-edit-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.form-image-container {
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
