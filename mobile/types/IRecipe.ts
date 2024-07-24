import { ICategory } from './ICategory'

export interface IRecipe {
  id: number
  name: string
  rating?: number
  ingredients?: string
  directions?: string
  picture?: string
  duration?: number
  servings?: number
  created_at: string
  creator: {
    id: number
    username: string
  }
  categories: ICategory[]
  favourited: boolean
}
