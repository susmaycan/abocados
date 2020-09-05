<template>
  <div>
    <svg v-if="rankingList" v-for="(ranking, index) in rankingList" :key="index"
         xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#ffac25" stroke="none"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
      <polygon
        points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
    </svg>
    <svg v-if="rankingList === undefined || rankingList === null" v-for="index in 5" :key="index"
         xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#e7e6e4 " stroke="none"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
      <polygon
        points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
    </svg>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator'

  const RankingProps = Vue.extend({
    props: {
      rankingList: Number
    }
  })

  @Component
  export default class Ranking extends RankingProps {
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
