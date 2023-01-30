<template>
  <v-textarea
    v-model="inputValue"
    v-bind="$attrs"
    :error-messages="inputErrors"
    @input="onInput()"
    @change="onChange()"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-textarea>
</template>

<script>
export default {
  name: 'ATextArea',
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: [String, Array, Number],
      required: false,
      default: null
    },
    errors: {
      type: [String, Array, Object],
      required: false,
      default: ''
    },
    required: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      inputValue: null
    }
  },
  computed: {
    inputErrors () {
      if (!this.errors) {
        return ''
      }
      if (typeof this.errors === 'string') {
        return this.errors
      } else if (Array.isArray(this.errors)) {
        return this.errors.join()
      }
      return this.$t('error_field')
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
