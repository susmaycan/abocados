import { IUser } from '@/types/IUser'
import { createContext } from 'react'

interface AuthContext {
  token: string | null
  login: (user: IUser, token: string) => void
  logout: () => void
  user: IUser | null
}

export const AuthContext = createContext<AuthContext>({
  token: null,
  login: () => null,
  logout: () => null,
  user: null,
})
