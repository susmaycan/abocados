export default function ({ store, redirect, app }) {
  const token = app.$cookies.get('token')
  if (!store.state.user.loggedIn && !token) {
    return redirect('/login')
  }
}
