<template>
  <v-text-field
    v-model="inputValue"
    v-bind="$attrs"
    :error-messages="inputErrors"
    :messages="success"
    :class="inputClass"
    :success="!!success"
    :success-messages="success"
    @input="onInput()"
    @change="onChange()"
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
export default {
  name: 'AInput',
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
    success: {
      type: String,
      required: false,
      default: null
    },
    required: {
      type: Boolean,
      default: false
    },
    fullWidth: {
      type: Boolean,
      default: false
    },
    on: {
      type: Object,
      default: null
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
    },
    inputClass () {
      let base = ''
      if (this.fullWidth) {
        base += ' full-width-input'
      }
      return base
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
<style>
  .full-width-input {
    width: 80vw;
  }
  .a-input-sucess {
    color: blue !important;
  }
</style>
