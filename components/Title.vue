<template>
  <div class="title-container">
    <h1 class="title"><slot/></h1>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Title extends Vue {
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100&display=swap');

  .title {
    font-family: 'Montserrat', Arial, sans-serif;
    display: block;
    font-weight: 100;
    font-size: 100px;
    color: #3F3D56;
    letter-spacing: 1px;
  }

  .title-container {
    padding:10px;
  }
</style>
