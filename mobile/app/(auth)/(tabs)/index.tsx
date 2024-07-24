import AImage from '@/components/AImage'
import Loader from '@/components/Loader'
import { ScreenView } from '@/components/ScreenView'
import useAPI from '@/hooks/useAPI'
import { useAuth } from '@/hooks/useAuth'
import { IRecipeList } from '@/types/IRecipeList'
import { useEffect } from 'react'
import { Text, View } from 'react-native'

export default function Index() {
  const { user, logout } = useAuth()

  const { fetchData, data, errors, isLoading } = useAPI<IRecipeList>()

  useEffect(() => {
    fetchData('recipes', { params: { limit: '8' } })
  }, [])

  const recipeList = () => {
    return data ? data.results : []
  }

  return (
    <ScreenView title="Welcome!">
      <Text>Welcome back {user?.name}</Text>

      {isLoading ? (
        <Loader />
      ) : (
        <View>
          <Text>View all these recipes for you!</Text>
          {recipeList().map((recipe) => (
            <View key={recipe.id}>
              {recipe.picture && (
                <AImage url={recipe.picture} alt="Picture of food" />
              )}
              <Text>{recipe.name}</Text>
            </View>
          ))}
        </View>
      )}
    </ScreenView>
  )
}
