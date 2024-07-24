import { IRecipe } from './IRecipe'

export interface IRecipeList {
  count: number
  next?: number
  previous?: number
  results: IRecipe[]
}
