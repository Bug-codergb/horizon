import http from "@/api";
export function getActorListApi(data) {
  return http.get(`/actor/list`, data);
}
export function getActorDetailApi(id) {
  return http.get(`/actor/detail/${id}`);
}
