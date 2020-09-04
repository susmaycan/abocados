<template>
  <div class="subtitle-container">
    <h2 class="subtitle">
      <slot/>
    </h2>
  </div>
</template>

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
    padding: 7px;
  }
</style>
