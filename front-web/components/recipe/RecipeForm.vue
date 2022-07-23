<template>
  <v-form
    ref="recipe-form"
    v-model="valid"
  >
    <recipe-form-image :src="displayPicture" />

    <a-modal name="recipe-picture-edit-modal" :display-button-actions="false">
      <template #title>
        <a-subtitle>
          <a-icon name="fa-solid fa-image" />
          {{ $t('upload_picture') | capitalize }}
        </a-subtitle>
      </template>
      <a-file-input
        :value="form.picture"
        :error-messages="errors.picture"
        :label="$t('picture')"
        accept="image/*"
        @input="onInputChanges('picture', $event)"
      />

      <template #button-actions>
        <a-button
          color="secondary"
          :disabled="!form.picture"
          @click="submitPicture"
        >
          {{ $t('upload') | capitalize }}
        </a-button>
      </template>
    </a-modal>
    <a-input
      :value="form.name"
      :errors="errors.name"
      :label="$t('name')"
      :rules="rules.name"
      :counter="180"
      @input="onInputChanges('name', $event)"
    />

    <div class="d-flex justify-center">
      <a-input
        :value="form.duration"
        :errors="errors.duration"
        :label="$t('duration')"
        type="number"
        class="mr-2"
        @input="onInputChanges('duration', $event)"
      />
      <rating-selector
        :initial-value="form.rating"
        :rules="rules.rating"
        @input="onInputChanges('rating', $event)"
      />
    </div>
    <div>
      <a-input
        :value="form.servings"
        :errors="errors.servings"
        :label="$t('servings')"
        type="number"
        @input="onInputChanges('servings', $event)"
      />
    </div>

    <a-select
      :value="form.categories"
      :errors="errors.categories"
      :items="categories"
      :label="$t('categories')"
      item-text="name"
      item-value="id"
      multiple
      chips
      @input="onInputChanges('categories', $event)"
    />

    <ingredients-input
      :initial-ingredients="form.ingredients"
      :errors="errors.ingredients && errors.ingredients[index] ? errors.ingredients[index] : null"
      :rules="rules.directions"
      @input="onInputChanges('ingredients', $event)"
    />

    <a-text-area
      :value="form.directions"
      :errors="errors.directions"
      :required="true"
      :counter="2000"
      :label="$t('directions') | capitalize"
      auto-grow
      :rules="rules.directions"
      @input="onInputChanges('directions', $event)"
    />

    <a-alert v-if="globalError" type="error">
      {{ globalError }}
    </a-alert>
    <a-button
      v-if="$device.isMobile"
      icon="fa-solid fa-floppy-disk"
      color="primary"
      fab
      class="save-recipe-mobile"
      @click="onSubmit()"
    />
    <div v-else class="my-2">
      <a-button
        color="secondary"
        @click="onCancel"
      >
        {{ $t('cancel') | capitalize }}
      </a-button>
      <a-button
        :disabled="!valid"
        color="secondary"
        @click="onSubmit"
      >
        {{ $t('submit') | capitalize }}
      </a-button>
    </div>
  </v-form>
</template>

<script>
import { mapState } from 'vuex'
import RulesMixin from '@/utils/mixins/rules'
export default {
  name: 'RecipeForm',
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
    recipe: {
      type: Object,
      default () { return null }
    }
  },
  data () {
    return {
      valid: false,
      form: {
        name: null,
        directions: null,
        ingredients: [],
        rating: null,
        duration: null,
        servings: null,
        picture: null,
        categories: []
      },
      displayPicture: null,
      rules: {
        name: [
          this.required
        ],
        directions: [
          this.required
        ],
        ingredients: [
          this.required
        ],
        rating: [
          v => this.minMax(0, 5, v)
        ]
      },
      items: [
        this.$t('ingredients'),
        this.$t('directions')
      ]
    }
  },
  computed: {
    ...mapState(['categories'])
  },
  watch: {
    recipe () {
      this.form = this.recipe
      if (this.recipe.picture) {
        this.displayPicture = this.recipe.picture
      }
    }
  },
  methods: {
    onInputChanges (key, value) {
      this.form[key] = value
    },
    onInputUploadedPicture (value) {
      this.uploadedPicture = value
    },
    submitPicture () {
      this.displayPicture = URL.createObjectURL(this.form.picture)
      this.$modal.hide('recipe-picture-edit-modal')
    },
    onSubmit () {
      if (this.valid) {
        this.$emit('submit', this.form)
      }
    },
    onCancel () {
      this.$router.go(-1)
    }
  }

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
