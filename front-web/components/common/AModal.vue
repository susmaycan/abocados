<template>
  <modal
    :name="name"
    :adaptive="true"
    height="auto"
    :max-width="width"
    :scrollable="true"
    :click-to-close="closable"
  >
    <div v-if="closable" slot="top-right">
      <a-button text icon="fa-solid fa-circle-xmark" @click="onClose" />
    </div>
    <div v-if="closable" class="d-flex justify-end">
      <a-button text icon="fa-solid fa-circle-xmark" @click="onClose" />
    </div>
    <div class="custom-modal-container">
      <slot name="title">
        <div class="custom-modal-title">
          <a-subtitle>{{ title | capitalize }}</a-subtitle>
        </div>
      </slot>
      <div class="custom-modal-content">
        <slot />
      </div>
      <slot name="button-actions">
        <div v-if="displayButtonActions" class="custom-modal-button-list">
          <a-button class="mr-2" color="secondary" @click="onClose">
            {{ $t('cancel') | capitalize }}
          </a-button>
          <a-button color="secondary" @click="onAccept">
            {{ $t('accept') | capitalize }}
          </a-button>
        </div>
        <div v-else class="custom-modal-button-list">
          <a-button @click="onClose">
            {{ $t('close') | capitalize }}
          </a-button>
        </div>
      </slot>
    </div>
  </modal>
</template>

<script>
export default {
  name: 'AModal',
  props: {
    name: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: false,
      default: ''
    },
    width: {
      type: Number,
      default: 500
    },
    displayButtonActions: {
      type: Boolean,
      default: true
    },
    closable: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    onAccept () {
      this.$emit('accept')
      this.onClose()
    },
    onClose () {
      this.$modal.hide(this.name)
    }
  }
}
</script>

<style scoped>
.custom-modal-container {
  padding: 2em 1em;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.custom-modal-button-list {
  margin-top: .5em;
  display: flex;
  justify-content: center;
  align-content: center;
}
.custom-modal-content {
  font-weight: 300;
}
@media (max-width: 756px) {
.custom-modal-container {
  padding: 1em;
}
}
</style>
