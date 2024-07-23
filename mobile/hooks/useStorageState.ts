import * as SecureStore from 'expo-secure-store'
import * as React from 'react'
import { Platform } from 'react-native'

type UseStateHook<T> = [[boolean, T | null], (value: T | null) => void]

function useAsyncState<T>(
  initialValue: [boolean, T | null] = [true, null]
): UseStateHook<T> {
  return React.useReducer(
    (
      state: [boolean, T | null],
      action: T | null = null
    ): [boolean, T | null] => [false, action],
    initialValue
  ) as UseStateHook<T>
}

export async function setStorageItemAsync(key: string, value: string | null) {
  if (Platform.OS === 'web') {
    try {
      if (value === null) {
        localStorage.removeItem(key)
      } else {
        localStorage.setItem(key, value)
      }
    } catch (e) {
      console.error('Local storage is unavailable:', e)
    }
  } else {
    if (value == null) {
      await SecureStore.deleteItemAsync(key)
    } else {
      await SecureStore.setItemAsync(key, value)
    }
  }
}

export function useStorageState<T>(key: string): UseStateHook<T> {
  // Public
  const [state, setState] = useAsyncState<T>()

  // Get
  React.useEffect(() => {
    if (Platform.OS === 'web') {
      try {
        if (typeof localStorage !== 'undefined') {
          const localStorageItem = localStorage.getItem(key)
            ? (JSON.parse(localStorage.getItem(key)!) as T)
            : null
          setState(localStorageItem)
        }
      } catch (e) {
        console.error('Local storage is unavailable:', e)
      }
    } else {
      SecureStore.getItemAsync(key).then((value) => {
        const parsedValue = value ? (JSON.parse(value) as T) : null
        setState(parsedValue)
      })
    }
  }, [key])

  // Set
  const setValue = React.useCallback(
    (value: T | null) => {
      setState(value)

      const stringValue = JSON.stringify(value)
      setStorageItemAsync(key, stringValue)
    },
    [key]
  )

  return [state, setValue]
}
