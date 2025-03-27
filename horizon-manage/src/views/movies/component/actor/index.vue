<script setup lang="jsx">
import { ref, reactive } from "vue";
import ProTable from "@/components/ProTable/index.vue";
import { getActorListApi } from "@/api/modules/actor";
import moment from "moment";
const columns = reactive([
  {
    prop: "name",
    label: "名称"
  },
  {
    prop: "gender",
    label: "性别",
    width: 80,
    render: scope => {
      return scope.row.gender === 1 ? "女" : "男";
    }
  },
  {
    prop: "nationality",
    label: "国籍"
  },
  {
    prop: "identity",
    label: "身份"
  },
  {
    label: "生日",
    prop: "birthday",
    render: scope => {
      return moment(scope.row.birthday).format("yyyy-MM-DD");
    }
  },
  {
    prop: "birthplace",
    label: "出生地"
  },
  {
    label: "签约公司",
    prop: "company"
  },
  {
    label: "操作",
    prop: "action",
    render: scope => {
      return (
        <el-space>
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
    <ProTable :columns="columns" :request-api="getActorListApi" />
  </div>
</template>

<style scoped lang="scss"></style>
