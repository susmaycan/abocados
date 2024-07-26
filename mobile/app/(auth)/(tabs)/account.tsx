import AButton from '@/components/AButton'
import Loader from '@/components/Loader'
import ScreenSection from '@/components/ScreenSection'
import ScreenTitle from '@/components/ScreenTitle'
import { ScreenView } from '@/components/ScreenView'
import UserDetail from '@/components/User/Detail'
import { useAuth } from '@/hooks/useAuth'

export default function Index() {
  const { user, logout } = useAuth()

  if (user)
    return (
      <ScreenView>
        <ScreenSection>
          <ScreenTitle>My account</ScreenTitle>
        </ScreenSection>
        <UserDetail user={user} />
        <ScreenSection>
          <AButton
            title="Edit profile"
            onPress={() => console.log('Edit profile')}
          />
          <AButton
            title="Delete profile"
            onPress={() => console.log('Delete profile')}
          />
          <AButton title="Logout" onPress={() => logout()} />
        </ScreenSection>
      </ScreenView>
    )
  else return <Loader />
}
