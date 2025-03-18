import http from "../index.js";
export function getRoleListApi(params) {
  return http.get("/role/all", params);
}
export function createRoleApi(data) {
  return http.post("/role/create", data);
}
export function setUserRoleApi(data) {
  return http.post("/role/user", data);
}
export function deleteRoleApi(id) {
  return http.delete(`/role/delete/${id}`);
}
