<template>
  <div class="pdf-viewer">
    <canvas ref="pdfCanvas"></canvas>
  </div>
</template>

<script>
import pdfjsLib from 'pdfjs-dist';

export default {
  name: 'PdfViewer',
  data() {
    return {
      pdfDocument: null,
      pageNumber: 1,
      totalPages: 0,
    };
  },
  mounted() {
    this.loadPdf();
  },
  methods: {
    async loadPdf() {
      const pdfUrl = 'your_pdf_url_here.pdf'; // 替换成您的 PDF 文件 URL
      const pdfCanvas = this.$refs.pdfCanvas;
      
      // 加载 PDF 文件
      const loadingTask = pdfjsLib.getDocument(pdfUrl);

      loadingTask.promise
        .then((pdfDoc) => {
          this.pdfDocument = pdfDoc;
          this.totalPages = pdfDoc.numPages;
          return this.renderPage(this.pageNumber, pdfCanvas);
        })
        .catch((error) => {
          console.error('Error loading PDF:', error);
        });
    },
    async renderPage(pageNumber, canvas) {
      if (!this.pdfDocument) return;
      
      const pdfPage = await this.pdfDocument.getPage(pageNumber);
      const viewport = pdfPage.getViewport({ scale: 1.0 });
      const context = canvas.getContext('2d');
      
      canvas.height = viewport.height;
      canvas.width = viewport.width;

      const renderContext = {
        canvasContext: context,
        viewport: viewport,
      };

      await pdfPage.render(renderContext);
    },
  },
}
</script>

<style scoped>
.pdf-viewer {
  display: flex;
  align-items: center;
  justify-content: center;
}

canvas {
  border: 1px solid #000;
}
</style>
