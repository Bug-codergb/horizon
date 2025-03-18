<template>
  <div class="footer flx-center">
    <span>{{ APP_NAME }}</span>
  </div>
</template>
<script setup>
const APP_NAME = import.meta.env.VITE_GLOB_APP_TITLE;
</script>
<style scoped lang="scss">
@import "./index";
</style>
