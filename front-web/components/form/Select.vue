<template>
  <v-select
    v-model="inputValue"
    v-bind="$attrs"
    :items="items"
    :menu-props="top ? { top: true, offsetY: true } : {}"
    attach
    :error-messages="inputErrors"
    @input="onInput"
    @click:clear="onClear"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-select>
</template>
<script>
import InputMixin from '@/mixins/input'
export default {
  name: 'Select',
  mixins: [InputMixin],
  props: {
    items: {
      type: [Array],
      required: true,
      default: null
    },
    top: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>
