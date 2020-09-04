<template>
  <Container>
    <div class="recipe-header">
      <Subtitle>{{recipe.name}}</Subtitle>
      <Ranking :rankingList="recipe.ranking"/>
    </div>
    <div class="recipe-detail-container">
      <div class="container-left">
        <img class="recipe-img" :src="recipe.picture"/>
      </div>
      <div class="container-right">
        <p v-if="recipe.duration !== undefined">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
               class="feather feather-clock">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
          {{recipe.duration}} min
        </p>
        <div>
          <h3>Ingredients</h3>
          <ul>
            <li v-for="(ingredient, index) in recipe.ingredients" :key="index" v-if="recipe.ingredients !== undefined">
              {{ingredient}}
            </li>
          </ul>
        </div>
        <div>
          <h3>Directions</h3>
          <p v-if="recipe.directions !== undefined">{{recipe.directions}}</p>
        </div>
      </div>
    </div>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'
  import Ranking from "~/components/Ranking.vue";

  @Component({
    components: {Ranking}
  })
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

  .recipe-detail-container {
    display: flex;
    flex-direction: row;
    column-gap: 2rem;
  }

  .recipe-img {
    width: 250px;
    height: 250px;
    object-fit: cover;
    border-radius: .5rem;
  }

  .container-right {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    text-align: left;
    row-gap: 1rem;
  }

  .recipe-header {
    margin-bottom: 2rem;
  }

  .feather-clock{
    margin-bottom: -.4rem;
  }

</style>
