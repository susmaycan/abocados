import { View, StyleSheet, ScrollView, SafeAreaView } from 'react-native'
import { ReactNode } from 'react'

interface ScrollListProps {
  children: ReactNode
  horizontal?: boolean
  style?: Record<string, string | number>
}

export default function ScrollList({
  children,
  horizontal,
  style,
}: ScrollListProps) {
  return (
    <ScrollView
      horizontal={horizontal}
      contentContainerStyle={{ ...styles.contentContainer, ...style }}
    >
      {children}
    </ScrollView>
  )
}

const styles = StyleSheet.create({
  contentContainer: {
    gap: 20,
    padding: 10,
  },
})
