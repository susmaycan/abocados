<template>
  <v-form ref="meal-form" v-model="valid">
    <form-date-picker
      :value="form.date"
      :errors="formErrors.date"
      :label="$t('date')"
      :rules="rules.date"
      :disabled="isEditMode"
      @input="onInputChanges('date', $event)"
    />

    <div class="text-left">
      <div class="d-flex justify-space-between">
        <a-subtitle>{{ $t('breakfast') | capitalize }}</a-subtitle>
        <meal-recipe-selector
          :title="$t('select_breakfast_recipes')"
          :initial-recipe-list="form.breakfast"
          @accept="onInputChanges('breakfast', $event)"
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
          @accept="onInputChanges('lunch', $event)"
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
          @accept="onInputChanges('dinner', $event)"
        />
      </div>
      <meal-recipe-list
        :recipe-list="form.dinner"
        :empty-message="$t('meal_empty_recipes_dinner')"
      />
    </div>

    <form-errors :errors="globalErrors" />

    <div class="my-2 d-flex justify-center">
      <a-button class="mr-2" color="secondary" @click="onCancel">
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
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'

export default {
  name: 'MealForm',
  mixins: [RulesMixin, FormMixin],
  props: {
    date: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      rules: {
        date: [this.required, (v) => this.maxLength(v, 50)],
      },
    }
  },
  watch: {
    date(newValue) {
      this.form.date = newValue
    },
  },
  mounted() {
    if (this.date) {
      this.form.date = this.date
    }
  },
  methods: {
    onSubmit() {
      if (this.valid) {
        const newForm = { ...this.form }
        newForm.breakfast = this.parseRecipes(newForm.breakfast)
        newForm.lunch = this.parseRecipes(newForm.lunch)
        newForm.dinner = this.parseRecipes(newForm.dinner)
        this.$emit('submit', newForm)
      }
    },
    parseRecipes(recipeList) {
      if (!recipeList) {
        return []
      }
      return recipeList.map((recipe) => recipe.id)
    },
  },
}
</script>
