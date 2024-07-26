import { Text, StyleSheet, View, TouchableOpacity } from 'react-native'

import AImage from '@/components/AImage'
import { Icon } from '@/components/Icon'
import ScreenSection from '@/components/ScreenSection'
import ScreenTitle from '@/components/ScreenTitle'
import ScrollList from '@/components/ScrollList'
import AChip from '@/components/AChip'

import { IRecipe } from '@/types/IRecipe'
import { router } from 'expo-router'

interface RecipeDetailProps {
  recipe: IRecipe
}

const RecipeDetail = ({ recipe }: RecipeDetailProps) => {
  const goToUserProfile = () => {
    router.push(`/users/${recipe.creator.id}`)
  }
  return (
    <ScrollList style={styles.scrollView}>
      <ScreenSection style={styles.container}>
        <AImage
          url={
            recipe.picture ||
            'https://abocados-s3-bucket.s3.eu-west-3.amazonaws.com/recipes/no_photo'
          }
          alt={`Picture of ${recipe.name}`}
          width={300}
          height={300}
          style={styles.recipeImage}
        />
        <ScreenTitle>{recipe.name}</ScreenTitle>
        <View style={styles.recipeInfoContainer}>
          <View style={styles.recipeInfo}>
            <Icon name="clock-time-eight" size={20} />
            <Text>{recipe.duration} min</Text>
          </View>
          <View style={styles.recipeInfo}>
            <Icon name="star" size={20} color="#FFC165" />
            <Text>{recipe.rating}</Text>
          </View>
        </View>
        <View style={styles.recipeInfoContainer}>
          <View style={styles.recipeInfo}>
            <Icon name="silverware-fork-knife" size={20} />
            <Text>{recipe.servings} servings</Text>
          </View>
        </View>
        <View style={styles.recipeInfoContainer}>
          {recipe.categories.map((category) => (
            <AChip key={category.id} content={category.name} />
          ))}
        </View>
        <View style={styles.recipeInfoContainer}>
          <TouchableOpacity onPress={goToUserProfile}>
            <View style={styles.recipeInfo}>
              <Icon name="chef-hat" size={20} />
              <Text>
                Created by{' '}
                <Text style={styles.creator}>@{recipe.creator.username}</Text>
              </Text>
            </View>
          </TouchableOpacity>
        </View>
        <Text style={styles.recipeSubTitle}>Ingredients</Text>
        <Text>{recipe.ingredients}</Text>
        <Text style={styles.recipeSubTitle}>Directions</Text>
        <Text>{recipe.directions}</Text>
      </ScreenSection>
    </ScrollList>
  )
}

export default RecipeDetail

const styles = StyleSheet.create({
  container: {
    gap: 10,
    paddingVertical: 20,
  },
  scrollView: {
    padding: 0,
  },
  recipeImage: {
    borderRadius: 10,
  },
  recipeSubTitle: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  recipeInfo: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    gap: 3,
  },
  recipeInfoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    flexWrap: 'wrap',
  },
  creator: {
    fontWeight: 'bold',
  },
})
