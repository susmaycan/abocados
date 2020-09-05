<template>
  <div>
    <Loading v-if="isLoading"/>
    <Recipe v-else-if="!error" :recipe="recipe"/>
    <Error v-else>{{errorMsg}}</Error>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class RecipeComponent extends Vue {
    private recipe: object = {}
    private error: Boolean = false
    private errorMsg: String = ""
    private isLoading: Boolean = false

    retrieveRecipe() {
      let id: string = this.$route.params.id
      this.isLoading = true
      RecipesAPI.get(id)
        .then((response: any) => {
          this.isLoading = false
          this.recipe = response.data
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.errorMsg = error.message
        })
    }

    mounted() {
      this.retrieveRecipe()
    }
  }
</script>
