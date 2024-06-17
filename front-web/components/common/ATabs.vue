<template>
  <div class="d-flex flex-column justify-center text-left">
    <v-tabs
      v-model="tab"
      v-bind="$attrs"
      center-active
      fixed-tabs
    >
      <v-tab
        v-for="item in items"
        :key="item"
      >
        {{ item }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <slot />
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'ATabs',
  props: {
    items: {
      type: Array,
      default () { return [] }
    }
  },
  data () {
    return {
      tab: null

    }
  }
}
</script>
