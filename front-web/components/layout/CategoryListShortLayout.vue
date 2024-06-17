<template>
  <div>
    <div class="text-left">
      <span>
        {{ title }}:
      </span>
    </div>
    <div v-if="emptyList">
      <p>{{ emptyMessage || $t('home_category_list_empty') }}</p>
    </div>
    <div v-else>
      <div v-if="!$device.isDesktop">
        <vertical-scroll-container>
          <div v-for="category in categories" :key="category.id">
            <category :category="category" @click="goToCategoryListing" />
          </div>
        </vertical-scroll-container>
      </div>
      <div v-else>
        <flex-grid>
          <div v-for="category in categories" :key="category.id">
            <category :category="category" @click="goToCategoryListing" />
          </div>
        </flex-grid>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CategoryListShortLayout',
  props: {
    categories: {
      type: Array,
      default () { return [] }
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
      return this.categories && this.categories.length === 0
    }
  },
  methods: {
    goToCategoryListing (categoryId) {
      this.$router.push({ name: 'search', query: { category: categoryId } })
    }
  }
}
</script>
<style scoped>
.list-title {
    font-size: 21px;
}
</style>
