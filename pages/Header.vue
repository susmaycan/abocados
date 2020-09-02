<template>
  <div class="header">
    <Title>aBocados</Title>
    <hr/>
    <Paragraph>The application to store your favourite recipes</Paragraph>
    <Logo/>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Header extends Vue {
  }
</script>

<style>

</style>
