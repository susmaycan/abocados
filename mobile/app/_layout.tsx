import { Slot } from 'expo-router'
import { SessionProvider } from '@/components/SessionProvider'
import { MD3LightTheme, PaperProvider } from 'react-native-paper'

const RootScreen = () => {
  const theme = {
    ...MD3LightTheme, // or MD3DarkTheme
    // roundness: 2,
    colors: {
      ...MD3LightTheme.colors,
      primary: '#9AD14B',
      secondary: '#f1c40f',
      tertiary: '#a1b2c3',
    },
  }

  return (
    <SessionProvider>
      <PaperProvider theme={theme}>
        <Slot />
      </PaperProvider>
    </SessionProvider>
  )
}

export default RootScreen
