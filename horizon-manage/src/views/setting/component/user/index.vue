<script setup lang="jsx">
import ProTable from "@/components/ProTable/index.vue";
import SetRole from "./component/SetRole.vue";
import { reactive, ref } from "vue";
import { getUserListApi } from "@/api/modules/user";

const columns = reactive([
  {
    label: "用户名",
    prop: "user_name"
  },
  {
    label: "性别",
    prop: "ugender",
    render: scope => {
      return <span>{scope.row.gender === 0 ? "男" : "女"}</span>;
    }
  },
  {
    label: "简介",
    prop: "description",
    render: scope => {
      return <span>{scope.row.description}</span>;
    }
  },
  {
    label: "角色",
    prop: "role",
    render: scope => {
      return (
        <el-space>
          {scope.row.roles.map(item => {
            return <el-tag>{item.name}</el-tag>;
          })}
        </el-space>
      );
    }
  },
  {
    label: "操作",
    prop: "action",
    render: scope => {
      return (
        <el-space>
          <el-link type="success" onClick={() => handleSetUserRole(scope.row)}>
            设置角色
          </el-link>
          <el-link type="primary">编辑</el-link>
          <el-link type="danger">删除</el-link>
        </el-space>
      );
    }
  }
]);
const setRoleRef = ref();
const handleSetUserRole = user => {
  setRoleRef.value && setRoleRef.value.showDrawer(user);
};
const tableRef = ref();
const search = () => {
  tableRef.value && tableRef.value.search();
};
</script>

<template>
  <div class="table-box">
    <ProTable :columns="columns" ref="tableRef" :request-api="getUserListApi" />
    <SetRole ref="setRoleRef" @success="search" />
  </div>
</template>

<style scoped lang="scss"></style>
