<template>
  <v-text-field
    v-model="inputValue"
    v-bind="$attrs"
    :error-messages="inputErrors"
    :class="inputClass"
    @input="onInput"
    @change="onChange"
    v-on="on"
  >
    <template #prepend>
      <slot name="icon-left" />
    </template>
    <template #prepend-inner>
      <slot name="icon-left-inner" />
    </template>
    <template #append>
      <slot name="icon-right" />
    </template>
    <template #append-outer>
      <slot name="icon-right-outer" />
    </template>
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-text-field>
</template>

<script>
import InputMixin from '@/mixins/input'
export default {
  name: 'TextInput',
  mixins: [InputMixin]
}
</script>
<style>
.full-width-input {
  width: 80vw;
}
</style>
