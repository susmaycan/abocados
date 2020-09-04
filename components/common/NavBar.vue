<template>
  <nav class="nav-bar">
    <div class="nav-bar-left">
      <nuxt-link class="brand" to="/">
        <Logo/>
        aBocados
      </nuxt-link>
    </div>
    <div class="nav-bar-right">
      <Link>
        <nuxt-link to="/recipes">Recipes</nuxt-link>
      </Link>
      <Button>
        <nuxt-link to="/addRecipe">Add recipe</nuxt-link>
      </Button>
    </div>
  </nav>
</template>

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
    justify-content: space-between;
  }

  .brand {
    font-weight: bold;
  }


</style>
