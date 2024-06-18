const LANGUAGE_KEY = 'language'
const COLOR_MODE_KEY = 'color_mode'

export const useUserConfig = () => {
  const userLanguage = useState<ILanguage>(LANGUAGE_KEY, () => ELanguage.en)
  const colorMode = useState<IColorMode>(COLOR_MODE_KEY, () => EColorMode.dark)

  const themeInstance = useColorMode()
  const localeInstance = useI18n()

  const setLanguage = (lang: ILanguage) => {
    userLanguage.value = lang
    localeInstance.setLocale(lang)
    addToLocalStorage(lang, LANGUAGE_KEY)
  }

  const setColorMode = (color: IColorMode) => {
    colorMode.value = color
    themeInstance.preference = colorMode.value

    addToLocalStorage(color, COLOR_MODE_KEY)
  }

  const initUserConfig = () => {
    const languageFromLocalStorage =
      getFromLocalStorage(LANGUAGE_KEY) || userLanguage.value
    setLanguage(languageFromLocalStorage)

    const colorModeFromLocalStorage =
      getFromLocalStorage(COLOR_MODE_KEY) || colorMode.value
    setColorMode(colorModeFromLocalStorage)
  }

  return { userLanguage, colorMode, setLanguage, setColorMode, initUserConfig }
}
