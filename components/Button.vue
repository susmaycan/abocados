<template>
  <a @click="onClick" class="fake-button">
    <slot/>
  </a>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const ButtonProps = Vue.extend({
    props: {
      onClick: Object
    }
  })

  @Component
  export default class Button extends ButtonProps {
  }
</script>

<style>
 .fake-button {
   color: #ffffff;
   background-color: #3F3D56;
   padding: .7rem;
   border-radius: .7rem;
   text-decoration: none;
 }
</style>
