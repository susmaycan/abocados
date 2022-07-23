<template>
  <page-layout :title="$t('add_recipe')">
    <recipe-form
      :errors="errors"
      :global-error="globalError"
      @submit=" onSubmit"
    />
  </page-layout>
</template>
<script>
export default {
  name: 'AddRecipe',
  middleware: ['auth-custom'],
  data () {
    return {
      errors: {},
      globalError: null
    }
  },
  methods: {
    onSubmit (form) {
      this.$api.recipe.create(form)
        .then((data) => {
          if (data.id) {
            this.$router.replace({ name: 'recipes-id', params: { id: data.id } })
          }
        })
        .catch((response) => {
          this.globalError = response?.data?.message
          this.errors = response?.data
        })
    }
  }
}

</script>
