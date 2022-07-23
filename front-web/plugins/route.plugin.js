export default ({ app, store }) => {
  app.router.afterEach(() => {
    store.commit('setError', null)
  })
}
