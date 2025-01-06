### 脚本说明

1. **自动获取脚本所在路径**
   使用 `os.path.dirname(os.path.abspath(__file__))` 获取脚本所在的路径，并将其作为图片文件夹的路径。
2. **创建 `compressed` 文件夹**
   如果 `compressed` 文件夹不存在，脚本会自动创建它。
3. **支持多种图片格式**
   脚本支持常见的图片格式（如 `.jpg`, `.png`, `.webp` 等），并保持压缩后的图片格式和名称不变。
4. **调试信息**
   脚本会打印正在处理的文件夹路径、文件夹中的文件列表，以及每个文件的处理状态。

------

### 使用步骤

1. 将脚本保存为 `.py` 文件（例如 `compress_images.py`）。

2. 将该脚本放到你需要压缩图片的文件夹中。

3. 打开终端，进入该文件夹，运行脚本：

   ```
   python3 compress_images.py
   ```

------

### 示例输出

假设脚本所在的文件夹中有以下文件：

- `image1.jpg`
- `image2.png`
- `document.pdf`

运行脚本后，输出如下：

复制

```
创建文件夹: /path/to/your/folder/compressed
正在处理的文件夹: /path/to/your/folder
文件夹中的文件: ['image1.jpg', 'image2.png', 'document.pdf']
正在压缩: image1.jpg
图片已压缩并保存到: /path/to/your/folder/compressed/image1.jpg
正在压缩: image2.png
图片已压缩并保存到: /path/to/your/folder/compressed/image2.png
跳过不支持的文件: document.pdf
```

压缩后的图片会保存到 `compressed` 文件夹中，文件名和格式保持不变。

------

### 注意事项

1. 确保脚本所在的文件夹中有图片文件。
2. 如果文件夹中没有图片文件，脚本会跳过压缩步骤。
3. 如果文件夹中已经有 `compressed` 文件夹，脚本会直接使用它，而不会重新创建。
