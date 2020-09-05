<template>
  <div>
    <Loading v-if="isLoading"/>
    <RecipeList v-else-if="!error" :recipes="recipeList"/>
    <Error v-else>{{errorMsg}}</Error>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class Recipes extends Vue {
    private recipeList: any[] = []
    private error: Boolean = false
    private errorMsg: String = ""
    private isLoading: Boolean = false

    retrieveRecipeList() {
      this.isLoading = true
      RecipesAPI.getAll()
        .then((response: any) => {
          this.isLoading = false
          this.recipeList = response.data
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.errorMsg = error.message
        })
    }

    mounted() {
      this.retrieveRecipeList()
    }
  }
</script>
