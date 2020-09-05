<template>
  <span>
    <button v-if="submit" type="submit" class="custom-button">
      <slot/>
    </button>
    <button v-else-if="onClick" @click="onClick" class="custom-button">
      <slot/>
    </button>
    <button v-else class="custom-button">
      <slot/>
    </button>
  </span>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const ButtonProps = Vue.extend({
    props: {
      onClick: {type: Function, required: false},
      submit: {type: Boolean, required: false},
      url: {type: String, required: false},
    }
  })

  @Component
  export default class Button extends ButtonProps {
  }
</script>

<style>
  .custom-button {
    color: #ffffff;
    background-color: #3F3D56;
    padding: .7rem;
    border-radius: .7rem;
    font-size: 1rem;
    text-decoration: none;
    border: solid 1px #ffffff;
    cursor: pointer;
  }

  .custom-button:hover {
    color: #3F3D56;
    background-color: #ffffff;
    border: solid 1px #3F3D56;
  }
</style>
