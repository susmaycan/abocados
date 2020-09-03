<template>
  <Container>
    <div id="recipes">
      <Subtitle>Recipes</Subtitle>
      <div class="recipe-list-container">
        <RecipeCard
          v-for="(recipe, index) in recipeList"
          :key="index"
          :recipe="recipe"
        />
      </div>
    </div>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'
  import RecipeCard from "~/components/RecipeCard.vue";
  import Subtitle from "~/components/Subtitle.vue";

  @Component({
    components: {Subtitle, RecipeCard}
  })
  export default class RecipeList extends Vue {
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

<style>
  .recipe-list-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>
