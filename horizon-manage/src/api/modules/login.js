import http from "@/api";

/**
 * @name 登录模块
 */
// 用户登录
export const loginApi = params => {
  return http.post(`/login`, params, { loading: false }); // 正常 post json 请求  ==>  application/json
};

// 获取菜单列表
export const getAuthMenuListApi = () => {
  return http.get(`/menu/role/user/1742210914558`, {}, { loading: false });
};

// 获取按钮权限
export const getAuthButtonListApi = () => {
  return http.get(`/auth/buttons`, {}, { loading: false });
};

// 用户退出登录
export const logoutApi = () => {
  return http.post(`/logout`);
};
