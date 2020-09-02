<template>
    <p class="paragraph"><slot/></p>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Paragraph extends Vue {

  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap');

  .paragraph {
    font-family: 'Montserrat', Arial, sans-serif;
    display: block;
    font-weight: 400;
    font-size: 15px;
    color: #3F3D56;
    padding:0.5rem;
  }
</style>
