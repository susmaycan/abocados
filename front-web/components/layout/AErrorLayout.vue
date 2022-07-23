<template>
  <v-container>
    <page-layout :title="$t(title) | capitalize">
      <p>{{ $t(message) | capitalize }}</p>
      <a-button
        class="my-2"
        @click="$router.push({ name: 'index' })"
      >
        {{ $t("go_home") | capitalize }}
      </a-button>
    </page-layout>
  </v-container>
</template>

<script>
import { HTTP_ERROR_CODES } from '@/utils/consts'

export default {
  name: 'AErrorLayout',
  props: {
    error: {
      type: Number,
      default: null
    }
  },
  head () {
    return {
      title: this.$t(this.title)
    }
  },
  computed: {
    title () {
      if (!this.error) {
        return ''
      }
      return {
        [HTTP_ERROR_CODES.NOT_FOUND]: 'not_found_error',
        [HTTP_ERROR_CODES.FORBIDDEN]: 'forbidden_error',
        [HTTP_ERROR_CODES.UNAUTHORIZED]: 'forbidden_error',
        [HTTP_ERROR_CODES.SERVER]: 'server_error'
      }[this.error]
    },
    message () {
      if (!this.error) {
        return ''
      }
      return {
        [HTTP_ERROR_CODES.NOT_FOUND]: 'not_found_error_message',
        [HTTP_ERROR_CODES.FORBIDDEN]: 'forbidden_error_message',
        [HTTP_ERROR_CODES.UNAUTHORIZED]: 'forbidden_error_message',
        [HTTP_ERROR_CODES.SERVER]: 'server_error_message'
      }[this.error]
    }
  }
}
</script>
