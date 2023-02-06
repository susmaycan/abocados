<template>
  <v-form ref="recipe-form" v-model="valid">
    <form-image
      width="350px"
      height="350px"
      :image="form.picture"
      type="recipe"
      :errors="formErrors.picture"
      @input="onInputChanges('picture', $event)"
    />

    <form-text-input
      :value="form.name"
      :errors="formErrors.name"
      :label="$t('name')"
      :rules="rules.name"
      :counter="50"
      @input="onInputChanges('name', $event)"
    />

    <div class="d-flex justify-center">
      <form-text-input
        :value="form.duration"
        :errors="formErrors.duration"
        :label="$t('duration')"
        type="number"
        class="mr-2"
        @input="onInputChanges('duration', $event)"
      />
      <form-rating-selector
        :initial-value="form.rating"
        :rules="rules.rating"
        @input="onInputChanges('rating', $event)"
      />
    </div>
    <div>
      <form-text-input
        :value="form.servings"
        :errors="formErrors.servings"
        :label="$t('servings')"
        type="number"
        @input="onInputChanges('servings', $event)"
      />
    </div>

    <form-select
      :value="form.categories"
      :errors="formErrors.categories"
      :items="categories"
      :label="$t('categories')"
      item-text="name"
      item-value="id"
      multiple
      chips
      @input="onInputChanges('categories', $event)"
    />

    <form-text-area
      :value="form.ingredients"
      :errors="formErrors.ingredients"
      :counter="2000"
      :label="$t('ingredients') | capitalize"
      auto-grow
      @input="onInputChanges('ingredients', $event)"
    />

    <form-text-area
      :value="form.directions"
      :errors="formErrors.directions"
      :counter="2000"
      :label="$t('directions') | capitalize"
      auto-grow
      @input="onInputChanges('directions', $event)"
    />

    <form-errors :errors="globalErrors" />

    <a-button
      v-if="$device.isMobile"
      icon="fa-solid fa-floppy-disk"
      color="primary"
      fab
      class="save-recipe-mobile"
      @click="onSubmit(SAVE_TYPE.SAVE)"
    />
    <div v-else class="my-2 d-flex justify-center">
      <a-button class="mr-2" color="secondary" @click="onCancel">
        {{ $t('cancel') | capitalize }}
      </a-button>
      <a-button
        :disabled="!valid"
        class="mr-2"
        color="secondary"
        @click="onSubmit(SAVE_TYPE.SAVE)"
      >
        {{ $t('save') | capitalize }}
      </a-button>
      <!-- <a-button
        v-if="!isEditMode"
        :disabled="!valid"
        color="secondary"
        @click="onSubmit(SAVE_TYPE.SAVE_AND_ADD)"
      >
        {{ $t('save_add') | capitalize }}
      </a-button> -->
    </div>
  </v-form>
</template>

<script>
import { mapState } from 'vuex'
import RulesMixin from '@/mixins/rules'
import FormMixin from '@/mixins/form'
import { SAVE_TYPE } from '@/utils/consts'

export default {
  name: 'RecipeForm',
  mixins: [RulesMixin, FormMixin],
  data() {
    return {
      displayPicture: null,
      rules: {
        name: [this.required, (v) => this.maxLength(v, 50)],
        rating: [(v) => this.minMax(0, 5, v)],
      },
      SAVE_TYPE,
    }
  },
  computed: {
    ...mapState(['categories']),
  },
}
</script>

<style scoped>
.save-recipe-mobile {
  position: fixed;
  bottom: 40px;
  right: 20px;
  margin-bottom: 40px;
  border-radius: 50%;
}
</style>
