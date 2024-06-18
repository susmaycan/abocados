<script setup>
const { locale: selectedLocale, locales, setLocale } = useI18n()

const flag = {
  en: 'i-twemoji-flag-united-kingdom',
  es: 'i-twemoji-flag-spain',
  kr: 'i-twemoji-flag-south-korea',
}
const availableLocales = computed(() => {
  return locales.value.map((locale) => [
    {
      label: locale.name,
      icon: flag[locale.code],
      disabled: locale.code === selectedLocale.value,
      click: () => setLocale(locale.code),
    },
  ])
})
</script>

<template>
  <UDropdown :items="availableLocales" :popper="{ placement: 'bottom-start' }">
    <ab-button
      color="white"
      right-icon="i-heroicons-chevron-down-20-solid"
      left-icon="i-heroicons-language-20-solid"
    />
    <template #item="{ item }">
      <span class="truncate">{{ item.label }}</span>
      <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 ms-auto" />
    </template>
  </UDropdown>
</template>
