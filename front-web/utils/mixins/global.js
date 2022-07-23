import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['user'])
  },
  methods: {
    isCreator (recipe) {
      return recipe?.creator.id === this.user?.id
    }
  }
}
