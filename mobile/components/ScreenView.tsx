import { ReactNode } from 'react'
import { StyleSheet, View, Text } from 'react-native'

interface ScreenViewProps {
  title?: string
  children?: ReactNode
}
export function ScreenView({ children, title }: ScreenViewProps) {
  return (
    <View style={styles.screenView}>
      <Text style={styles.screenTitle}>{title}</Text>
      {children}
    </View>
  )
}

const styles = StyleSheet.create({
  screenTitle: {
    fontSize: 30,
    fontWeight: 'bold',
  },
  screenView: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
    alignItems: 'center',
    gap: 5,
    rowGap: 5,
  },
})
