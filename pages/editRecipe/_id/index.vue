<template>
  <div>
    <Loading v-if="isLoading"/>
    <Container v-else-if="!submitted && !error">
      <Subtitle>Edit recipe</Subtitle>
      <RecipeForm :recipe="recipe" :saveRecipe="saveRecipe"/>
    </Container>
    <Container v-else-if="submitted && !error">
      <h1>Yay! Recipe edited successfully!</h1>
      <p>Click <strong><Link><nuxt-link :to="`/recipes/${recipe._id}`">here</nuxt-link></Link></strong> to see the recipe.</p>
    </Container>
    <Error v-else>{{errorMsg}}</Error>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class EditRecipe extends Vue {

    private recipe: any = {}
    private submitted: boolean = false
    private error: boolean = false
    private errorMsg: string = ""
    private isLoading: boolean = false

    saveRecipe() {
      this.isLoading = true
      RecipesAPI.update(this.recipe._id, this.recipe)
        .then((response: any) => {
          this.isLoading = false
          this.submitted = true
          this.recipe = response.data
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.errorMsg = error.message
        })
    }

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
