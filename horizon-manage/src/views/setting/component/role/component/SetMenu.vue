<template>
  <ProDrawer v-model="isShow" width="30%" @confirm="handleConfirm" @cancel="handleCancel" title="设置用户角色">
    <el-tree
      node-key="id"
      ref="treeRef"
      style="max-width: 600px"
      :props="treeProps"
      :data="menuList"
      :default-expand-all="true"
      show-checkbox
    />
  </ProDrawer>
</template>
<script setup>
import ProDrawer from "@/components/ProDrawer/index.vue";
import { ref, reactive, nextTick } from "vue";
import { ElMessage } from "element-plus";
import { getMenuListApi, setRoleMenuApi, getRoleMenuApi } from "@/api/modules/menu";
const emit = defineEmits(["success"]);
const isShow = ref(false);
const role = ref({});
const showDrawer = async params => {
  isShow.value = true;
  role.value = params;
  await getMenuList();
  await getRoleMenu(params.id);
  //selected.value = user.roles ? user.roles.map(item => item.id) : [];
};
const selected = ref([]);
const menuList = ref([]);
const getMenuList = async () => {
  const res = await getMenuListApi();
  menuList.value = res.rows;
};

const roleMenu = ref([]);
const getRoleMenu = async id => {
  const res = await getRoleMenuApi(id);
  let menuList = res.data || [];
  const keys = menuList.filter(item => item.half === 0).map(item => item.menu.id);
  const halfKeys = menuList.filter(item => item.half == 1).map(item => item.menu.id);
  nextTick(() => {
    console.log(keys);
    treeRef.value && treeRef.value.setCheckedKeys(keys);
  });
};

const treeRef = ref();
const treeProps = {
  label: "name",
  children: "children"
};
const handleConfirm = async () => {
  let params = {
    role_id: role.value.id,
    menu_list: []
  };
  for (let item of treeRef.value.getCheckedKeys()) {
    params.menu_list.push({
      menu_id: item,
      half: 0
    });
  }
  for (let item of treeRef.value.getHalfCheckedKeys()) {
    params.menu_list.push({
      menu_id: item,
      half: 1
    });
  }
  const res = await setRoleMenuApi(params);
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
