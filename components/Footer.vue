<template>
  <div class="footer">
    <p>© 2020 — Web app coded by <a href="https://www.susmaycan.dev" target="_blank">Susana Mayo Cano</a> using VueJS.</p>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  @Component
  export default class Footer extends Vue {
  }
</script>

<style>
  .footer {
    background-color: #3F3D56;
    color: #ffffff;
    width: 100%;
    padding: 2rem 4rem;
    text-align: center;
    align-self: end;
    margin-top: auto;
  }
</style>
