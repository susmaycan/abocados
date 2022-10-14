<template>
  <div>
    <v-menu
      ref="menu"
      v-model="menu"
      :close-on-content-click="false"
      :return-value.sync="inputValue"
      transition="scale-transition"
      offset-y
      min-width="auto"
    >
      <template #activator="{ on }">
        <a-input
          readonly
          :value="inputDateFormatted"
          :label="label"
          v-bind="$attrs"
          :on="on"
        >
          <template #icon-left>
            <a-icon name="fa-solid fa-calendar" />
          </template>
        </a-input>
      </template>
      <v-date-picker
        v-model="inputValue"
        no-title
        scrollable
        @input="onInput()"
        @change="onChange()"
      >
        <v-spacer />
        <a-button
          text
          color="primary"
          @click="menu = false"
        >
          {{ $t('cancel') | capitalize }}
        </a-button>
        <a-button
          text
          color="primary"
          @click="$refs.menu.save(inputValue)"
        >
          {{ $t('accept') | capitalize }}
        </a-button>
      </v-date-picker>
    </v-menu>
    <p v-if="inputErrors" class="text-error">
      {{ inputErrors }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'ADatePicker',
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
    },
    fullWidth: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      inputValue: null,
      menu: false
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
    },
    inputDateFormatted () {
      if (!this.inputValue) {
        return ''
      }

      return this.formatDate(this.inputValue)
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
    },
    formatDate (date) {
      if (!date) { return null }

      const [year, month, day] = date.split('-')
      return `${day}/${month}/${year}`
    }
  }
}
</script>
<style>
  .full-width-input {
    width: 80vw;
  }
  .text-error {
    color: red;
  }
</style>
