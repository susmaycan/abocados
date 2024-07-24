import { useState } from 'react'
import { EHttpMethod } from '@/types/EHttpMethod'
import { useAuth } from '@/hooks/useAuth'
import {
  IFetchConfig,
  IFetchErrors,
  IFetchOptions,
  IServerErrors,
} from '@/types/IFetchConfig'

export default function useApi<ResponseType>() {
  const [data, setData] = useState<ResponseType | null>(null)
  const [errors, setErrors] = useState<IFetchErrors | null>(null)
  const [isLoading, setLoading] = useState(false)

  const { token } = useAuth()
  console.log('🚀 ~ token:', token)

  const fetchData = async (route: string, config?: IFetchConfig) => {
    setLoading(true)
    setErrors(null)

    const options: IFetchOptions = {
      method: config?.method || EHttpMethod.GET,
    }

    if (token) {
      options.headers = {
        Authorization: 'Token ' + token,
      }
    }

    const methodsSupportingBody: EHttpMethod[] = [
      EHttpMethod.POST,
      EHttpMethod.PATCH,
      EHttpMethod.PUT,
    ]

    if (config?.body && methodsSupportingBody.includes(options.method)) {
      const formData = new FormData()

      Object.entries(config?.body).forEach(([key, value]) => {
        if (value) {
          formData.append(key, value as string)
        }
      })

      options.body = formData
    }

    const base = `${process.env.EXPO_PUBLIC_API_URL}/${route}/`
    const urlParams = config?.params
      ? `?${new URLSearchParams(config?.params)}`
      : ''

    const url = `${base}${urlParams}`

    console.log('🚀 ~ fetchData ~ url:', url)
    console.log('🚀 ~ fetchData ~ options:', options)

    try {
      const response = await fetch(url, options)

      const dataResponse = await response.json()
      if (response.ok) {
        setData(dataResponse)
        setErrors(null)
      } else {
        const dataError = dataResponse as IServerErrors
        if (dataError.non_field_errors)
          setErrors({ generalErrors: dataError.non_field_errors })
        else setErrors({ fieldErrors: dataError })
        setData(null)
      }
    } catch (error: any) {
      const dataError = error as IServerErrors
      if (dataError.non_field_errors)
        setErrors({ generalErrors: dataError.non_field_errors })
      else setErrors({ fieldErrors: dataError })
      setData(null)
    } finally {
      setLoading(false)
      return data
    }
  }

  return { data, errors, isLoading, fetchData }
}

// src/hooks/useFetchData.ts

// import { useState, useEffect } from 'react';

// interface FetchOptions {
//   method?: string;
//   headers?: Record<string, string>;
//   body?: any;
// }

// interface FetchData<T> {
//   data: T | null;
//   error: string | null;
//   loading: boolean;
// }

// const $fetch = async <T>(url: string, options?: FetchOptions): Promise<T> => {
//   // Assuming $fetch is similar to fetch or axios
//   const response = await fetch(url, {
//     method: options?.method || 'GET',
//     headers: options?.headers,
//     body: JSON.stringify(options?.body),
//   });
//   if (!response.ok) {
//     throw new Error(`Error: ${response.statusText}`);
//   }
//   return response.json();
// };

// const useFetchData = <T,>(url: string, options?: FetchOptions): FetchData<T> => {
//   const [data, setData] = useState<T | null>(null);
//   const [error, setError] = useState<string | null>(null);
//   const [loading, setLoading] = useState<boolean>(false);

//   useEffect(() => {
//     const fetchData = async () => {
//       setLoading(true);
//       try {
//         const result = await $fetch<T>(url, options);
//         setData(result);
//       } catch (err) {
//         setError((err as Error).message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchData();
//   }, [url, options]);

//   return { data, error, loading };
// };

// export default useFetchData;
