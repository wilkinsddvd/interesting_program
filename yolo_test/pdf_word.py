from pdf2docx import parse

def multi_page_pdf_to_word_with_format(pdf_path, word_path):
    # 将多页PDF转换为Word文档并保留格式和布局
    parse(pdf_path, word_path)

if __name__ == "__main__":
    # 定义输入的PDF文件路径和输出的Word文件路径
    pdf_path = "D:\d.pdf"
    word_path = "D:\目标.docx"
    # 执行转换操作
    multi_page_pdf_to_word_with_format(pdf_path, word_path)
