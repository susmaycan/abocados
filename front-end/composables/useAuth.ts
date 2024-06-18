const USER_KEY = 'user'
const TOKEN_KEY = 'token'

export const useAuth = () => {
  const user = useState<IAuthUser | null>(USER_KEY, () => null)
  const token = useState<string | null>(TOKEN_KEY, () => null)

  const isAuthenticated = computed(() => !!token.value && !!user.value)

  const logIn = (authUser: IAuthUser | null, authToken: string | null) => {
    user.value = authUser
    addToLocalStorage(authUser, USER_KEY)

    token.value = authToken
    addToLocalStorage(authToken, TOKEN_KEY)
  }

  const logOut = () => {
    logIn(null, null)
  }

  const initAuthentication = () => {
    const userFromLocalStorage = getFromLocalStorage(USER_KEY)
    const tokenFromLocalStorage = getFromLocalStorage(TOKEN_KEY)
    logIn(userFromLocalStorage, tokenFromLocalStorage)
  }

  return {
    user,
    token,
    isAuthenticated,
    logIn,
    initAuthentication,
    logOut,
  }
}
