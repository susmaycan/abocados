<template>
  <Container>
    <div class="error-container">
      <h1>Error</h1>
      <slot/>
    </div>
  </Container>
</template>

<style>
  .error-container {
    text-align: center;
    background-color: #fd9a9a;
    color: #fd1e1e;
    padding: 2rem;
    border-radius: 1rem;
  }
</style>
