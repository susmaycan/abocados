import { IFormData } from '@/types/IFormData'
import { useState } from 'react'

interface UseFormProps {
  submit(newValue: IFormData): void
  initialData: IFormData
}

export default function useForm({ submit, initialData }: UseFormProps) {
  const [formData, setFormData] = useState<IFormData>(initialData)

  const onSubmit = (event: any): void => {
    event.preventDefault()
    submit(formData)
  }

  const updateForm = (key: string, value: string | number) => {
    setFormData({ ...formData, [key]: value })
  }

  return { formData, updateForm, onSubmit }
}
