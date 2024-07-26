import Loader from '@/components/Loader'
import RecipeCard from '@/components/Recipe/Card'
import ScreenSection from '@/components/ScreenSection'
import ScreenTitle from '@/components/ScreenTitle'
import { ScreenView } from '@/components/ScreenView'
import ScrollList from '@/components/ScrollList'
import useAPI from '@/hooks/useAPI'
import { useAuth } from '@/hooks/useAuth'
import { IRecipeList } from '@/types/IRecipeList'
import { useEffect } from 'react'
import { Text } from 'react-native'

export default function Recipes() {
  const { user } = useAuth()

  const { fetchData, data, errors, isLoading } = useAPI<IRecipeList>()

  useEffect(() => {
    fetchData(`users/${user?.id}/recipes`)
  }, [])

  const recipeList = () => {
    return data ? data.results : []
  }

  return (
    <ScreenView>
      <ScreenSection>
        <ScreenTitle>My recipes</ScreenTitle>
        <Text>View saved recipes</Text>
      </ScreenSection>
      <ScreenSection>
        <ScrollList>
          {isLoading && <Loader />}
          {!isLoading &&
            recipeList().map((recipe) => (
              <RecipeCard key={recipe.id} recipe={recipe} />
            ))}
        </ScrollList>
      </ScreenSection>
    </ScreenView>
  )
}
