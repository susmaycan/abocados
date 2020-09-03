<template>
  <div>
    <Container>
      <div class="header">
        <Title>aBocados</Title>
        <hr/>
        <p>The application to store your favourite recipes</p>
        <HeaderImage/>
      </div>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Index extends Vue {
  }
</script>

<style>
  .header {
    display: flex;
    flex-direction: column;
    bottom: 0;
    left: 0;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
  }
</style>
