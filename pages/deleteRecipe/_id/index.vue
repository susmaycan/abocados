<template>
  <div>
    <Loading v-if="isLoading"/>
    <Container v-else-if="!deleted && !error">
      <Subtitle>
        Delete recipe
      </Subtitle>
      <div v-if="!deleted">
        <p>Are you sure you want to delete your delicious <strong>{{recipe.name}}</strong> recipe? </p>
        <p>Once you delete it, there's no turn back.</p>
        <div class="delete-button">
          <Button :onClick="deleteRecipe">Yes, I'm 100% sure</Button>
          <Button>
            <nuxt-link :to="`/recipes/${recipe._id}`">No wait!!</nuxt-link>
          </Button>
        </div>
      </div>
    </Container>
    <Container v-else-if="deleted && !error">
      <h1>Yay! Deleted recipe successfully!</h1>
      <Link><nuxt-link to="/recipes">Go home.</nuxt-link></Link>
    </Container>
    <Error v-else>{{errorMsg}}</Error>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class DeleteRecipe extends Vue {

    private recipe: any = {}
    private deleted: boolean = false
    private error: Boolean = false
    private errorMsg: String = ""
    private isLoading: Boolean = false

    deleteRecipe() {
      this.isLoading = true
      RecipesAPI.delete(this.recipe._id)
        .then(() => {
          this.isLoading = false
          this.deleted = true
          this.recipe = {}
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.errorMsg = error.message
        })
    }

    retrieveRecipe() {
      let id: string = this.$route.params.id
      this.isLoading = true
      RecipesAPI.get(id)
        .then((response: any) => {
          this.isLoading = false
          this.recipe = response.data
        })
        .catch((error: any) => {
          this.isLoading = false
          this.error = true
          this.errorMsg = error.message
        })
    }

    mounted() {
      this.retrieveRecipe()
    }
  }
</script>

<style>
  .delete-button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    column-gap: 2rem;
    margin: 1rem;
  }
</style>
