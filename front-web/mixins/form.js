export default {
  data() {
    return {
      valid: false,
      form: {},
      formErrors: {},
      globalErrors: [],
    }
  },
  props: {
    errors: {
      type: Object,
      default: null,
    },
    data: {
      type: Object,
      default: null,
    },
  },
  computed: {
    isEditMode() {
      return !!this.$route.params.id
    },
    success() {
      return !this.errors
    },
  },
  watch: {
    errors(newValue) {
      if (newValue) {
        this.handleErrors(newValue)
      }
    },
    data() {
      this.form = this.data
    },
  },
  methods: {
    onSubmit() {
      if (this.valid) {
        this.formErrors = {}
        this.globalErrors = []
        const formData = { ...this.form }
        if (typeof this.form.picture === 'string') {
          formData.picture = null
        }
        this.$emit('submit', formData)
      }
    },
    onCancel() {
      this.$router.go(-1)
    },
    handleErrors(errors) {
      this.globalErrors = errors?.non_field_errors || []
      this.formErrors = errors
    },
    onInputChanges(key, value) {
      this.form = {
        ...this.form,
        [key]: value,
      }
      this.formErrors = {
        ...this.formErrors,
        [key]: null,
      }
    },
  },
}
