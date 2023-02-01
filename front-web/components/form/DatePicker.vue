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
        <form-text-input
          readonly
          :value="inputDateFormatted"
          :label="label"
          v-bind="$attrs"
          :on="on"
        >
          <template #icon-left>
            <a-icon name="fa-solid fa-calendar" />
          </template>
        </form-text-input>
      </template>
      <v-date-picker
        v-model="inputValue"
        no-title
        scrollable
        @input="onInput"
        @change="onChange"
      >
        <v-spacer />
        <a-button text color="primary" @click="menu = false">
          {{ $t('cancel') | capitalize }}
        </a-button>
        <a-button text color="primary" @click="$refs.menu.save(inputValue)">
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
import InputMixin from '@/mixins/input'

export default {
  name: 'DatePicker',
  mixins: [InputMixin],
  data () {
    return {
      menu: false
    }
  },
  computed: {
    inputDateFormatted () {
      if (!this.inputValue) {
        return ''
      }

      return this.formatDate(this.inputValue)
    }
  },
  methods: {
    formatDate (date) {
      if (!date) {
        return null
      }

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
