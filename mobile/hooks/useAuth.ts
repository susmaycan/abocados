import { AuthContext } from '@/context/AuthContext'
import { IUser } from '@/types/IUser'
import { useContext, useEffect } from 'react'
export const useAuth = () => {
  const { user, token, login, logout } = useContext(AuthContext)

  const isAuthenticated = () => !!user && !!token

  return {
    user,
    token,
    login,
    logout,
    isAuthenticated,
  }
}
