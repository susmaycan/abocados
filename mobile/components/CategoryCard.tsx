import { TouchableOpacity, StyleSheet, Text, View, Image } from 'react-native'
import { ICategory } from '@/types/ICategory'
import AImage from './AImage'

interface CategoryCardProps {
  category: ICategory
}

export default function CategoryCard({ category }: CategoryCardProps) {
  const searchByCategory = () => {
    // router.push(`/recipes/${recipe.id}`)
  }
  return (
    <TouchableOpacity onPress={searchByCategory}>
      <View style={styles.categoryCard}>
        <AImage
          url={category.picture}
          alt="picture category"
          width={79}
          height={79}
        />
        <Text style={styles.categoryText}>{category.name}</Text>
      </View>
    </TouchableOpacity>
  )
}

const styles = StyleSheet.create({
  categoryCard: {
    width: 150,
    height: 150,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 10,
    alignContent: 'center',
    alignItems: 'center',
    justifyContent: 'center',
    rowGap: 5,
  },
  categoryText: {
    fontSize: 14,
    fontWeight: 700,
  },
})
