<template>
  <page-layout :title="$t('edit_recipe')">
    <recipe-form :errors="errors" :data="recipe" @submit="onSubmit" />
  </page-layout>
</template>
<script>
import mixin from '@/mixins/global'

export default {
  name: 'EditRecipe',
  mixins: [mixin],
  middleware: ['auth-custom'],
  data() {
    return {
      errors: null,
      recipe: null,
    }
  },
  computed: {
    recipeId() {
      return this.$route.params.id
    },
  },
  async mounted() {
    if (this.recipeId) {
      const recipe = await this.$api.recipe.findOne(this.recipeId)
      if (!this.isCreator(recipe)) {
        this.$router.replace({ name: 'index' })
      }
      recipe.categories = recipe.categories.map((category) => category.id)

      this.recipe = recipe
    }
  },
  methods: {
    async onSubmit(form) {
      try {
        const response = await this.$api.recipe.update(this.recipeId, form)

        if (response.id) {
          this.$router.go(-1)
        }
      } catch (errors) {
        this.errors = errors
      }
    },
  },
}
</script>
