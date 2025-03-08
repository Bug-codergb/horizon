import http from "../index.js";
export function createMenuApi(data) {
  return http.post("/menu/create", data);
}
