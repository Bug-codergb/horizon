<script setup lang="jsx">
import { ref, reactive } from "vue";
import moment from "moment";
import { getFilmListApi } from "@/api/modules/film";
import ProTable from "@/components/ProTable/index.vue";
const columns = reactive([
  {
    label: "名称",
    prop: "name",
    "min-width": 100
  },
  {
    label: "外文名",
    prop: "foreign_name",
    "min-width": 100
  },
  {
    label: "别名",
    prop: "alias",
    "min-width": 100
  },
  {
    label: "语言",
    prop: "language",
    width: 100
  },
  {
    label: "评分",
    prop: "score",
    width: 80
  },
  {
    label: "上映时间",
    prop: "release_time",
    width: 130,
    render: scope => {
      return moment(scope.row.release_time).format("yyyy-mMM-DD");
    }
  },
  {
    label: "分类",
    prop: "cate",
    width: 150,
    render: scope => {
      return (
        <el-space>
          {scope.row.cate.map(item => {
            return <el-tag key={item.id}>{item.name}</el-tag>;
          })}
        </el-space>
      );
    }
  },
  {
    label: "操作",
    prop: "action",
    fixed: "right",
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
    <ProTable :request-api="getFilmListApi" :columns="columns">
      <template #toolButton>
        <el-button type="primary">新增</el-button>
      </template>
    </ProTable>
  </div>
</template>

<style scoped lang="scss"></style>
