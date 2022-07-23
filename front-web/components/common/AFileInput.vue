<template>
  <v-file-input
    v-model="inputFile"
    v-bind="$attrs"
    :label="label | capitalize"
    show-size
    truncate-length="24"
    @change="onInput()"
  />
</template>

<script>
export default {
  name: 'AFileInput',
  props: {
    label: {
      type: String,
      default: ''
    },
    value: null
  },
  data () {
    return {
      inputFile: null
    }
  },
  mounted () {
    this.inputFile = this.value
  },
  methods: {
    onInput () {
      this.$emit('input', this.inputFile)
    }
  }
}
</script>
