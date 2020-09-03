<template>
  <Container>
    <Subtitle>Error 404</Subtitle>
    <p>'Cause I still haven't found what you are looking for 🎵</p>
  </Container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import Subtitle from '~/components/Subtitle.vue'

  @Component({
    components: {Subtitle}
  })
  export default class Error extends Vue {
  }
</script>
