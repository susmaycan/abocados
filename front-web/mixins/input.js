export default {
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: [Array, String, Number],
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
    },
    on: {
      type: Object,
      default: null
    },
    fullWidth: {
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
    onChange () {
      this.$emit('change', this.inputValue)
    },
    onInput () {
      this.$emit('input', this.inputValue)
    },
    onClear () {
      this.$emit('clear')
    }
  }
}
