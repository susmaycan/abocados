export default $axios => (resource, sublist) => ({
  list (id, queryParams = {}) {
    return $axios.$get(`/${resource}/${id}/${sublist}/`, { params: queryParams })
  },
  add (id, payload) {
    return $axios.$post(`/${resource}/${id}/${sublist}/add/`, payload)
  },
  delete (id, payload) {
    return $axios.$post(`/${resource}/${id}/${sublist}/delete/`, payload)
  }
})
