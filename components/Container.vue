<template>
  <div class="container">
    <slot/>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Container extends Vue {
  }
</script>

<style>
   .container {
      margin: 0 auto;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      flex-direction: column;
    }
</style>
