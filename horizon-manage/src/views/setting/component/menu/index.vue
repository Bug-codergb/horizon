<template>
  <div class="table-box">
    <ProTable :columns="columns" ref="tableRef" :request-api="getMenuListApi">
      <template #toolButton>
        <el-button type="primary" @click="() => handleCreate()">新增</el-button>
      </template>
      <template #meta="scope">
        <div v-if="scope.row.meta" class="menu-icon">
          <component :is="scope.row.meta.icon" />
        </div>
        <span v-else>--</span>
      </template>
    </ProTable>
    <CreateMenu ref="createMenuRef" @success="search" />
  </div>
</template>
<script setup lang="jsx">
import { reactive, ref } from "vue";
import ProTable from "@/components/ProTable/index.vue";
import { getMenuListApi, deleteMenuApi } from "@/api/modules/menu.js";
import CreateMenu from "./components/createMenu/index.vue";
import { ElMessage, ElMessageBox } from "element-plus";
const columns = reactive([
  {
    label: "序号",
    type: "index",
    width: 80
  },
  {
    label: "菜单名称",
    prop: "name"
  },
  {
    label: "URL",
    prop: "path"
  },
  {
    label: "组件路径",
    prop: "component"
  },
  {
    label: "图标",
    prop: "meta"
  },
  {
    label: "排序",
    prop: "sort"
  },
  {
    label: "操作",
    prop: "action",
    render: scope => {
      return (
        <el-space>
          <el-link type="success" onClick={() => handleCreate(scope.row)}>
            新增子菜单
          </el-link>
          <el-link type="primary" onClick={() => handleEdit(scope.row)}>
            编辑
          </el-link>
          <el-link type="danger" onClick={() => handleDelete(scope.row)}>
            删除
          </el-link>
        </el-space>
      );
    }
  }
]);
const handleEdit = item => {
  console.log(item);
};
const handleDelete = async item => {
  try {
    const ret = await ElMessageBox.confirm("确认删除吗", "提示", {
      type: "warning"
    });
    const res = await deleteMenuApi(item.id);
    ElMessage.success("删除成功");
    search();
  } catch (e) {}
};
const createMenuRef = ref();
const handleCreate = item => {
  createMenuRef.value && createMenuRef.value.showDrawer(item);
};
const tableRef = ref();
const search = () => {
  tableRef.value && tableRef.value.search();
};
</script>
<style scoped lang="scss">
.menu-icon {
  svg {
    width: 22px;
    font-size: 14px;
  }
}
</style>
