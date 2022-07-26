<template>
  <v-container>
    <page-layout :title="$t(title) | capitalize">
      <p>{{ $t(message) | capitalize }}</p>
      <a-button class="my-2" @click="$router.push({ name: 'index' })">
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
      switch (this.error) {
        case HTTP_ERROR_CODES.NOT_FOUND:
          return 'not_found_error'
        case HTTP_ERROR_CODES.UNAUTHORIZED:
        case HTTP_ERROR_CODES.FORBIDDEN:
          return 'forbidden_error'
        case HTTP_ERROR_CODES.INTERNAL_SERVER_ERROR:
          return 'server_error'
        default: {
          return 'server_error'
        }
      }
    },
    message () {
      switch (this.error) {
        case HTTP_ERROR_CODES.NOT_FOUND:
          return 'not_found_error_message'
        case HTTP_ERROR_CODES.UNAUTHORIZED:
        case HTTP_ERROR_CODES.FORBIDDEN:
          return 'forbidden_error_message'
        case HTTP_ERROR_CODES.INTERNAL_SERVER_ERROR:
          return 'server_error_message'
        default: {
          return 'server_error_message'
        }
      }
    }
  }
}
</script>
