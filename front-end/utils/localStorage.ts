export const addToLocalStorage = (dataToStore: any, key: string): void => {
  const jsonData = JSON.stringify(dataToStore)
  localStorage.setItem(key, jsonData)
}

export const getFromLocalStorage = (key: string) => {
  const item = localStorage.getItem(key)
  return item ? JSON.parse(item) : null
}
export const removeFromLocalStorage = (key: string): void => {
  localStorage.removeItem(key)
}
