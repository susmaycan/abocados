import { ICategory } from './ICategory'

export interface ICategoryList {
  count: number
  next?: number
  previous?: number
  results: ICategory[]
}
