import { ReactNode } from 'react'
import { StyleSheet, View, SafeAreaView } from 'react-native'
import ScreenTitle from '@/components/ScreenTitle'

interface ScreenViewProps {
  title?: string
  children?: ReactNode
}
export function ScreenView({ children, title }: ScreenViewProps) {
  return (
    <SafeAreaView>
      <View style={styles.screenView}>
        {title && <ScreenTitle>{title}</ScreenTitle>}
        <View style={styles.content}>{children}</View>
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  screenView: {
    paddingHorizontal: 20,
    paddingVertical: 30,
    justifyContent: 'center',
    alignItems: 'center',
  },
  content: {
    width: '100%',
  },
})
