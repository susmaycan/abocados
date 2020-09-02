import http from "./http-common"

class DataService {
  getAll() {
    return http.get("/recipe")
  }

  get(id: string) {
    return http.get(`/recipe/${id}`)
  }

  create(data: any) {
    return http.post("/recipe", data)
  }

  update(id: string, data: any) {
    return http.put(`/recipe/${id}`, data)
  }

  delete(id: string) {
    return http.delete(`/recipe/${id}`)
  }

}

export default new DataService()
