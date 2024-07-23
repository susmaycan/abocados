import { Slot } from 'expo-router'
import { SessionProvider } from '@/components/SessionProvider'

const RootScreen = () => {
  return (
    <SessionProvider>
      <Slot />
    </SessionProvider>
  )
}

export default RootScreen
