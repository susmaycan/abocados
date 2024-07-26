import { Text, StyleSheet } from 'react-native'

import AImage from '@/components/AImage'

import ScreenSection from '../ScreenSection'
import ScreenTitle from '../ScreenTitle'
import { IUser } from '@/types/IUser'

interface IUserDetailProps {
  user: IUser
}

const UserDetail = ({ user }: IUserDetailProps) => {
  return (
    <ScreenSection style={styles.userProfileSection}>
      {user.picture && (
        <AImage
          alt={`Picture of ${user.name}`}
          url={user.picture}
          style={styles.userProfilePicture}
        />
      )}
      <ScreenTitle>@{user.username}</ScreenTitle>
      <Text>{user.name}</Text>
      <Text>{user.email}</Text>
    </ScreenSection>
  )
}

export default UserDetail

const styles = StyleSheet.create({
  userProfilePicture: {
    borderRadius: 50,
  },
  userProfileSection: {
    paddingVertical: 40,
    gap: 10,
  },
})
