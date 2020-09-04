import axios from "axios"

export default axios.create({
  baseURL: "https://abocados.herokuapp.com",
  headers: {
    "Content-type": "application/json"
  }
})
