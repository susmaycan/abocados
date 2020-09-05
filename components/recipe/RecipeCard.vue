<template>
  <nuxt-link v-if="recipe._id !== undefined" :to="`recipes/${recipe._id}`">
    <div class="recipe-card-container">
      <img :src="recipe.picture"/>
      <p>{{recipe.name}}</p>
      <Ranking :rankingList="recipe.ranking"/>
    </div>
  </nuxt-link>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const RecipeProps = Vue.extend({
    props: {
      recipe: Object
    }
  })

  @Component
  export default class RecipeCard extends RecipeProps {
  }
</script>

<style>
  .recipe-card-container {
    padding: 1rem;
    margin: 1rem;
    border-radius: 0.5rem;
    border: .5px solid #cdcdcd;
  }

  .recipe-card-container:hover {
    box-shadow: 5px 5px 5px #7F828B;
  }

  .recipe-card-container img {
    width: 200px;
    height: 200px;
    object-fit: cover;
  }
</style>
