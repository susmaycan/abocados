<template>
  <div>
    <Container>
      <Subtitle>Edit recipe</Subtitle>
      <div v-if="!submitted">
        <RecipeForm :recipe="recipe" :saveRecipe="saveRecipe"/>
      </div>
      <div v-else>
        Edited recipe! Click <strong>
        <Link>
          <nuxt-link :to="`/recipes/${recipe._id}`">here</nuxt-link>
        </Link>
      </strong> to see the recipe.
      </div>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class EditRecipe extends Vue {

    private recipe: any = {}
    private submitted: boolean = false

    saveRecipe() {
      RecipesAPI.update(this.recipe._id, this.recipe)
        .then((response: any) => {
          this.submitted = true
          this.recipe = response.data
        })
        .catch((e) => {
          console.log(e)
        })
    }

    retrieveRecipe() {
      let id: string = this.$route.params.id
      RecipesAPI.get(id)
        .then((response) => {
          this.recipe = response.data
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
