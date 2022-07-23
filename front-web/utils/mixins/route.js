import _ from 'lodash'

export default {
  methods: {
    applyFilters (params) {
      const { name } = this.$route
      const queryParams = { ...params }

      for (const item in queryParams) {
        const nullValues = [null, undefined, '']
        if (nullValues.includes(queryParams[item])) { delete queryParams[item] }
      }

      this.$router.replace({
        name,
        query: { ...queryParams }
      }).catch(() => {})
    },
    clearRoute () {
      const { name } = this.$route

      Object.keys(this.filters).forEach((key) => {
        this.filters[key] = null
      }
      )

      this.$router.replace({
        name,
        query: {}
      }).catch(() => {})
    },
    setFilters () {
      const { query } = this.$route
      const queryParamedFilters = {}

      Object.entries(query).forEach(([key, value]) => {
        const camelCaseKey = _.camelCase(key)
        queryParamedFilters[camelCaseKey] = value
      })

      this.filters = queryParamedFilters
    }
  }

}
