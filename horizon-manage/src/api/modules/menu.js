import http from "../index.js";
export function createMenuApi(data) {
  return http.post("/menu/create", data);
}
export function getMenuListApi(data) {
  return http.get("/menu/list", data);
}
