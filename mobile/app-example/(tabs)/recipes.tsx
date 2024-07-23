import { ThemedText } from '@/components/ThemedText'
import { ThemedView } from '@/components/ThemedView'
import { ScreenView } from '@/components/ScreenView'

export default function TabTwoScreen() {
  return (
    <ScreenView>
      <ThemedView>
        <ThemedText type="title">Recipes list</ThemedText>
      </ThemedView>
    </ScreenView>
  )
}
