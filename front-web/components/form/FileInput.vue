<template>
  <v-file-input
    v-model="inputValue"
    v-bind="$attrs"
    :label="label | capitalize"
    show-size
    truncate-length="24"
    @change="onInput()"
  />
</template>

<script>
import InputMixin from '@/mixins/input'
export default {
  name: 'FileInput',
  mixins: [InputMixin]
}
</script>
