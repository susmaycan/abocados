import { ReactNode } from 'react'
import { StyleSheet, Text } from 'react-native'

interface ScreenTitleProps {
  children?: ReactNode
}
const ScreenTitle = ({ children }: ScreenTitleProps) => (
  <Text style={styles.screenTitle}>{children}</Text>
)

export default ScreenTitle

const styles = StyleSheet.create({
  screenTitle: {
    fontSize: 30,
    fontWeight: 'bold',
  },
})
