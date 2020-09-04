<template>
  <div class="container">
    <slot/>
  </div>
</template>

<style>
   .container {
      margin: 0 auto;
      display: flex;
      width: 100%;
      justify-content: center;
      align-items: center;
      text-align: center;
      flex-direction: column;
      padding-bottom: 4rem;
    }
</style>
