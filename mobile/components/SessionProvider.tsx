import { AuthContext } from '@/context/AuthContext'
import { useStorageState } from '@/hooks/useStorageState'
import { IUser } from '@/types/IUser'
import { PropsWithChildren } from 'react'

export const SessionProvider = ({ children }: PropsWithChildren) => {
  const [[isLoading, tokenState], setTokenState] =
    useStorageState<string>('token')
  const [[isLoadingUser, userState], setUserState] =
    useStorageState<IUser>('user')

  return (
    <AuthContext.Provider
      value={{
        user: userState,
        token: tokenState,
        login: (user: IUser, newToken: string) => {
          setUserState(user)
          setTokenState(newToken)
        },
        logout: () => {
          setUserState(null)
          setTokenState(null)
        },
      }}
    >
      {children}
    </AuthContext.Provider>
  )
}
