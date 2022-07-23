import { capitalize } from 'lodash'
export default {
  methods: {
    required (value) {
      return !!value || capitalize(this.$t('this_field_is_required'))
    },
    emailFormat (value) {
      return /.+@.+\..+/.test(value) || capitalize(this.$t('email_invalid_format'))
    },
    minMax (min, max, value) {
      if (!value) {
        return true
      }
      const valueNumber = parseInt(value)
      if (!valueNumber) {
        return capitalize(this.$t('wrong_value'))
      }
      if (valueNumber < min) {
        return capitalize(this.$t('field_minimum_value') + min)
      }
      if (valueNumber > max) {
        return capitalize(this.$t('field_maximum_value') + max)
      }
      return true
    },
    minLength (value, min) {
      if (value && value.length < min) {
        return capitalize(this.$t('field_minimum_length') + min)
      }
      return true
    },
    maxLength (value, max) {
      if (value && value.length > max) {
        return capitalize(this.$t('field_maximum_length') + max)
      }
      return true
    }

  }
}
