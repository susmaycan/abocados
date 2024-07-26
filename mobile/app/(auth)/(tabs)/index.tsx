import { useEffect } from 'react'

import CategoryCard from '@/components/CategoryCard'
import Loader from '@/components/Loader'
import RecipeCard from '@/components/Recipe/Card'
import ScreenSection from '@/components/ScreenSection'
import ScreenTitle from '@/components/ScreenTitle'
import { ScreenView } from '@/components/ScreenView'
import ScrollList from '@/components/ScrollList'

import useAPI from '@/hooks/useAPI'

import { ICategoryList } from '@/types/ICategoryList'
import { IRecipeList } from '@/types/IRecipeList'

export default function Index() {
  const {
    fetchData: fetchRecipes,
    data: recipeData,
    isLoading: isLoadingRecipes,
  } = useAPI<IRecipeList>()
  const {
    fetchData: fetchCategories,
    data: categoriesData,
    isLoading: isLoadingCategories,
  } = useAPI<ICategoryList>()

  useEffect(() => {
    fetchCategories('categories')
    fetchRecipes('recipes', { params: { limit: '8' } })
  }, [])

  const recipeList = () => {
    return recipeData ? recipeData.results : []
  }

  const categoryList = () => {
    return categoriesData ? categoriesData.results : []
  }

  return (
    <ScreenView>
      <ScreenSection>
        <ScreenTitle>aBocados 🥑</ScreenTitle>
      </ScreenSection>
      <ScreenSection title="Search by category">
        <ScrollList horizontal={true}>
          {isLoadingCategories && <Loader />}
          {!isLoadingCategories &&
            categoryList().map((category) => (
              <CategoryCard key={category.id} category={category} />
            ))}
        </ScrollList>
      </ScreenSection>
      <ScreenSection title="Latest recipes">
        <ScrollList horizontal={true}>
          {isLoadingRecipes && <Loader />}
          {!isLoadingRecipes &&
            recipeList().map((recipe) => (
              <RecipeCard key={recipe.id} recipe={recipe} />
            ))}
        </ScrollList>
      </ScreenSection>
    </ScreenView>
  )
}
