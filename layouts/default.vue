<template>
  <div class="layout-container">
    <NavBar/>
    <Nuxt/>
    <Footer/>
  </div>
</template>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400&display=swap');

  html {
    font-family: 'Montserrat',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
    word-spacing: 1px;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
    color: #3F3D56;
    font-weight: 400;
    font-size: 15px;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  a:hover {
    cursor: pointer;
  }

  *,
  *::before,
  *::after {
    box-sizing: border-box;
    margin: 0;
  }

  .layout-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    font-weight: 400;
  }
</style>
<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import NavBar from '~/components/NavBar.vue'
  import Footer from '~/components/Footer.vue'

  @Component({
    components: {NavBar, Footer}
  })
  export default class Layout extends Vue {
  }
</script>

