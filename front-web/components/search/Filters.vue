<template>
  <div>
    <a-drawer :show="showFilters" @change="toggleShowFilters">
      <div class="filters px-6 my-3">
        <a-subtitle>
          <a-icon name="fa-solid fa-filter" />{{ $t('filters') | capitalize }}
        </a-subtitle>
        <search-selector-category
          class="my-3"
          :name="$t('time') | capitalize"
          :categories="getCategoriesByType(categoryType.TIME)"
          :value="filters.category"
          @input="selectCategory"
        />
        <search-selector-category
          class="my-3"
          :name="$t('cuisine') | capitalize"
          :categories="getCategoriesByType(categoryType.CUISINE)"
          :value="filters.category"
          @input="selectCategory"
        />
        <search-selector-category
          class="my-3"
          :name="$t('food') | capitalize"
          :categories="getCategoriesByType(categoryType.FOOD)"
          :value="filters.category"
          @input="selectCategory"
        />
        <search-selector-rating
          class="my-3"
          :value="filters.rating"
          @input="onInputChanges('rating', $event)"
        />
        <search-selector-duration
          class="my-3"
          :value="filters.duration"
          @input="onInputChanges('duration', $event)"
        />
        <a-button
          class="my-3"
          full-width
          color="secondary"
          icon="fa-solid fa-circle-xmark"
          @click="clearFilters"
        >
          {{ $t('reset') }}
        </a-button>
      </div>
    </a-drawer>
    <div class="d-flex justify-center align-center filters my-2">
      <form-text-input
        :value="filters.name"
        :label="$t('search_placeholder')"
        class="name-filter-input"
        rounded
        hide-details="auto"
        filled
        dense
        clearable
        @input="onInputChanges('name', $event)"
      >
        <template #icon-left-inner>
          <a-icon name="fa-solid fa-magnifying-glass" class="mr-2" />
        </template>
      </form-text-input>
      <a-badge :show="!filtersEmpty" color="primary">
        <a-button
          icon="fa-solid fa-filter"
          color="secondary"
          text
          @click="toggleShowFilters(true)"
        />
      </a-badge>
    </div>
  </div>
</template>
<script>
import { capitalize, isEmpty } from 'lodash'
import { mapState } from 'vuex'
import RouteMixin from '@/mixins/route'
import { CATEGORY_TYPE } from '@/utils/consts'

export default {
  name: 'SearchFilters',
  mixin: [RouteMixin],
  props: {
    initFilters: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  data() {
    return {
      filters: {},
      showFilters: false,
      categoryType: CATEGORY_TYPE,
    }
  },
  computed: {
    ...mapState(['categories']),
    parsedFilters() {
      const finalFilters = []
      Object.entries(this.filters).forEach(([key, value]) => {
        if (Array.isArray(value) && value.length > 0) {
          value.forEach((arrayVal) => {
            if (arrayVal) {
              finalFilters.push({ key, value: arrayVal })
            }
          })
        } else if (!Array.isArray(value) && value) {
          finalFilters.push({ key, value })
        }
      })
      return finalFilters
    },
    filtersEmpty() {
      return isEmpty(this.filters)
    },
    filterCount() {
      return Object.keys(this.filters).length
    },
  },
  watch: {
    initFilters: {
      handler(val) {
        const initialFilters = { ...val }
        if (initialFilters.category) {
          initialFilters.category = this.parseCategories(
            initialFilters.category
          )
        }
        this.filters = initialFilters
      },
      deep: true,
    },
  },
  mounted() {
    this.filters = { ...this.initFilters }
    if (this.filters.category) {
      this.filters.category = [this.initFilters.category]
    }
  },
  methods: {
    capitalize,
    onInputChanges(key, value) {
      this.filters = { ...this.filters, [key]: value }
      this.getData()
    },
    clearFilters() {
      this.filters = {}
      this.getData()
      this.toggleShowFilters(false)
    },
    toggleShowFilters(value) {
      this.showFilters = value
    },
    getData() {
      this.$emit('filter', this.filters)
    },
    parseCategories(categories) {
      const initialCategories = categories
      if (!initialCategories) {
        return null
      }
      if (!Array.isArray(initialCategories)) {
        const parsedInt = parseInt(initialCategories)
        if (parsedInt) {
          return [parsedInt]
        }
      }
      return initialCategories.map((categoryString) => parseInt(categoryString))
    },
    selectCategory(categoryList) {
      if (!this.filters.category) {
        this.filters.category = []
      }

      if (categoryList.length === 0) {
        this.filters = {
          ...this.filters,
          category: null,
        }
        delete this.filters.category
      } else {
        this.filters = {
          ...this.filters,
          category: categoryList,
        }
      }

      this.getData()
    },
    getCategoriesByType(type) {
      return this.categories.filter((category) => category.type === type)
    },
  },
}
</script>
<style scoped>
.filters {
  width: 100%;
}
.show-filters-mobile {
  position: fixed;
  bottom: 40px;
  right: 20px;
  margin-bottom: 40px;
  border-radius: 50%;
}
</style>
