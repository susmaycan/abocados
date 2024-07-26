import Loader from '@/components/Loader'
import { ScreenView } from '@/components/ScreenView'
import useAPI from '@/hooks/useAPI'
import { useEffect } from 'react'
import { Stack, useLocalSearchParams } from 'expo-router'
import { PaperProvider } from 'react-native-paper'
import UserDetail from '@/components/User/Detail'
import { IUser } from '@/types/IUser'

export default function UserDetailPage() {
  const params = useLocalSearchParams()

  const userId = () => params.id

  const { fetchData, data, isLoading } = useAPI<IUser>()

  useEffect(() => {
    fetchData(`users/${userId()}`)
  }, [])

  return (
    <PaperProvider>
      <Stack.Screen
        options={{
          title: '',
        }}
      />
      <ScreenView>
        {isLoading || !data ? <Loader /> : <UserDetail user={data!} />}
      </ScreenView>
    </PaperProvider>
  )
}
