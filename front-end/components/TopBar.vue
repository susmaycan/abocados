<script setup lang="ts"></script>

<template>
  <div class="flex items-center">
    <nuxt-link to="/">
      <div class="flex items-center">
        <ab-app-logo :width="30" :height="30" /> {{ $t('app_name') }}
      </div>
    </nuxt-link>

    <div class="ml-auto flex items-end gap-2">
      <lang-switcher />
      <theme-switcher />
    </div>
  </div>
</template>
