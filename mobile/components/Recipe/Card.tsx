import { router } from 'expo-router'
import { Text, TouchableOpacity, StyleSheet, View } from 'react-native'

import AImage from '@/components/AImage'
import { Icon } from '@/components/Icon'

import { IRecipe } from '@/types/IRecipe'

interface RecipeCardProps {
  recipe: IRecipe
}

export default function RecipeCard({ recipe }: RecipeCardProps) {
  const navigateToDetailPage = () => {
    router.push(`/recipes/${recipe.id}`)
  }
  return (
    <TouchableOpacity onPress={navigateToDetailPage}>
      <View style={styles.recipeCard}>
        <AImage
          url={
            recipe.picture ||
            'https://abocados-s3-bucket.s3.eu-west-3.amazonaws.com/recipes/no_photo'
          }
          alt={`Picture of ${recipe.name}`}
          width={200}
          height={200}
          style={styles.recipeImage}
        />
        <Text style={styles.recipeTitle}>{recipe.name}</Text>
        <View style={styles.recipeInfoContainer}>
          <View style={styles.recipeDuration}>
            <Icon name="clock-time-eight" size={20} />
            <Text>{recipe.duration}</Text>
          </View>
          <View style={styles.recipeDuration}>
            <Icon name="star" size={20} color="#FFC165" />
            <Text>{recipe.rating}</Text>
          </View>
        </View>
      </View>
    </TouchableOpacity>
  )
}

const styles = StyleSheet.create({
  recipeCard: {
    width: 200,
    height: 270,
    alignContent: 'center',
    alignItems: 'center',
    justifyContent: 'center',
    rowGap: 5,
  },
  recipeImage: {
    borderRadius: 10,
  },
  recipeTitle: {
    fontSize: 16,
    fontWeight: 600,
  },
  recipeDuration: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    gap: 3,
  },
  recipeInfoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
})
