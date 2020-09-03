<template>
  <nav class="nav-bar">
    <div class="nav-bar-left">
      <nuxt-link class="brand" to="/"><Logo />aBocados</nuxt-link>
    </div>
    <div class="nav-bar-right">
      <nuxt-link to="/RecipeList">Recipes</nuxt-link>
      <Button>
        <nuxt-link to="/AddRecipe">AddRecipe</nuxt-link>
      </Button>
    </div>
  </nav>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import Button from "~/components/Button.vue";

  @Component({
    components: {Button}
  })
  export default class Header extends Vue {
  }
</script>

<style>
  .nav-bar {
    padding: 1rem;
    margin: 1rem;
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    left: 0;
    background-color: #ffffff;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
  }

  .nav-bar-right {
    margin-left: auto;
  }

  .brand {
    font-weight: bold;
  }


</style>
