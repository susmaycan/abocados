import { useAuth } from '@/hooks/useAuth'
import { Text, View } from 'react-native'

export default function Index() {
  const { user, token, logout } = useAuth()

  return (
    <View
      style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Text>
        Auth screen -- {user?.name} ^ {token}
      </Text>
      <Text onPress={() => logout()}>Logout</Text>
    </View>
  )
}
