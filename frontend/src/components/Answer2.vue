<template>
  <div class="answer2">
    <p>{{ answer2Data }}</p>
  </div>
</template>

<script>
export default {
  name: 'Answer2',
  props: {
    answer2Data: String // 通过 prop 接收答案二数据
  }
}
</script>

<style scoped>
.answer2 {
  background-color: #e0f7fa;
  padding: 10px;
  border: 1px solid #00bcd4;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
