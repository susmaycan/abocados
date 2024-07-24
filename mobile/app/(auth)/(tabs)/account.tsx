import AButton from '@/components/AButton'
import AImage from '@/components/AImage'
import { ScreenView } from '@/components/ScreenView'
import { useAuth } from '@/hooks/useAuth'
import { Text, View } from 'react-native'

export default function Index() {
  const { user, logout } = useAuth()

  return (
    <ScreenView title="Account">
      {user?.picture && (
        <AImage alt={`Picture of ${user.name}`} url={user.picture} />
      )}
      <Text>Name: {user?.name}</Text>
      <Text>Email: {user?.email}</Text>
      <Text>Username: {user?.username}</Text>
      <AButton title="Logout" onPress={() => logout()} />
    </ScreenView>
  )
}
