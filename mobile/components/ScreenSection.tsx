import { ReactNode } from 'react'
import { StyleSheet, View, Text } from 'react-native'

interface ScreenSectionProps {
  children: ReactNode
  style?: Record<string, string | number>
  title?: string
  [key: string]: any
}
const ScreenSection = ({
  children,
  style,
  title,
  ...otherProps
}: ScreenSectionProps) => (
  <View style={{ ...styles.screenSection, ...style }} {...otherProps}>
    {title && <Text style={styles.sectionTitle}>{title}</Text>}
    {children}
  </View>
)

export default ScreenSection

const styles = StyleSheet.create({
  screenSection: {
    marginBottom: 10,
    padding: 10,
    alignItems: 'center',
    alignContent: 'center',
    backgroundColor: '#fffcfc',
    borderRadius: 10,
    justifyContent: 'center',
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
  },
})
