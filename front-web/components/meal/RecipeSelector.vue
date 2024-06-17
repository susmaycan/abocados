<template>
  <v-dialog
    v-model="dialog"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <template #activator="{ on }">
      <a-button icon="fa-solid fa-pen" color="primary" fab small :on="on" />
    </template>
    <div class="recipe-list-selector p-2">
      <a-subtitle>{{ title | capitalize }}</a-subtitle>
      <search-filters :init-filters="filters" @filter="filter" />
      <recipe-list-layout
        :recipes="list"
        :empty-message="$t('recipe_search_empty')"
        :next="!!next"
        :previous="!!previous"
        :show-select="true"
        :selected-recipes="selectedRecipes"
        @search="search"
        @select="select"
      />
      <div class="my-2 d-flex justify-center">
        <a-button class="mr-2" color="secondary" @click="onCancel">
          {{ $t('cancel') | capitalize }}
        </a-button>
        <a-button
          :disabled="selectedRecipes.length === 0"
          class="mr-2"
          color="secondary"
          @click="onSelect"
        >
          {{ $t('select') | capitalize }}
        </a-button>
      </div>
    </div>
  </v-dialog>
</template>

<script>
import ListMixin from '@/mixins/list'

export default {
  name: 'MealRecipeSelector',
  mixins: [ListMixin],
  props: {
    name: {
      type: String,
      default: '',
    },
    title: {
      type: String,
      default: '',
    },
    initialRecipeList: {
      type: Array,
      default() {
        return []
      },
    },
  },
  data() {
    return {
      dialog: false,
    }
  },
  watch: {
    initialRecipeList() {
      this.selectedRecipes = this.initialRecipeList
    },
  },
  mounted() {
    this.queryParams = false
    this.getData(this.filters)
    this.selectedRecipes = this.initialRecipeList
  },
  methods: {
    onCancel() {
      this.dialog = false
    },
    onSelect() {
      this.$emit('accept', this.selectedRecipes)
      this.dialog = false
    },
    async getData(queryParams) {
      const data = await this.$api.recipe.list(queryParams)
      this.setData(data)
    },
    select(selectedRecipe, value) {
      if (value) {
        this.selectedRecipes.push(selectedRecipe)
      } else {
        const findRecipe = this.selectedRecipes.findIndex(
          (recipe) => selectedRecipe.id === recipe.id
        )
        this.selectedRecipes.splice(findRecipe, 1)
      }
    },
  },
}
</script>
<style scoped>
.recipe-list {
  height: 200px;
}
.recipe-list-selector {
  background: white;
  padding: 2em;
}
</style>
