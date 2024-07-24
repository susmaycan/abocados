import { useEffect } from 'react'
import { Text } from 'react-native'
import { router } from 'expo-router'

import { useAuth } from '@/hooks/useAuth'
import useAPI from '@/hooks/useAPI'

import AImage from '@/components/AImage'
import { ScreenView } from '@/components/ScreenView'
import LoginForm from '@/components/Form/Login'

import { IFormData } from '@/types/IFormData'
import { EHttpMethod } from '@/types/EHttpMethod'
import { ILoginResponse } from '@/types/ILoginResponse'

export default function LoginScreen() {
  const { login } = useAuth()

  const { fetchData, data, errors, isLoading } = useAPI<ILoginResponse>()

  const handleLogin = async (formData: IFormData) => {
    await fetchData('auth/login', {
      body: formData,
      method: EHttpMethod.POST,
    })
  }

  useEffect(() => {
    if (data) {
      login(data.user, data.access_token)
      router.replace('/')
    }
  }, [data])

  return (
    <ScreenView title="Login">
      <AImage
        alt="Abocados logo"
        height={200}
        url="https://abocados-s3-bucket.s3.eu-west-3.amazonaws.com/logo.png"
        width={200}
      />
      <Text>Type your email and password to access</Text>
      <LoginForm
        isLoading={isLoading}
        serverErrors={errors}
        submit={handleLogin}
      />
    </ScreenView>
  )
}
