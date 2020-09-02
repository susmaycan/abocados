<template>
  <div class="nav-bar">
    <a href="#recipeList">Recipes</a>
    <Button>Add recipe</Button>
  </div>
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
    align-self: flex-end;
    padding: 1rem;
    margin: 1rem;
  }
</style>
