<template>
  <div class="page">
    <div class="pdf-container">
      <!-- 左侧 PDF 内容显示框 -->
      <div class="pdf-content">
        <!-- 这里放置 PDF 内容，可以使用第三方 PDF 渲染库 -->
      </div>
    </div>

    <div class="right-container">
      <!-- 右侧上方问题显示框 -->
      <div class="question-box">
        <h2>请选择您要问的问题</h2>
        <!-- 在这里显示问题内容 -->
      </div>

      <!-- 右侧中部答案一显示框 -->
      <div class="answer-box">
        <h2>机器给出的答案</h2>
        <!-- 在这里显示答案一内容 -->
      </div>

      <!-- 右侧下部答案二显示框 -->
      <div class="answer-box">
        <h2>我们给出的答案</h2>
        <!-- 在这里显示答案二内容 -->
      </div>
    </div>
  </div>
</template>

<script setup>
// 在这里可以设置组件的属性、变量和方法
</script>

<style scoped>
.page {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  height: 100vh;
}

.pdf-container {
  flex: 1;
  padding: 20px;
  border: 1px solid #ccc;
  overflow: auto;
}

.pdf-content {
  /* 样式用于显示 PDF 内容 */
}

.right-container {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.question-box, .answer-box {
  padding: 20px;
  border: 1px solid #ccc;
}
</style>
