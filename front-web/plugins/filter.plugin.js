import Vue from 'vue'

export default () => {
  Vue.filter('capitalize', function (value) {
    if (!value) { return '' }

    return value.charAt(0).toUpperCase() + value.slice(1)
  })

  Vue.filter('uppercase', function (value) {
    if (!value) { return '' }

    return value.toUpperCase()
  })
}
