import { theme, language } from '@/constants/config'

export const state = () => ({
  language: language.spanish,
  theme: theme.dark,
})

export const mutations = {
  setLanguage(state, language) {
    state.language = language
    localStorage.setItem('language', language)
  },
  setTheme(state, _theme) {
    state.theme = _theme
    localStorage.setItem('theme', _theme)
  },
}

export const getters = {
  getTheme(state) {
    return state.theme
  },
  getLanguage(state) {
    return state.language
  },
}

export const actions = {
  async loadInitialConfig({ commit }) {
    const localStorageLang =
      localStorage.getItem('language') || language.spanish
    const localStorageTheme = localStorage.getItem('theme') || theme.dark

    commit('setLanguage', localStorageLang)
    commit('setTheme', localStorageTheme)
  },
}
