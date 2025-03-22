<template>
  <ProDrawer v-model="isShow" width="680px" @cancel="handleCancel" @confirm="handleConfirm" title="设置影院标签角色">
    <el-transfer
      :titles="['全部标签', '已选标签']"
      v-model="selected"
      :filter-method="filterMethod"
      filterable
      :data="tagList"
      :props="{ key: 'id', label: 'name' }"
    />
  </ProDrawer>
</template>
<script setup>
import ProDrawer from "@/components/ProDrawer/index.vue";
import { ref, reactive } from "vue";
import { ElMessage } from "element-plus";
import { getCinemaTagApi, setCinemaTagApi } from "@/api/modules/cinema";
const emit = defineEmits(["success"]);
const isShow = ref(false);
const userItem = ref({});
const showDrawer = async user => {
  isShow.value = true;
  userItem.value = user;
  await getCinemaTag();
  selected.value = user.tag ? user.tag.map(item => item.id) : [];
};
const selected = ref([]);
const tagList = ref([]);
const getCinemaTag = async () => {
  const res = await getCinemaTagApi();
  tagList.value = res.rows;
};
const filterMethod = (query, item) => {
  return item.name.toLowerCase().includes(query.toLowerCase());
};
const handleConfirm = async () => {
  let params = {
    cinema_id: userItem.value.id,
    tag: selected.value
  };
  const res = await setCinemaTagApi(params);
  ElMessage.success("影院标签设置成功");
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
