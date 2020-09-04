<template>
  <form v-on:submit.prevent="saveRecipe">

    <div class="input-form">
      <label for="name">Name: </label> <br/>
      <input placeholder="Tikka masala" v-model="recipe.name" name="name" id="name" type="text" required/>
    </div>

    <div class="grid-form">
      <div class="input-form">
        <label for="duration">Duration (min):</label><br/>
        <input placeholder="60" v-model="recipe.duration" name="duration" id="duration" type="number"/>
      </div>

      <div class="input-form">
        <label for="ranking">Ranking: </label><br/>
        <input placeholder="2" min="1" max="5" v-model="recipe.ranking" name="ranking" id="ranking" type="number"/>
      </div>
      <div class="input-form">
        <label for="picture">Picture URL: </label>
        <input placeholder="https://www.google.es/images/asd.png" v-model="recipe.picture" name="picture" id="picture"
               type="url"/>
      </div>
    </div>
    <div class="grid-text-area">
      <div class="input-form">
        <label for="ingredients">Ingredients: </label>
        <textarea rows="10" cols="10" v-model="recipe.ingredients" name="ingredients" id="ingredients" type="string"/>
      </div>

      <div class="input-form">
        <label for="directions">Directions: </label>
        <textarea rows="10" cols="10" v-model="recipe.directions" name="directions" id="directions"/>
      </div>
    </div>
    <Button :submit="true">Submit</Button>
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

  .grid-form {
    display: grid;
    grid-template-columns:  1fr 1fr 1fr;
  }

  .grid-text-area {
    display: grid;
    grid-template-columns:  1fr 1fr;
  }

  .input-form {
    padding: 1rem;
  }

  @media (max-width: 800px) {
    .grid-form {
      grid-template-columns:  1fr;
    }

    .grid-text-area {
      grid-template-columns:  1fr;
    }
  }

  input, textarea {
    border: .5px solid #3F3D56;
    padding: .5rem;
    margin: .5rem;
    border-radius: 1rem;
    width: 100%;
  }

  input:focus {
    border: 1px solid #3F3D56;
  }
</style>
