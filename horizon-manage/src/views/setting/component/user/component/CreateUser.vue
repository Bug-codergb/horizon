<template>
  <ProDrawer v-model="isShow" :title="title" @confirm="handleConfirm">
    <el-form label-position="top" :rules="rules" :model="formData" ref="formRef">
      <el-form-item label="用户名" prop="user_name">
        <el-input v-model="formData.user_name" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item label="性别" prop="gender">
        <el-radio-group v-model="formData.gender">
          <el-radio :value="1">男</el-radio>
          <el-radio :value="0">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="formData.password" placeholder="请输入密码" />
      </el-form-item>
      <el-form-item label="简介" prop="description">
        <el-input v-model="formData.description" type="textarea" placeholder="请输入描述" />
      </el-form-item>
    </el-form>
  </ProDrawer>
</template>
<script setup>
import { ref, reactive } from "vue";
import ProDrawer from "@/components/ProDrawer/index.vue";
import { createUserApi } from "@/api/modules/user";
import { ElMessage } from "element-plus";
const rules = reactive({
  user_name: [{ required: true, message: "用户名不能为空", trigger: "blur" }],
  gender: [{ required: true, message: "性别不能为空", trigger: "change" }],
  password: [{ required: true, message: "密码不能为空", trigger: "blur" }]
});
const emit = defineEmits(["success"]);

const isShow = ref(false);
const title = ref("创建用户");
const showDrawer = () => {
  isShow.value = true;
};
const formData = reactive({
  user_name: "",
  gender: 1,
  password: "",
  description: ""
});
const formRef = ref();
const handleConfirm = () => {
  formRef.value &&
    formRef.value.validate(async e => {
      if (e) {
        const res = await createUserApi({
          ...formData
        });
        ElMessage.success("用户创建成功");
        isShow.value = false;
        emit("success");
      }
    });
};
defineExpose({
  showDrawer
});
</script>
