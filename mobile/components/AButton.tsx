import { GestureResponderEvent } from 'react-native'
import { Button } from 'react-native-paper'

interface AButtonProps {
  icon?: string
  isLoading?: boolean
  onPress: (event: Event | GestureResponderEvent) => void
  title: string
}

export default function AButton({
  icon,
  isLoading,
  onPress,
  title,
}: AButtonProps) {
  return (
    <Button
      icon={icon}
      loading={isLoading}
      mode="contained"
      onPress={(event) => onPress(event)}
    >
      {title}
    </Button>
  )
}
