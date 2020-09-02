<template>
  <div class="recipe-card-container">
    <img :src="recipe.picture"/>
    <p>{{recipe.name}}</p>
    <p v-if="recipe.duration !== undefined">Duration: {{recipe.duration}} min</p>
  </div>
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
    box-shadow: 5px 5px 5px #7F828B;
  }

  .recipe-card-container img {
    width: 200px;
    height: 200px;
    object-fit: cover;
  }
</style>
