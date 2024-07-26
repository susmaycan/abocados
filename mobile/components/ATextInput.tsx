import { View, Text } from 'react-native'
import { HelperText, TextInput } from 'react-native-paper'
import { useState } from 'react'

interface ATextInputProps {
  errors?: string[]
  isRequired?: boolean
  label: string
  onChange: (newValue: string) => void
  type?: 'email' | 'password'
  value: string
}

export default function ATextInput({
  errors,
  isRequired,
  label,
  type,
  value,
  onChange,
}: ATextInputProps) {
  const textLabel = isRequired ? `${label} *` : label

  const [showPassword, setShowPassword] = useState(false)

  const isTypePassword = () => type === 'password'
  return (
    <View>
      <TextInput
        label={textLabel}
        mode="outlined"
        onChangeText={(text) => onChange(text)}
        value={value}
        autoComplete={type}
        secureTextEntry={isTypePassword() && !showPassword}
        right={
          isTypePassword() && (
            <TextInput.Icon
              icon={showPassword ? 'eye-off' : 'eye'}
              onPress={() => setShowPassword(!showPassword)}
            />
          )
        }
      />
      {errors?.map((error) => (
        <HelperText type="error" visible={!!error} key={error}>
          {error}
        </HelperText>
      ))}
    </View>
  )
}
