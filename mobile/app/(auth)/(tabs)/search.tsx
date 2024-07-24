import AButton from '@/components/AButton'
import { ScreenView } from '@/components/ScreenView'
import { useAuth } from '@/hooks/useAuth'
import { Text, View } from 'react-native'

export default function Index() {
  const { user, logout } = useAuth()

  return (
    <ScreenView title="Search recipes">
      <Text>Here you can search your recipes</Text>
    </ScreenView>
  )
}
