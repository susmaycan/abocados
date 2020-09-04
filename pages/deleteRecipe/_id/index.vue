<template>
  <div>
    <Container>
      <Subtitle>
        <DeleteIcon/>
        Delete recipe
      </Subtitle>
      <div v-if="!deleted">
        <p>Are you sure you want to delete your delicious {{recipe.name}} recipe? </p>
        <p>Once you delete it there's not turn back!</p>
        <button @click="deleteRecipe">Yes, I'm 100% sure</button>
        <nuxt-link :to="`/recipes/${recipe._id}`">No wait!!</nuxt-link>
      </div>
      <div v-else>
        Deleted recipe!
        <nuxt-link to="/recipes">Go back</nuxt-link>
      </div>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class DeleteRecipe extends Vue {

    private recipe: Object = {}
    private deleted: boolean = false


    deleteRecipe() {
      RecipesAPI.delete(this.recipe._id)
        .then(() => (
          this.deleted = true
        ))
        .catch((e) => {
          console.log(e)
        })
    }

    retrieveRecipe() {
      let id: string = this.$route.params.id
      RecipesAPI.get(id)
        .then((response) => {
          this.recipe = response.data
        })
        .catch((e) => {
          console.log(e)
        })
    }

    mounted() {
      this.retrieveRecipe()
    }
  }
</script>

<style>
  .input-form {
    padding: 1rem;
  }
</style>
