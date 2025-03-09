<template>
  <el-drawer
    v-model="isShow"
    :title="title"
    :destroy-on-close="true"
    :close-on-click-modal="false"
    :close-on-press-escape="false"
    :size="width"
  >
    <template #header>
      <slot name="header" />
    </template>
    <template #default>
      <slot></slot>
    </template>
    <template #footer>
      <el-button @click="handleCancel">取消</el-button>
      <el-button type="primary" @click="handleConfirm">确定</el-button>
    </template>
  </el-drawer>
</template>
<script setup>
import { defineModel } from "vue";
defineProps({
  title: {
    type: String,
    default: ""
  },
  width: {
    type: String,
    default: "30%"
  }
});
const emit = defineEmits(["cancel", "confirm"]);

const [isShow] = defineModel({
  type: Boolean,
  set(val) {
    return val;
  }
});
const handleCancel = () => {
  emit("cancel");
};
const handleConfirm = () => {
  emit("confirm");
};
</script>
