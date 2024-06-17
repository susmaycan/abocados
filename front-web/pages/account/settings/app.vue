<template>
  <page-layout :title="$t('application_settings') | capitalize">
    <p>{{ $t('application_settings_description') }}</p>
    <language-selector />
  </page-layout>
</template>
<script>
export default {
  name: 'ApplicationSettings',
  middleware: ['auth-custom']
}
</script>
