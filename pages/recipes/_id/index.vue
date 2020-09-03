<template>
  <Container>
      <img class="recipe-img":src="recipe.picture"/>
      <Subtitle>{{recipe.name}}</Subtitle>
      <p v-if="recipe.duration !== undefined">Duration: {{recipe.duration}} min</p>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class RecipeList extends Vue {
    private recipe: object[] = []

    retrieveRecipeList() {
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
      this.retrieveRecipeList()
    }
  }
</script>

<style>
  .recipe-img {
    width: 300px;
    height: 300px;
    object-fit: cover;
  }
</style>
