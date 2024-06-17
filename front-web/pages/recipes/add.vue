<template>
  <page-layout :title="$t('add_recipe')">
    <recipe-form :errors="errors" @submit="onSubmit" />
  </page-layout>
</template>
<script>
import { SAVE_TYPE } from '@/utils/consts'

export default {
  name: 'AddRecipe',
  middleware: ['auth-custom'],
  data () {
    return {
      errors: null
    }
  },
  methods: {
    onSubmit (form, saveType) {
      this.$api.recipe
        .create(form)
        .then((data) => {
          if (data.id) {
            const route =
              saveType === SAVE_TYPE.SAVE
                ? { name: 'recipes-id', params: { id: data.id } }
                : { name: 'recipes-add' }
            this.$router.replace(route)
          }
        })
        .catch((errors) => {
          this.errors = errors
        })
    }
  }
}
</script>
