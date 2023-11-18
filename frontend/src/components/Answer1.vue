<template>
  <div class="answer1">
    <p>{{ answer1Data }}</p>
  </div>
</template>

<script>
export default {
  name: 'Answer1',
  props: {
    answer1Data: String // 通过 prop 接收答案一数据
  }
}
</script>

<style scoped>
.answer1 {
  background-color: #f5f5f5;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
