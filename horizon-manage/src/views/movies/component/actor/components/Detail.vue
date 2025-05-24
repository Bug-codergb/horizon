<script setup lang="jsx">
import { ref } from "vue";
import { useRoute } from "vue-router";

import { getActorDetailApi } from "@/api/modules/actor.js";
const route = useRoute();
const actor = ref({});
getActorDetailApi(route.params.id).then(res => {
  console.log(res.data);
  actor.value = res.data;
});
</script>

<template>
  <div class="table-box card">
    <el-descriptions border column="3">
      <el-descriptions-item label="名称" :span="1">{{ actor.name }}</el-descriptions-item>
      <el-descriptions-item label="性别" :span="1">{{ actor.gender === 1 ? "女" : "男" }}</el-descriptions-item>
      <el-descriptions-item label="出生地" :span="1">{{ actor.birthplace }}</el-descriptions-item>
      <el-descriptions-item label="出生日期" :span="1">{{ actor.birthday }}</el-descriptions-item>
      <el-descriptions-item label="身份" :span="1">{{ actor.identity }}</el-descriptions-item>
      <el-descriptions-item label="国籍" :span="1">{{ actor.nationality }}</el-descriptions-item>
      <el-descriptions-item label="名族" :span="1">{{ actor.people }}</el-descriptions-item>
      <el-descriptions-item label="身高" :span="1">{{ actor.height }}</el-descriptions-item>
      <el-descriptions-item label="星座" :span="1">{{ actor.constellation }}</el-descriptions-item>
      <el-descriptions-item label="毕业学校" :span="1">{{ actor.school }}</el-descriptions-item>
      <el-descriptions-item label="经济公司" :span="2">{{ actor.company }}</el-descriptions-item>
      <el-descriptions-item label="简介" :span="3">{{ actor.description }}</el-descriptions-item>
      <el-descriptions-item label="演艺经历">
        <el-timeline v-if="actor && actor.deductive" style="max-width: 600px">
          <el-timeline-item v-for="(activity, index) in actor.deductive" :key="index" :timestamp="activity.description">
            {{ activity.year }}
          </el-timeline-item>
        </el-timeline>
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<style scoped lang="scss"></style>
