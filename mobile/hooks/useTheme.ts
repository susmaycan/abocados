import { useColorScheme } from '@/hooks/useColorScheme'

import { DarkTheme, DefaultTheme } from '@react-navigation/native'

export function useTheme() {
  const colorScheme = useColorScheme()

  const isDarkTheme = () => colorScheme === 'dark'

  const selectedTheme = () => (isDarkTheme() ? DarkTheme : DefaultTheme)

  return { isDarkTheme, selectedTheme }
}
