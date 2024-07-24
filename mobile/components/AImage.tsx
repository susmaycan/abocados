import React from 'react'
import { Image } from 'react-native'

interface AImageProps {
  alt: string
  height?: number
  url: string
  width?: number
}
const AImage = ({ url, alt, width, height }: AImageProps) => {
  return (
    <Image
      alt={alt}
      source={{
        uri: url,
      }}
      style={{ width: width || 100, height: height || 100 }}
    />
  )
}

export default AImage
