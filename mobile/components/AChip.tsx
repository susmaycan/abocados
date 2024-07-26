import * as React from 'react'
import { GestureResponderEvent, Text } from 'react-native'
import { Chip } from 'react-native-paper'

interface AChipProps {
  content: string
  icon?: string
  isLoading?: boolean
  onPress?: (event: Event | GestureResponderEvent) => void
}

const AChip = ({ content, icon, onPress }: AChipProps) => (
  <Chip icon={icon} onPress={onPress} style={{ backgroundColor: '#9AD14B' }}>
    <Text style={{ color: 'white' }}>{content}</Text>
  </Chip>
)

export default AChip
