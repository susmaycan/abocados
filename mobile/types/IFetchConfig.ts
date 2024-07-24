import { EHttpMethod } from './EHttpMethod'
import { IFormData } from './IFormData'

// Input data from components
export interface IFetchConfig {
  method?: EHttpMethod
  body?: IFormData
  params?: Record<string, string>
}

// Used to call fetch
export interface IFetchOptions {
  method: EHttpMethod
  headers?: Record<string, string>
  body?: FormData
  params?: Record<string, string | number>
}

export interface IFieldErrors {
  [key: string]: string[]
}
export type IServerErrors = IFieldErrors | { non_field_errors?: string[] }

export interface IFetchErrors {
  fieldErrors?: IFieldErrors
  generalErrors?: string[]
}
