<template>
  <v-textarea
    v-model="inputValue"
    v-bind="$attrs"
    :error-messages="inputErrors"
    @input="onInput"
    @change="onChange"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-textarea>
</template>
<script>
import InputMixin from '@/mixins/input'
export default {
  name: 'TextArea',
  mixins: [InputMixin]
}
</script>
