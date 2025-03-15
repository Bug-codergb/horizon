<script setup lang="jsx">
import ProTable from "@/components/ProTable/index.vue";
import { reactive } from "vue";
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
          <el-link type="success">设置角色</el-link>
          <el-link type="primary">编辑</el-link>
          <el-link type="danger">删除</el-link>
        </el-space>
      );
    }
  }
]);
</script>

<template>
  <div class="table-box">
    <ProTable :columns="columns" :request-api="getUserListApi" />
  </div>
</template>

<style scoped lang="scss"></style>
