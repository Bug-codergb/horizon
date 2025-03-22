<template>
  <ProDrawer v-model="isShow" :title="title" @confirm="handleConfirm">
    <el-form :model="formData" label-position="top" :rules="rules">
      <el-form-item label="名称" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名称" />
      </el-form-item>
      <el-form-item label="别名" prop="alias">
        <el-input v-model="formData.alias" placeholder="请输入别名" />
      </el-form-item>
      <el-form-item label="地址" prop="address">
        <el-input v-model="formData.address" type="textarea" placeholder="请输入地址" />
      </el-form-item>
    </el-form>
  </ProDrawer>
</template>
<script setup>
import { createCinemaApi } from "@/api/modules/cinema";
import ProDrawer from "@/components/ProDrawer/index.vue";
import { ref, reactive } from "vue";
import { useUserStore } from "@/stores/modules/user";
import { ElMessage } from "element-plus";

const emit = defineEmits(["success"]);
const isShow = ref(false);
const title = ref("新增影院");
const rules = reactive({
  name: [{ required: true, message: "影院名称不能为空", trigger: "blur" }],
  alias: [{ required: true, message: "别名不能为空", trigger: "blur" }],
  address: [{ required: true, message: "影院地址不能为空", trigger: "blur" }]
});
const userStore = useUserStore();
const formData = reactive({
  name: "",
  alias: "",
  address: ""
});
const showDrawer = () => {
  resetForm();
  isShow.value = true;
};
const resetForm = () => {
  formData.name = "";
  formData.address = "";
  formData.alias = "";
};
const handleConfirm = async () => {
  try {
    let params = {
      ...formData,
      userId: userStore.userInfo.userId
    };
    const res = await createCinemaApi(params);
    isShow.value = false;
    ElMessage.success("影院创建成功");
    emit("success");
  } catch (e) {}
};
defineExpose({
  showDrawer
});
</script>
