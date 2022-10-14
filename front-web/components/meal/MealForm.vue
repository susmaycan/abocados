<template>
  <v-form
    ref="meal-form"
    v-model="valid"
  >
    <a-date-picker
      :value="form.date"
      :errors="errors.date"
      :label="$t('date')"
      :rules="rules.date"
      :disabled="edit"
      @input="onInputChanges('date', $event)"
    />

    <div class="text-left">
      <div class="d-flex justify-space-between">
        <a-subtitle>{{ $t('breakfast') | capitalize }}</a-subtitle>
        <meal-recipe-selector
          :title="$t('select_breakfast_recipes')"
          :initial-recipe-list="form.breakfast"
          @accept="selectBreakfastRecipe"
        />
      </div>
      <meal-recipe-list
        :recipe-list="form.breakfast"
        :empty-message="$t('meal_empty_recipes_breakfast')"
      />
    </div>

    <div class="text-left">
      <div class="d-flex justify-space-between">
        <a-subtitle>{{ $t('lunch') | capitalize }}</a-subtitle>
        <meal-recipe-selector
          :title="$t('select_lunch_recipes')"
          :initial-recipe-list="form.lunch"
          @accept="selectLunchRecipe"
        />
      </div>
      <meal-recipe-list
        :recipe-list="form.lunch"
        :empty-message="$t('meal_empty_recipes_lunch')"
      />
    </div>

    <div class="text-left">
      <div class="d-flex justify-space-between">
        <a-subtitle>{{ $t('dinner') | capitalize }}</a-subtitle>
        <meal-recipe-selector
          :title="$t('select_dinner_recipes')"
          :initial-recipe-list="form.dinner"
          @accept="selectDinnerRecipe"
        />
      </div>
      <meal-recipe-list
        :recipe-list="form.dinner"
        :empty-message="$t('meal_empty_recipes_dinner')"
      />
    </div>

    <a-alert v-if="globalError" type="error">
      {{ globalError }}
    </a-alert>
    <div class="my-2 d-flex justify-center">
      <a-button
        class="mr-2"
        color="secondary"
        @click="onCancel"
      >
        {{ $t('cancel') | capitalize }}
      </a-button>
      <a-button
        :disabled="!valid"
        class="mr-2"
        color="secondary"
        @click="onSubmit"
      >
        {{ $t('save') | capitalize }}
      </a-button>
    </div>
  </v-form>
</template>

<script>
import RulesMixin from '@/utils/mixins/rules'

export default {
  name: 'MealForm',
  mixins: [RulesMixin],
  props: {
    errors: {
      type: Object,
      default () { return {} }
    },
    globalError: {
      type: String,
      default () { return null }
    },
    meal: {
      type: Object,
      default () { return null }
    },
    edit: {
      type: Boolean,
      default: false
    },
    date: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      valid: false,
      form: {
        date: null,
        breakfast: [],
        lunch: [],
        dinner: []
      },
      rules: {
        date: [
          this.required,
          v => this.maxLength(v, 50)
        ]
      }
    }
  },
  watch: {
    date (newValue) {
      this.form.date = newValue
    },
    meal (newVal) {
      this.form = newVal
    }
  },
  mounted () {
    if (this.meal) {
      this.form = this.meal
    } else if (this.date) {
      this.form.date = this.date
    }
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
    },
    onSubmit () {
      if (this.valid) {
        const newForm = { ...this.form }
        newForm.breakfast = this.parseRecipes(newForm.breakfast)
        newForm.lunch = this.parseRecipes(newForm.lunch)
        newForm.dinner = this.parseRecipes(newForm.dinner)
        this.$emit('submit', newForm)
      }
    },
    onCancel () {
      this.$router.go(-1)
    },
    selectBreakfastRecipe (selectedRecipes) {
      this.form.breakfast = selectedRecipes
    },
    selectLunchRecipe (selectedRecipes) {
      this.form.lunch = selectedRecipes
    },
    selectDinnerRecipe (selectedRecipes) {
      this.form.dinner = selectedRecipes
    },
    parseRecipes (recipeList) {
      return recipeList.map(recipe => recipe.id)
    }
  }
}
</script>
