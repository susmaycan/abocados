import { View, type ViewProps } from 'react-native'

import { useThemeColor } from '@/hooks/useThemeColor'

export type ThemedViewProps = ViewProps & {
  lightColor?: string
  darkColor?: string
}

export function ThemedView({ style, ...otherProps }: ThemedViewProps) {
  const backgroundColor = useThemeColor(
    { light: '#A1CEDC', dark: '#1D3D47' },
    'background'
  )

  return <View style={[{ backgroundColor }, style]} {...otherProps} />
}
