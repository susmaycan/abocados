<script setup lang="ts"></script>

<template>
  <div class="flex items-center">
    <div>{{ $t('app_name') }}</div>
    <div class="ml-auto">
      <lang-switcher />
      <theme-switcher />
    </div>
  </div>
</template>
