import RouteMixin from '@/mixins/route'

export default {
  mixins: [RouteMixin],
  data() {
    return {
      list: null,
      previous: null,
      next: null,
      filters: {},
      selectedRecipes: [],
      queryParams: true,
    }
  },
  mounted() {
    if (this.queryParams) {
      this.setFilters()
    }
    this.getData(this.filters)
  },
  methods: {
    setData(data) {
      this.list = data.results
      this.previous = data.previous
      this.next = data.next
    },
    search(pageFilter) {
      this.getData({
        ...this.filters,
        page: pageFilter,
      })
    },
    filter(queryParams) {
      if (this.queryParams) {
        this.applyFilters(queryParams)
      }
      this.getData(queryParams)
    },
  },
}
