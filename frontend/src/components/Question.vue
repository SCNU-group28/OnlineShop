<template>
  <div class="question">
    <p>{{ questionData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: {
    questionData: String // 通过 prop 接收问题数据
  }
}
</script>

<style scoped>
.question {
  font-size: 16px;
  color: #333;
  border: 1px solid #ddd;
  padding: 10px;
}
</style>
