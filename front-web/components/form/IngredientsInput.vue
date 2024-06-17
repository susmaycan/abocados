<template>
  <div class="mb-4">
    <div class="d-flex justify-space-between align-center">
      <a-label>
        {{ $t("ingredients") | capitalize }}
      </a-label>
      <a-button
        icon="fa-solid fa-circle-plus"
        text
        color="secondary"
        @click="addIngredient"
      />
    </div>
    <div v-if="ingredients.length === 0">
      <p class="small-input">
        {{ $t("ingredients_list_empty") }}
      </p>
    </div>
    <div
      v-for="(ingredient, index) in ingredients"
      v-else
      :key="index"
      class="d-flex justify-space-between align-center my-0 py-0"
    >
      <form-text-input
        :value="ingredients[index]"
        :errors="errors"
        :placeholder="$t('ingredient')"
        class="my-0 py-0 small-input"
        v-bind="$attrs"
        @input="onIngredientChanges(index, $event)"
      />
      <a-button
        text
        icon="fa-solid fa-circle-minus"
        @click="deleteIngredient(index)"
      />
    </div>
  </div>
</template>
<script>
export default {
  name: 'IngredientsInput',
  props: {
    errors: {
      type: Object,
      default () {
        return {}
      }
    },
    initialIngredients: {
      type: Array,
      default () {
        return []
      }
    }
  },
  data () {
    return {
      ingredients: []
    }
  },
  watch: {
    initialIngredients () {
      this.ingredients = this.initialIngredients
    },
    ingredients () {
      this.$emit('input', this.ingredients)
    }
  },
  methods: {
    onIngredientChanges (index, value) {
      this.ingredients[index] = value
    },
    addIngredient () {
      this.ingredients.push('')
    },
    deleteIngredient (index) {
      this.ingredients.splice(index, 1)
    }
  }
}
</script>

<style scoped>
.small-input {
  font-size: 12px;
}
</style>
