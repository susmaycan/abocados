<template>
  <form v-on:submit.prevent="saveRecipe">
    <div class="input-form">
      <label for="name">Name: </label>
      <input v-model="recipe.name" name="name" id="name" type="text" required/>
    </div>
    <div class="input-form">
      <label for="duration">Duration (in minutes):</label>
      <input v-model="recipe.duration" name="duration" id="duration" type="number"/>
    </div>
    <div class="input-form">
      <label for="ranking">Ranking (from 1 to 5): </label>
      <input v-model="recipe.ranking" name="ranking" id="ranking" type="number"/>
    </div>

    <div class="input-form">
      <label for="picture">Picture URL: </label>
      <input v-model="recipe.picture" name="picture" id="picture" type="url"/>
    </div>

    <div class="input-form">
      <label for="ingredients">Ingredients: </label>
      <input name="ingredients" id="ingredients" type="string"/>
    </div>

    <div class="input-form">
      <label for="directions">Directions: </label>
      <textarea v-model="recipe.directions" name="directions" id="directions"/>
    </div>

    <button type="submit">Submit</button>
  </form>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  const RecipeFormProps = Vue.extend({
    props: {
      recipe: {type: Object, required: true,},
      saveRecipe: {type: Function, required: true,}
    }
  })

  @Component
  export default class RecipeForm extends RecipeFormProps {
  }
</script>

<style>
  .input-form {
    padding: 1rem;
  }
</style>
