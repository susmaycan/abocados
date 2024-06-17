export default $axios => (resource, sublist) => ({
  list (queryParams = {}) {
    return $axios.$get(`/${resource}/`, { params: queryParams })
  },

  create (payload) {
    return $axios.$post(`/${resource}/`, payload)
  },

  findOne (id) {
    return $axios.$get(`/${resource}/${id}/`)
  },

  update (id, payload) {
    return $axios.$put(`/${resource}/${id}/`, payload)
  },

  delete (id) {
    return $axios.$delete(`/${resource}/${id}/`)
  },

  sublist (id, queryParams = {}) {
    return $axios.$get(`/${resource}/${id}/${sublist}/`, { params: queryParams })
  }
})
