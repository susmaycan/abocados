<template>
  <div v-bind="$attrs">
    <form-select
      :top="true"
      :value="selectedLanguage"
      :items="languages"
      :label="$t('language')"
      item-text="name"
      item-value="code"
      @input="onClickLanguage"
    />
  </div>
</template>

<script>
export default {
  name: 'LanguageSelector',
  data () {
    return {
      selectedLanguage: this.$i18n.localeProperties?.code || 'en'
    }
  },
  computed: {
    languages () {
      return this.$i18n.locales
    }
  },
  methods: {
    onClickLanguage (code) {
      this.selectedLanguage = code
      this.$i18n.setLocale(this.selectedLanguage)
    }
  }
}
</script>
