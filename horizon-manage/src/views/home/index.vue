<template>
  <div class="home card">
    <img class="home-bg" src="@/assets/images/welcome.png" alt="welcome" />
    <el-form :model="formData">
      <el-form-item label="菜单名称">
        <el-input v-model="formData.name" />
      </el-form-item>
      <el-form-item label="url">
        <el-input v-model="formData.path" />
      </el-form-item>
      <el-form-item label="组件路径">
        <el-input v-model="formData.component" />
      </el-form-item>
      <el-form-item label="父级菜单">
        <el-input v-model="formData.parent_id" />
      </el-form-item>
    </el-form>
    <el-button type="primary" @click="handleconfirm">确定</el-button>
  </div>
</template>

<script setup lang="js" name="home">
import { reactive } from "vue";
import { createMenuApi } from "@/api/modules/menu.js";
const formData = reactive({
  name: "",
  path: "",
  component: "",
  meta: {
    isHide: false,
    isAffix: false,
    isFull: false,
    isKeepAlive: false,
    isLink: "",
    title: "",
    icon: "Menu"
  },
  parent_id: 18
});
const handleconfirm = async () => {
  formData.meta.title = formData.name;
  formData.meta = JSON.stringify(formData.meta);
  const res = await createMenuApi(formData);
  console.log(res);
};
</script>

<style scoped lang="scss">
@import "./index.scss";
</style>
