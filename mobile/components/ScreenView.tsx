import { ThemedView } from '@/components/ThemedView'
import { ReactNode } from 'react'
import { StyleSheet } from 'react-native'

interface ScreenViewProps {
  children?: ReactNode
}
export function ScreenView({ children }: ScreenViewProps) {
  return <ThemedView style={styles.screenView}>{children}</ThemedView>
}

const styles = StyleSheet.create({
  screenView: {
    flex: 1,
    padding: 20,
  },
})
