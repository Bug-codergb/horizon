import http from "@/api";
export function getFilmListApi(data) {
  return http.get(`/film/list`, data);
}
