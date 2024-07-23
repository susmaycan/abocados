import { useAuth } from '@/hooks/useAuth'
import { Text, View } from 'react-native'
import { router } from 'expo-router'

export default function LoginScreen() {
  const { login } = useAuth()

  const handleLogin = () => {
    console.log('Handling click')
    login(
      { id: 1, name: 'Phoebe Buffay', email: 'phoebe_buffay@friends.com' },
      'patatatassss!!'
    )
    router.replace('/')
  }

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text onPress={() => handleLogin()}>Login</Text>
    </View>
  )
}
