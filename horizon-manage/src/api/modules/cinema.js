import http from "@/api";
export function getUserCinemaApi(data) {
  return http.get(`/cinema/user/${data.userId}`, data);
}
export function createCinemaApi(data) {
  return http.post("/cinema/create", data);
}
export function getCinemaTagApi(data) {
  return http.get("/cinema/tag/list", data);
}
export function setCinemaTagApi(data) {
  return http.post("/cinema/tag", data);
}
