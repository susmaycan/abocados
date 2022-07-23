export const state = () => ({
  user: null,
  token: null,
  loggedIn: false
})

export const mutations = {
  setUser (state, data) {
    state.user = data.user
    state.token = data.access_token
    state.loggedIn = true
    this.$cookies.set('user', data.user)
    this.$cookies.set('token', data.access_token)
  },
  removeUser (state) {
    state.user = null
    state.token = null
    state.loggedIn = false
    this.$cookies.removeAll()
  }
}
