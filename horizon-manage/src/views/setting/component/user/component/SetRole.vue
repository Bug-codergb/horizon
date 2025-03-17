<template>
  <ProDrawer v-model="isShow" width="680px" @confirm="handleConfirm" @cancel="handleCancel" title="设置用户角色">
    <el-transfer
      :titles="['全部角色', '已选角色']"
      v-model="selected"
      :filter-method="filterMethod"
      filterable
      :data="roleList"
      :props="{ key: 'id', label: 'name' }"
    />
  </ProDrawer>
</template>
<script setup>
import ProDrawer from "@/components/ProDrawer/index.vue";
import { ref, reactive } from "vue";
import { ElMessage } from "element-plus";
import { getRoleListApi, setUserRoleApi } from "@/api/modules/role";
const emit = defineEmits(["success"]);
const isShow = ref(false);
const userItem = ref({});
const showDrawer = async user => {
  isShow.value = true;
  userItem.value = user;
  await getRoleList();
  selected.value = user.roles ? user.roles.map(item => item.id) : [];
};
const selected = ref([]);
const roleList = ref([]);
const getRoleList = async () => {
  const res = await getRoleListApi();
  roleList.value = res.rows;
};
const filterMethod = (query, item) => {
  console.log(query);
  return item.name.toLowerCase().includes(query.toLowerCase());
};
const handleConfirm = async () => {
  let params = {
    user_id: userItem.value.user_id,
    role_list: selected.value
  };
  const res = await setUserRoleApi(params);
  ElMessage.success("用户角色设置成功");
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
