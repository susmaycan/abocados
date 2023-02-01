<template>
  <v-switch
    v-model="inputValue"
    v-bind="$attrs"
    inset
    @input="onInput"
    @change="onChange"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-switch>
</template>

<script>
import InputMixin from '@/mixins/input'
export default {
  name: 'Switch',
  mixins: [InputMixin]
}
</script>
