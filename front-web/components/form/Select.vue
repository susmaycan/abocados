<template>
  <v-select
    v-model="inputValue"
    v-bind="$attrs"
    :items="items"
    :menu-props="top ? { top: true, offsetY: true } : {}"
    attach
    :error-messages="inputErrors"
    @input="onInput()"
    @click:clear="onClear()"
  >
    <template #label>
      <a-label>
        {{ label | capitalize }}
      </a-label>
    </template>
  </v-select>
</template>

<script>
export default {
  name: 'ASelect',
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: [Array, String],
      required: false,
      default: null
    },
    items: {
      type: [Array],
      required: true,
      default: null
    },
    errors: {
      type: [String, Array],
      required: false,
      default: ''
    },
    customText: {
      type: Boolean,
      required: false,
      default: false
    },
    top: {
      type: Boolean,
      required: false,
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
      } else {
        return this.errors.join()
      }
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
    onClear () {
      this.$emit('clear')
    }
  }
}
</script>
