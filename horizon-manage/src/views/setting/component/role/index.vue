<script setup lang="jsx">
import { reactive, ref } from "vue";
import ProTable from "@/components/ProTable/index.vue";
import CreateRole from "./component/CreateRole.vue";
import { getRoleListApi } from "@/api/modules/role";
import moment from "moment";
const columns = reactive([
  {
    label: "名称",
    prop: "name"
  },
  {
    label: "创建时间",
    prop: "createTime",
    render: scope => {
      return moment(scope.row.createTime).format("yyyy-MM-DD HH:mm");
    }
  },
  {
    label: "用户数量",
    prop: "users",
    render: scope => {
      return scope.row.users ? scope.row.users.length : 0;
    }
  },
  {
    label: "操作",
    prop: "action",
    render: scope => {
      return (
        <el-space>
          <el-link type="success">菜单</el-link>
          <el-link type="primary">编辑</el-link>
          <el-link type="danger">删除</el-link>
        </el-space>
      );
    }
  }
]);
const createRoleRef = ref();
const handleCreate = () => {
  createRoleRef.value && createRoleRef.value.showDrawer();
};
const tableRef = ref();
const search = () => {
  tableRef.value && tableRef.value.search();
};
</script>

<template>
  <div class="table-box">
    <ProTable :columns="columns" ref="tableRef" :request-api="getRoleListApi">
      <template #toolButton>
        <el-button type="primary" @click="handleCreate">新增</el-button>
      </template>
    </ProTable>
    <CreateRole ref="createRoleRef" @success="search" />
  </div>
</template>

<style scoped lang="scss"></style>
