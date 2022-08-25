<template>
  <div>
    <div v-if="emptyList">
      <div v-if="!$device.isDesktop" class="text-left">
        <span class="list-title font-weight-bold"> {{ title }}: </span>
      </div>
      <p>{{ emptyMessage || $t("recipe_list_empty") }}</p>
    </div>
    <div v-else>
      <div v-if="!$device.isDesktop">
        <div class="d-flex justify-space-between align-center">
          <span> {{ title }}: </span>
          <span class="font-weight-bold clickable" @click="$emit('all')">
            {{ $t("all_recipes") | uppercase }}
          </span>
        </div>
        <vertical-scroll-container>
          <div v-for="recipe in recipes" :key="recipe.id">
            <recipe-card :recipe="recipe" :show-favourite="false" />
          </div>
        </vertical-scroll-container>
      </div>
      <div v-else>
        <flex-grid>
          <div v-for="recipe in recipes" :key="recipe.id">
            <recipe-card :recipe="recipe" :show-favourite="false" />
          </div>
        </flex-grid>
        <a-button full-width @click="$emit('all')">
          {{ $t("all_recipes") | uppercase }}
        </a-button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'RecipeListShortLayout',
  props: {
    recipes: {
      type: Array,
      default () {
        return []
      }
    },
    title: {
      type: String,
      default: ''
    },
    emptyMessage: {
      type: String,
      default: null
    }
  },
  computed: {
    emptyList () {
      return this.recipes && this.recipes.length === 0
    }
  }
}
</script>
<style scoped>
.list-title {
  font-size: 21px;
}
</style>
