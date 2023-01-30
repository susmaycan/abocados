<template>
  <v-switch
    v-model="inputValue"
    v-bind="$attrs"
    inset
    @input="onInput()"
    @change="onChange()"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-switch>
</template>

<script>
export default {
  name: 'ASwitch',
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: [Boolean],
      required: false,
      default: null
    }
  },
  data () {
    return {
      inputValue: null
    }
  },
  watch: {
    value () {
      this.inputValue = this.value
    }
  },
  mounted () {
    this.inputValue = this.value
  },
  methods: {
    onInput () {
      this.$emit('input', this.inputValue)
    },
    onChange () {
      this.$emit('change', this.inputValue)
    }
  }
}
</script>
