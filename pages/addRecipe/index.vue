<template>
  <div>
    <Loading v-if="isLoading"/>
    <Container v-else-if="!submitted && !error">
      <Subtitle>Add recipe</Subtitle>
      <RecipeForm :recipe="recipe" :saveRecipe="saveRecipe"/>
    </Container>
    <Container v-else-if="submitted && !error">
      <h1>Yay! Recipe added successfully!</h1>
      <p>Click <strong>
        <Link>
          <nuxt-link :to="`recipes/${recipe._id}`">here</nuxt-link>
        </Link>
      </strong> to see the recipe.
      </p>
    </Container>
    <Error v-else>{{errorMsg}}</Error>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class AddRecipe extends Vue {

    private recipe: any = {
      name: "",
      ingredients: undefined,
      directions: undefined,
      duration: undefined,
      difficult: undefined,
      ranking: undefined
    }
    private submitted: boolean = false
    private error: Boolean = false
    private errorMsg: String = ""
    private isLoading: Boolean = false


    saveRecipe() {
      this.isLoading = true
      RecipesAPI.create(this.recipe)
        .then((response: any) => {
          this.isLoading = false
          this.error = false
          this.submitted = true
          this.recipe = response.data
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.submitted = false
          this.errorMsg = error.message
        })
    }


  }
</script>
