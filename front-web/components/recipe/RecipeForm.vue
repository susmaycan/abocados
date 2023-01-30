<template>
  <v-form ref="recipe-form" v-model="valid">
    <recipe-form-image :src="displayPicture" />

    <a-modal name="recipe-picture-edit-modal" :display-button-actions="false">
      <template #title>
        <a-subtitle>
          <a-icon name="fa-solid fa-image" />
          {{ $t("upload_picture") | capitalize }}
        </a-subtitle>
      </template>
      <form-file-input
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
          {{ $t("upload") | capitalize }}
        </a-button>
      </template>
    </a-modal>
    <form-text-input
      :value="form.name"
      :errors="errors.name"
      :label="$t('name')"
      :rules="rules.name"
      :counter="50"
      @input="onInputChanges('name', $event)"
    />

    <div class="d-flex justify-center">
      <form-text-input
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
      <form-text-input
        :value="form.servings"
        :errors="errors.servings"
        :label="$t('servings')"
        type="number"
        @input="onInputChanges('servings', $event)"
      />
    </div>

    <form-select
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

    <form-text-area
      :value="form.ingredients"
      :errors="errors.ingredients"
      :counter="2000"
      :label="$t('ingredients') | capitalize"
      auto-grow
      @input="onInputChanges('ingredients', $event)"
    />

    <form-text-area
      :value="form.directions"
      :errors="errors.directions"
      :counter="2000"
      :label="$t('directions') | capitalize"
      auto-grow
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
      @click="onSubmit(SAVE_TYPE.SAVE)"
    />
    <div v-else class="my-2 d-flex justify-center">
      <a-button class="mr-2" color="secondary" @click="onCancel">
        {{ $t("cancel") | capitalize }}
      </a-button>
      <a-button
        :disabled="!valid"
        class="mr-2"
        color="secondary"
        @click="onSubmit(SAVE_TYPE.SAVE)"
      >
        {{ $t("save") | capitalize }}
      </a-button>
      <a-button
        v-if="!edit"
        :disabled="!valid"
        color="secondary"
        @click="onSubmit(SAVE_TYPE.SAVE_AND_ADD)"
      >
        {{ $t("save_add") | capitalize }}
      </a-button>
    </div>
  </v-form>
</template>

<script>
import { mapState } from 'vuex'
import RulesMixin from '@/utils/mixins/rules'
import { SAVE_TYPE } from '@/utils/consts'

export default {
  name: 'RecipeForm',
  mixins: [RulesMixin],
  props: {
    errors: {
      type: Object,
      default () {
        return {}
      }
    },
    globalError: {
      type: String,
      default () {
        return null
      }
    },
    recipe: {
      type: Object,
      default () {
        return null
      }
    },
    edit: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      valid: false,
      form: {
        name: null,
        directions: null,
        ingredients: null,
        rating: null,
        duration: null,
        servings: null,
        picture: null,
        categories: []
      },
      displayPicture: null,
      rules: {
        name: [this.required, v => this.maxLength(v, 50)],
        rating: [v => this.minMax(0, 5, v)]
      },
      items: [this.$t('ingredients'), this.$t('directions')],
      SAVE_TYPE
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
    submitPicture () {
      this.displayPicture = URL.createObjectURL(this.form.picture)
      this.$modal.hide('recipe-picture-edit-modal')
    },
    onSubmit (saveType) {
      if (this.valid) {
        this.$emit('submit', this.form, saveType)
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
