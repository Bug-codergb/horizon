import http from "@/api";
export function getActorListApi(data) {
  return http.get(`/actor/list`, data);
}
