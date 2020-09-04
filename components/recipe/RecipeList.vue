<template>
  <Container>
    <div id="recipes">
      <Subtitle>Your recipes</Subtitle>
      <div class="recipe-list-container">
        <RecipeCard
          v-for="(recipe, index) in recipes"
          :key="index"
          :recipe="recipe"
        />
      </div>
    </div>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const RecipeListProps = Vue.extend({
    props: {
      recipes: Array
    }
  })

  @Component
  export default class RecipeList extends RecipeListProps {
  }
</script>

<style>
  .recipe-list-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-bottom: 2rem;
  }
</style>
