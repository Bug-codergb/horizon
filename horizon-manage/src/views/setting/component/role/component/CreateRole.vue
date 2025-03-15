<template>
  <Prodrawer v-model="isShow" title="新增角色" @cancel="handleCancel" @confirm="handleConfirm">
    <el-form :model="formData">
      <el-form-item label="名称" :rules="{ required: true, message: '名称不能为空', trigger: 'blur' }">
        <el-input v-model="formData.name" placeholder="请输入角色名称" />
      </el-form-item>
    </el-form>
  </Prodrawer>
</template>
<script setup>
import { ref, reactive } from "vue";
import { createRoleApi } from "@/api/modules/role";
import Prodrawer from "@/components/ProDrawer/index.vue";
import { ElMessage } from "element-plus";
const emit = defineEmits(["success"]);
const isShow = ref(false);
const showDrawer = () => {
  isShow.value = true;
};
const formData = reactive({
  name: ""
});
const handleConfirm = async () => {
  const res = await createRoleApi({
    name: formData.name
  });
  ElMessage.success("添加成功");
  formData.name = "";
  emit("success");
  isShow.value = false;
};
const handleCancel = () => {
  isShow.value = false;
};
defineExpose({
  showDrawer
});
</script>
