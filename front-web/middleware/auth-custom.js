export default function ({ store, redirect, app }) {
  const token = app.$cookies.get('token')
  if (!token) {
    return redirect('/login')
  }
}
