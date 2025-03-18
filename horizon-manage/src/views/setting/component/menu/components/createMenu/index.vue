<script setup lang="js">
import { ref, reactive } from "vue";
import cloneDeep from "lodash/cloneDeep.js";
import { createMenuApi } from "@/api/modules/menu.js";
import ProDrawer from "@/components/ProDrawer/index.vue";
import * as Icons from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
const isShow = ref(false);
const title = ref("新增菜单");
const emit = defineEmits(["success"]);
const rules = {
  name: [{ required: true, message: "菜单名称不能为空", trigger: "blur" }],
  path: [{ required: true, message: "菜单URL不能为空", trigger: "blur" }],
  component: [{ required: true, message: "组件路径不能为空", trigger: "blur" }],
  sort: [{ required: true, message: "排序不能为空", trigger: ["blur", "change"] }],
  "meta.icon": [{ required: true, message: "图标不能为空", trigger: "change" }],
  "meta.isKeepAlive": [{ required: true, message: "keep-alive不能为空", trigger: "change" }]
};
let meta = {
  isHide: false,
  isAffix: false,
  isFull: false,
  isKeepAlive: false,
  isLink: "",
  title: "",
  icon: ""
};
const formData = reactive({
  name: "",
  path: "",
  component: "",
  meta,
  parent_id: null,
  parent_name: "顶级菜单",
  sort: 0
});
const showDrawer = data => {
  console.log(data);
  isShow.value = true;
  if (data) {
    formData.parent_id = data.id;
    formData.parent_name = data.name;
    formData.component = data.component;
  } else {
    formData.parent_id = null;
    formData.parent_name = "顶级菜单";
  }
};
const formRef = ref();
const handleConfirm = () => {
  formRef.value &&
    formRef.value.validate(async e => {
      if (e) {
        const data = cloneDeep(formData);
        if (data.meta) {
          data.meta.title = data.name;
        }
        data.meta = data.meta ? JSON.stringify(data.meta) : null;

        const res = await createMenuApi(data);
        if (res.code === 200) {
          emit("success");
          isShow.value = false;
          ElMessage.success("添加成功");
        }
      }
    });
};
defineExpose({
  showDrawer
});
</script>

<template>
  <ProDrawer :title="title" v-model="isShow" @confirm="handleConfirm">
    <el-form :model="formData" label-position="top" :rules="rules" ref="formRef">
      <el-form-item label="父级菜单" prop="parent_id">
        <el-input :value="formData.parent_name" disabled />
      </el-form-item>
      <el-form-item label="菜单名称" prop="name">
        <el-input v-model="formData.name" maxlength="120" placeholder="请输入菜单名称" />
      </el-form-item>
      <el-form-item label="URL" prop="path">
        <el-input v-model="formData.path" maxlength="120" placeholder="请输入菜单URL" />
      </el-form-item>
      <el-form-item label="组件路径" prop="component">
        <el-input v-model="formData.component" maxlength="120" placeholder="请输入组件路径" />
      </el-form-item>
      <el-form-item label="排序" prop="sort">
        <el-input-number v-model="formData.sort" :precision="0" />
      </el-form-item>
      <el-form-item label="图标" prop="meta.icon">
        <el-select v-model="formData.meta.icon" filterable>
          <el-option v-for="(value, k) in Icons" :key="k" :label="k" :value="value.name">
            <el-space>
              <el-icon :size="20">
                <component :is="k" />
              </el-icon>
              <span>{{ k }}</span>
            </el-space>
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="是否全屏" prop="meta.isFull">
        <el-radio-group v-model="formData.meta.isFull">
          <el-radio :value="false">否</el-radio>
          <el-radio :value="true">是</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="是否隐藏" prop="meta.isFull">
        <el-radio-group v-model="formData.meta.isHide">
          <el-radio :value="false">否</el-radio>
          <el-radio :value="true">是</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="isKeepAlive" prop="meta.isFull">
        <el-radio-group v-model="formData.meta.isKeepAlive">
          <el-radio :value="false">否</el-radio>
          <el-radio :value="true">是</el-radio>
        </el-radio-group>
      </el-form-item>
    </el-form>
  </ProDrawer>
</template>

<style scoped lang="scss"></style>
