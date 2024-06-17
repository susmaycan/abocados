export default $axios => resource => ({
  login (payload) {
    return $axios.$post(`${resource}/login/`, payload)
  },
  register (payload) {
    return $axios.$post(`${resource}/signup/`, payload)
  },
  getUser () {
    return $axios.$get(`${resource}/authenticated/`)
  },
  activateAccount (payload) {
    return $axios.$post(`${resource}/activate_account/`, payload)
  },
  sendValidationEmail (payload) {
    return $axios.$post(`${resource}/request_validation_email/`, payload)
  },
  passwordRecoveryRequest (payload) {
    return $axios.$post(`${resource}/password_recovery_request/`, payload)
  },
  passwordRecoveryCheck (payload) {
    return $axios.$post(`${resource}/password_recovery_check/`, payload)
  },
  passwordRecoveryConfirm (payload) {
    return $axios.$post(`${resource}/password_recovery_confirm/`, payload)
  }
})
