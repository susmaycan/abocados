import { Redirect, Stack } from 'expo-router'
import { useAuth } from '@/hooks/useAuth'

export default function AppLayout() {
  const { isAuthenticated } = useAuth()

  if (!isAuthenticated()) {
    return <Redirect href="/login" />
  }

  // This layout can be deferred because it's not the root layout.
  return (
    <Stack>
      <Stack.Screen title="TABS" name="(tabs)" />
    </Stack>
  )
}
