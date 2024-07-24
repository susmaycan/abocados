import { View } from 'react-native'
import { HelperText, TextInput } from 'react-native-paper'

interface ATextInputProps {
  isRequired?: boolean
  errors?: string[]
  label: string
  onChange: (newValue: string) => void
  type?: 'text' | 'password'
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
  const hasErrors = () => !!errors

  const textLabel = isRequired ? `${label} *` : label

  //   const displayedValue = type === 'password' ? value.replace(/./g, '*') : value
  return (
    <View>
      <TextInput
        label={textLabel}
        mode="outlined"
        onChangeText={(text) => onChange(text)}
        value={value}
      />
      {errors?.map((error) => (
        <HelperText type="error" visible={!!error} key={error}>
          {error}
        </HelperText>
      ))}
    </View>
  )
}
