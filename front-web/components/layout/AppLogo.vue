<template>
  <nuxt-link to="/">
    <a-image
      src="https://abocados-s3-bucket.s3.eu-west-3.amazonaws.com/logo.svg"
      :width="width"
      :height="height"
    />
  </nuxt-link>
</template>

<script>
export default {
  name: 'AppLogo',
  props: {
    width: {
      type: String,
      required: false,
      default: '250'
    },
    height: {
      type: String,
      required: false,
      default: '250'
    }
  }
}
</script>
