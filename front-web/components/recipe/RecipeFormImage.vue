<template>
  <div
    class="recipe-image-container"
  >
    <recipe-image
      class="recipe-image-edition"
      v-bind="$attrs"
      width="100%"
      :src="src"
    />
    <a-button color="white" text icon="fa-solid fa-edit" class="recipe-image-edit-button" @click="editImage" />
  </div>
</template>

<script>
import mixin from '@/utils/mixins/global'

export default {
  name: 'RecipeCardImage',
  mixins: [mixin],
  props: {
    src: {
      type: String,
      default: ''
    }
  },
  methods: {
    editImage () {
      this.$modal.show('recipe-picture-edit-modal')
    }
  }
}
</script>

<style scoped>
.recipe-image-edition {
  filter: brightness(70%);
  padding: 0;
}
.recipe-image-edit-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.recipe-image-container {
  position: relative;
}
</style>
