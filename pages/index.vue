<template>
  <div>
    <Container>
      <NavBar/>
      <Header/>
    </Container>
    <Container>
      <RecipeList/>
    </Container>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'
  import RecipeList from '~/pages/RecipeList.vue'
  import Header from '~/pages/Header.vue'
  import NavBar from '~/pages/NavBar.vue'

  @Component({
    components: {RecipeList, Header, NavBar}
  })
  export default class Index extends Vue {
  }
</script>
