<script setup lang="jsx">
import { reactive, ref } from "vue";
import ProTable from "@/components/ProTable/index.vue";
import { getUserCinemaApi } from "@/api/modules/cinema.js";
import { useUserStore } from "@/stores/modules/user";
import CreateCinema from "./components/CreateCinema.vue";
import RelateTag from "./components/RelateTag.vue";
import moment from "moment";
const userStore = useUserStore();
const searchParams = reactive({
  userId: userStore.userInfo.userId
});
const columns = reactive([
  {
    label: "影院名称",
    prop: "name",
    render: scope => {
      return <el-link type="primary">{scope.row.name}</el-link>;
    }
  },
  {
    label: "别名",
    prop: "alias"
  },
  {
    label: "地址",
    prop: "address"
  },
  {
    label: "标签",
    prop: "tag",
    "min-width": 140,
    render: scope => {
      return (
        <el-space>
          {scope.row.tag.map(it => {
            return <el-tag>{it.name}</el-tag>;
          })}
        </el-space>
      );
    }
  },
  {
    label: "创建时间",
    prop: "createTime",
    render: scope => {
      return moment(scope.row.createTime).format("yyyy-MM-DD HH:mm");
    }
  },
  {
    label: "创建人",
    prop: "user",
    render: scope => {
      return scope.row.user ? scope.row.user.user_name : "";
    }
  },
  {
    label: "操作",
    prop: "action",
    width: 160
  }
]);
const createCinemaRef = ref();
const handleCreate = () => {
  createCinemaRef.value && createCinemaRef.value.showDrawer();
};
const handleEdit = () => {};

const tableRef = ref();
const search = () => {
  tableRef.value && tableRef.value.search();
};
const relateTagRef = ref();

const handleCommand = (e, item) => {
  switch (e) {
    case "tag":
      relateTagRef.value.showDrawer(item);
      break;
    case "hall":
      break;
    case "coupons":
      console.log("coupons");
      break;
    case "food":
      console.log("fppd");
      break;
  }
};
</script>

<template>
  <div class="table-box">
    <ProTable :columns="columns" ref="tableRef" :request-api="getUserCinemaApi" :init-param="searchParams">
      <template #toolButton>
        <el-button type="primary" @click="handleCreate">添加</el-button>
      </template>
      <template #action="scope">
        <el-space>
          <el-link type="primary" @click="handleEdit(scope.row)">编辑</el-link>
          <el-link type="danger">删除</el-link>
          <el-dropdown @command="e => handleCommand(e, scope.row)">
            <span>
              <el-icon><More /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="tag">添加标签</el-dropdown-item>
                <el-dropdown-item command="hall">添加影厅</el-dropdown-item>
                <el-dropdown-item command="coupons">添加劵</el-dropdown-item>
                <el-dropdown-item command="food">观影小吃</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </el-space>
      </template>
    </ProTable>
    <CreateCinema ref="createCinemaRef" @success="search" />
    <RelateTag ref="relateTagRef" @success="search" />
  </div>
</template>

<style scoped lang="scss"></style>
