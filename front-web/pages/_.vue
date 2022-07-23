<template>
  <a-error-layout :error="HTTP_ERROR_CODES.NOT_FOUND" />
</template>
<script>
import { HTTP_ERROR_CODES } from '@/utils/consts'
export default {
  name: 'NotFound',
  data () {
    return {
      HTTP_ERROR_CODES
    }
  }
}
</script>
