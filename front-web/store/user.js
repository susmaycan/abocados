export const state = () => ({
  user: null,
  token: null,
})

export const mutations = {
  setUser(state, data) {
    state.user = data.user
    state.token = data.token
  },
}

export const actions = {
  setUserData({ commit }, data) {
    commit('setUser', { ...data, token: data.access_token })
    this.$cookies.set('user', data.user)
    this.$cookies.set('token', data.access_token)
  },
  removeUserData({ commit }) {
    commit('setUser', { user: null, token: null })
    this.$cookies.removeAll()
  },
}
export const getters = {
  isLoggedIn(state) {
    return !!state.token && !!state.user
  },
}
