<template>
  <Container>
    <div class="recipe-header">
      <Subtitle>{{recipe.name}}</Subtitle>
      <Ranking :rankingList="recipe.ranking"/>
    </div>
    <div class="recipe-detail-container">
      <div v-if="recipe.picture" class="container-left">
        <img class="recipe-img" :src="recipe.picture"/>
      </div>
      <div class="container-right">
        <p v-if="recipe.duration">
          <TimeIcon/>
          {{recipe.duration}} min
        </p>
        <div>
          <h3>Ingredients</h3>
          <p class="line-breaks" v-if="recipe.ingredients">{{recipe.ingredients}}</p>
        </div>
        <div>
          <h3>Directions</h3>
          <p class="line-breaks" v-if="recipe.directions">{{recipe.directions}}</p>
        </div>
      </div>
    </div>
    <div class="recipe-icons">
      <Button>
        <nuxt-link :to="`/editRecipe/${recipe._id}`">
          <EditIcon/>
          Edit
        </nuxt-link>
      </Button>
      <Button>
        <nuxt-link :to="`/deleteRecipe/${recipe._id}`">
          <DeleteIcon/>
          Delete
        </nuxt-link>
      </Button>
    </div>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const RecipeProps = Vue.extend({
    props: {
      recipe: Object
    }
  })

  @Component
  export default class RecipeList extends RecipeProps {

  }
</script>

<style>
  .recipe-detail-container {
    display: flex;
    flex-direction: row;
    column-gap: 2rem;
    justify-content: center;
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

  .line-breaks {
    white-space: pre-wrap;
  }

  .recipe-icons {
    padding: 1rem;
  }

</style>
