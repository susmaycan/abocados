<template>
  <RecipeList :recipes="recipeList"/>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class Recipes extends Vue {
    private recipeList: any[] = []

    retrieveRecipeList() {
      RecipesAPI.getAll()
        .then((response) => {
          this.recipeList = response.data
        })
        .catch((e) => {
          console.log(e)
        })
    }

    mounted() {
      this.retrieveRecipeList()
    }
  }
</script>
