import { IUser } from './IUser'

export interface ILoginResponse {
  user: IUser
  access_token: string
}
