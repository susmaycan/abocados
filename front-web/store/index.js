export const state = () => ({
  loading: false,
  error: null,
  categories: []
})

export const strict = false

export const mutations = {
  setIsLoading (state, loading) {
    state.loading = loading
  },
  setError (state, error) {
    state.error = error
  },
  setCategories (state, categories) {
    state.categories = categories
  }
}

export const actions = {
  async loadCategories ({ commit }) {
    try {
      const response = await this.$api.category.list()
      return commit('setCategories', response.results)
    } catch (error) {
      return Promise.resolve(false)
    }
  },
  nuxtServerInit ({ commit }, context) {
    commit('setIsLoading', true)
    const user = context.app.$cookies.get('user')
    const token = context.$cookies.get('token')
    if (token) {
      commit('user/setUser', { user, access_token: token })
    }
    commit('setIsLoading', false)
  }
}
