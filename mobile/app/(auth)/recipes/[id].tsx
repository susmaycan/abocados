import Loader from '@/components/Loader'
import RecipeDetail from '@/components/Recipe/Detail'
import { ScreenView } from '@/components/ScreenView'
import useAPI from '@/hooks/useAPI'
import { IRecipe } from '@/types/IRecipe'
import { useEffect, useState } from 'react'
import { View } from 'react-native'
import { Stack, useLocalSearchParams, useRouter } from 'expo-router'
import {
  Divider,
  Button,
  IconButton,
  Menu,
  PaperProvider,
} from 'react-native-paper'

export default function Index() {
  const params = useLocalSearchParams()
  const router = useRouter()

  const recipeId = () => params.id

  const { fetchData, data, isLoading } = useAPI<IRecipe>()

  useEffect(() => {
    fetchData(`recipes/${recipeId()}`)
  }, [])

  const recipeName = () => data?.name || 'Recipe'

  const handleDismiss = () => {
    router.dismiss()
  }

  const goToRecipes = () => {
    router.replace('/recipes')
  }

  const canGoBack = () => router.canGoBack()

  const [visible, setVisible] = useState(false)

  const openMenu = () => setVisible(true)

  const closeMenu = () => setVisible(false)
  return (
    <PaperProvider>
      <Stack.Screen
        options={{
          title: recipeName(),
          headerLeft: () => (
            <IconButton
              icon="arrow-left"
              size={20}
              onPress={canGoBack() ? handleDismiss : goToRecipes}
            />
          ),
          headerRight: () => (
            <Menu
              visible={visible}
              onDismiss={closeMenu}
              anchorPosition="bottom"
              anchor={
                <IconButton icon="menu" size={20} onPress={() => openMenu()} />
              }
            >
              <Menu.Item onPress={() => {}} title="Edit recipe" />
              <Menu.Item onPress={() => {}} title="Delete recipe" />
            </Menu>
          ),
        }}
      />
      <ScreenView>
        {isLoading || !data ? <Loader /> : <RecipeDetail recipe={data!} />}
      </ScreenView>
    </PaperProvider>
  )
}
