<template>
  <div class="subtitle-container">
    <h1 class="subtitle"><slot/></h1>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Subtitle extends Vue {
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100&display=swap');

  .subtitle {
    font-family: 'Montserrat', Arial, sans-serif;
    display: block;
    font-weight: 100;
    font-size: 50px;
    color: #3F3D56;
    letter-spacing: 1px;
  }

  .subtitle-container {
    padding:7px;
  }
</style>
