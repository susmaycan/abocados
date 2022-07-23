<template>
  <page-layout :menu="isCreator(recipe)">
    <template #buttons>
      <div v-if="isCreator(recipe)">
        <a-button icon="fa-solid fa-pen" color="secondary" @click="onEdit()">
          {{ $t("edit") | capitalize }}
        </a-button>
        <a-button
          icon="fa-solid fa-trash"
          color="secondary"
          @click="onDelete()"
        >
          {{ $t("delete") | capitalize }}
        </a-button>
      </div>
    </template>
    <template #menu>
      <div v-if="isCreator(recipe)" class="d-flex flex-column">
        <v-list>
          <v-list-item class="clickable" @click="onEdit()">
            <v-list-item-title>
              <a-icon name="fa-solid fa-pen" />
              {{ $t("edit") | capitalize }}
            </v-list-item-title>
          </v-list-item>

          <v-list-item class="clickable" @click="onDelete()">
            <v-list-item-title>
              <a-icon name="fa-solid fa-trash" />
              {{ $t("delete") | capitalize }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </div>
    </template>

    <div v-if="recipe" class="text-center">
      <recipe-card-image
        :width="$device.isMobile ? '100%' : ''"
        :recipe="recipe"
        @toggle-favourite="toggleFavourite"
      />
      <a-title>
        {{ recipe.name }}
      </a-title>
      <p v-if="!isCreator(recipe)" class="grey--text">
        {{ $t("by") }} <b>{{ recipe.creator.username }}</b>
      </p>

      <div class="d-flex align-stretch justify-center my-2">
        <span v-if="recipe.duration" class="mr-3"
          ><a-icon name="fa-solid fa-clock" /> {{ recipe.duration }}
          {{ $t("min") }}</span
        >
        <v-divider v-if="recipe.duration" vertical />
        <a-rating class="ml-2" :rating="recipe.rating" />
      </div>
      <servings v-if="recipe.servings" :servings="recipe.servings" />

      <div v-if="recipe.categories.length > 0" class="my-2">
        <a-pill
          v-for="category in recipe.categories"
          :key="category.id"
          color="primary"
          class="mr-2"
          outlined
        >
          {{ category.name }}
        </a-pill>
      </div>

      <a-tabs :items="items">
        <a-tabs-item key="ingredients">
          <pre class="paragraph my-3">
            {{ recipe.ingredients }}
          </pre>
        </a-tabs-item>
        <a-tabs-item key="directions">
          <pre class="paragraph my-3">
            {{ recipe.directions }}
          </pre>
        </a-tabs-item>
      </a-tabs>

      <a-modal name="delete-recipe" @accept="onAcceptDelete">
        <template #title>
          <a-subtitle>
            <a-icon name="fa-solid fa-triangle-exclamation" />
            {{ $t("delete_recipe") | capitalize }}
          </a-subtitle>
        </template>
        <p>
          {{ $t("delete_recipe_text") }}
          <span class="font-weight-bold">{{ recipe.name }}</span> ?
        </p>
      </a-modal>
    </div>
  </page-layout>
</template>
<script>
import mixin from "@/utils/mixins/global";

export default {
  name: "RecipeDetail",
  mixins: [mixin],
  middleware: ["auth-custom"],
  data() {
    return {
      recipe: null,
      items: [this.$t("ingredients"), this.$t("directions")],
    };
  },
  computed: {
    recipeId() {
      return this.$route.params.id;
    },
    title() {
      return this.recipe ? this.recipe.name : this.$t("recipe");
    },
  },
  async mounted() {
    this.recipe = await this.$api.recipe.findOne(this.recipeId);
  },
  methods: {
    onEdit() {
      this.$router.push({
        name: "recipes-edit-id",
        params: { id: this.recipeId },
      });
    },
    onDelete() {
      this.$modal.show("delete-recipe");
    },
    toggleFavourite(value) {
      this.recipe.favourited = value;
    },
    async onAcceptDelete() {
      await this.$api.recipe.delete(this.recipeId);
      this.$router.push({ name: "recipes" });
    },
  },
};
</script>

<style scoped>
.paragraph {
  white-space: pre-line; /* Since CSS 2.1 */
  white-space: -moz-pre-line; /* Mozilla, since 1999 */
  white-space: -pre-line; /* Opera 4-6 */
  white-space: -o-pre-line; /* Opera 7 */
  word-wrap: break-word;

  font-size: inherit;
  color: inherit;
  border: initial;
  font-family: inherit;
}
</style>
