import AButton from '@/components/AButton'
import ATextInput from '@/components/ATextInput'
import { IFormData } from '@/types/IFormData'
import useForm from '@/hooks/useForm'
import { HelperText } from 'react-native-paper'
import { IFetchErrors } from '@/types/IFetchConfig'
import { StyleSheet, View } from 'react-native'

interface LoginFormProps {
  isLoading: boolean
  serverErrors?: IFetchErrors | null
  submit: (formData: IFormData) => void
}

export default function LoginForm({
  isLoading,
  serverErrors,
  submit,
}: LoginFormProps) {
  const handleLogin = (formData: IFormData) => {
    submit(formData)
  }

  const { onSubmit, updateForm, formData } = useForm({
    submit: handleLogin,
    initialData: { email: '', password: '' },
  })

  return (
    <View style={styles.form}>
      <ATextInput
        errors={
          serverErrors?.fieldErrors ? serverErrors?.fieldErrors.email : []
        }
        isRequired={true}
        label="Email"
        value={formData.email as string}
        onChange={(e: string) => updateForm('email', e)}
      />
      <ATextInput
        errors={
          serverErrors?.fieldErrors ? serverErrors?.fieldErrors.password : []
        }
        isRequired={true}
        label="Password"
        value={formData.password as string}
        type="password"
        onChange={(e: string) => updateForm('password', e)}
      />
      {serverErrors?.generalErrors &&
        serverErrors?.generalErrors.map((error) => (
          <HelperText type="error" visible={!!error} key={error}>
            {error}
          </HelperText>
        ))}
      <AButton
        isLoading={isLoading}
        onPress={(event) => onSubmit(event)}
        title="Login"
      />
    </View>
  )
}

const styles = StyleSheet.create({
  form: {
    width: '80%',
    gap: 7,
    rowGap: 7,
  },
})
