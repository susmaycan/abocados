<template>
  <Recipe :recipe="recipe" />
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class RecipeComponent extends Vue {
    private recipe: object = {}

    retrieveRecipe() {
      let id: string = this.$route.params.id
      RecipesAPI.get(id)
        .then((response) => {
          this.recipe = response.data
          console.log(response.data)
        })
        .catch((e) => {
          console.log(e)
        })
    }

    mounted() {
      this.retrieveRecipe()
    }
  }
</script>
