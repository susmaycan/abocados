<template>
  <div>
    <Container>
      <Subtitle>Add recipe</Subtitle>
      <div v-if="!submitted">
        <RecipeForm :recipe="recipe" :saveRecipe="saveRecipe" />
      </div>
      <div v-else>
        Submitted recipe! Click <strong><Link><nuxt-link :to="`recipes/${recipe._id}`">here</nuxt-link></Link></strong> to see the recipe.
      </div>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class AddRecipe extends Vue {

    private recipe: Object = {
      name: "",
      ingredients: undefined,
      directions: undefined,
      duration: undefined,
      difficult: undefined,
      ranking: undefined
    }
    private submitted: boolean = false


    saveRecipe() {
      RecipesAPI.create(this.recipe)
        .then((response) => {
          this.submitted = true
          this.recipe = response.data
        })
        .catch((e) => {
          console.log(e)
        })
    }


  }
</script>

<style>
  .input-form {
    padding: 1rem;
  }
</style>
