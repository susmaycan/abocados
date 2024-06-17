import createRepository from '../services/repository.services'
import createFavouriteRepository from '../services/favourites.services'
import createAuthRepository from '../services/auth.services'
import { HTTP_ERROR_CODES } from '../utils/consts'

export default ({ store, $axios, i18n, $config }, inject) => {
  const repositoryWithAxios = createRepository($axios)
  const authRepositoryWithAxios = createAuthRepository($axios)
  const favouriteRepositoryWithAxios = createFavouriteRepository($axios)

  $axios.onRequest((config) => {
    config.baseURL = $config.server
    const language = i18n.localeProperties?.code || 'en'
    config.headers.common['Accept-Language'] = language

    const token = store?.state?.user?.token
    config.headers.common.Authorization = token ? `Token ${token}` : null
    config.headers.common['Content-Type'] =
      'multipart/form-data;boundary=BoUnDaRyStRiNg'

    // Transform data into form data
    if (config.data) {
      const { data } = config
      const formData = new FormData()
      for (const key in data) {
        const value = data[key]
        if (value) {
          if (Array.isArray(value)) {
            for (const arrayEl in value) {
              formData.append(key, value[arrayEl])
            }
          } else {
            formData.append(key, value)
          }
        }
      }
      config.data = formData
    }

    // Transform query params
    if (config.params) {
      const { params } = config
      const urlParams = new URLSearchParams()
      for (const key in params) {
        const value = params[key]
        if (value) {
          if (Array.isArray(value)) {
            for (const arrayEl in value) {
              urlParams.append(key, value[arrayEl])
            }
          } else {
            urlParams.append(key, value)
          }
        }
      }
      config.params = urlParams
    }
    store.commit('setIsLoading', true)
  })

  $axios.onResponse((data, headers) => {
    store.commit('setIsLoading', false)
  })

  $axios.onResponseError(({ response }) => {
    store.commit('setIsLoading', false)
    if (
      response &&
      response.data &&
      response.status === HTTP_ERROR_CODES.BAD_REQUEST
    ) {
      return Promise.reject(response.data)
    } else {
      store.commit('setError', response)
      return Promise.reject(response)
    }
  })

  const apiFinal = {
    recipe: repositoryWithAxios('recipes'),
    user: repositoryWithAxios('users', 'recipes'),
    auth: authRepositoryWithAxios('auth'),
    category: repositoryWithAxios('categories'),
    meal: repositoryWithAxios('meals'),
    favourite: favouriteRepositoryWithAxios('users', 'favourites'),
  }

  inject('api', apiFinal)
}
