import { Redirect, Stack } from 'expo-router'
import { useAuth } from '@/hooks/useAuth'

export default function AppLayout() {
  const { isAuthenticated } = useAuth()

  if (!isAuthenticated()) {
    return <Redirect href="/login" />
  }

  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="recipes/[id]" />
    </Stack>
  )
}
