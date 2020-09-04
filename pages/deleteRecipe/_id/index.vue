<template>
  <div>
    <Container>
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
      <div v-else>
        Deleted recipe!
        <strong>
          <Link>
            <nuxt-link to="/recipes">Go back.</nuxt-link>
          </Link>
        </strong>
      </div>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipesAPI from '~/api/recipes'

  @Component
  export default class DeleteRecipe extends Vue {

    private recipe: any = {}
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
  .delete-button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    column-gap: 2rem;
    margin: 1rem;
  }
</style>
