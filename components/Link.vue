<template>
    <span class="link">
      <slot/>
    </span>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Link extends Vue {
  }
</script>

<style>
  .link:hover {
    text-decoration: underline;
  }
</style>
