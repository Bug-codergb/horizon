<script setup lang="jsx">
import ProTable from "@/components/ProTable/index.vue";
import SetRole from "./component/SetRole.vue";
import CreateUser from "./component/CreateUser.vue";
import { reactive, ref } from "vue";
import { getUserListApi, deleteUserApi } from "@/api/modules/user";
import { ElMessage, ElMessageBox } from "element-plus";

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
          <el-link type="danger" onClick={() => handleDelete(scope.row)}>
            删除
          </el-link>
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

const createUserRef = ref();
const handleCreateUser = () => {
  createUserRef.value && createUserRef.value.showDrawer();
};

const handleDelete = async item => {
  try {
    const ret = await ElMessageBox.confirm("确认删除么？", "提示", {
      type: "warning"
    });
    const res = await deleteUserApi(item.user_id);
    ElMessage.success("删除成功");
    search();
  } catch (e) {}
};
</script>

<template>
  <div class="table-box">
    <ProTable :columns="columns" ref="tableRef" :request-api="getUserListApi">
      <template #toolButton>
        <el-button type="primary" @click="handleCreateUser">创建用户</el-button>
      </template>
    </ProTable>
    <SetRole ref="setRoleRef" @success="search" />
    <CreateUser ref="createUserRef" @success="search" />
  </div>
</template>

<style scoped lang="scss"></style>
