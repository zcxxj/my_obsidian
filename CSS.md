HTML默认支持的样式有什么，CSS自定义样式中的键值对中的键是有规定的吗？

---

**HTML 默认支持的样式与显示行为**

HTML 本质上是一种“内容结构描述语言”，它定义了一些**语义化标签**，每个标签在浏览器中都有一套默认的显示样式（叫 **user agent stylesheet**，即浏览器自带的默认样式表）。

**举几个常见例子：**

|HTML 标签|默认样式行为|
|---|---|
|`<h1>` 到 `<h6>`|显示为不同大小的粗体标题，有上下边距|
|`<p>`|显示为段落，有上下间距|
|`<ul>` / `<ol>`|显示为无序/有序列表，每项缩进显示|
|`<b>` / `<strong>`|显示为加粗|
|`<i>` / `<em>`|显示为斜体|
|`<a>`|显示为蓝色带下划线（未访问），紫色（已访问）|

你写的 HTML 页面，即使没有加任何 CSS，浏览器也会“自动显示成看起来还算不错的样子”，这就是因为这些**默认样式**。

但如果你想更改样式（颜色、大小、对齐、背景等），就要使用 CSS。

---

**CSS 自定义样式的“键”是有规定的**

是的，CSS 中你写的样式键值对（属性名和值），属性名是**标准化的、有规定的语法**，由 W3C（万维网联盟）制定。

例如：

```css
color: red;
font-size: 18px;
margin-top: 1em;
```

这些属性名必须是标准的 CSS 属性，不能随意起名。

---

**CSS 常见标准属性（键）分类举例**

1. **字体与文字**
    
    - `color`：文字颜色
        
    - `font-size`：字体大小
        
    - `font-weight`：粗细（如 `bold`、`400`）
        
    - `font-style`：斜体或正常
        
    - `text-align`：左中右对齐
        
2. **盒子模型**
    
    - `margin`：外边距
        
    - `padding`：内边距
        
    - `border`：边框
        
    - `width` / `height`：宽高
        
3. **布局**
    
    - `display`：布局方式，如 `block`、`inline`、`flex`
        
    - `position`：定位方式，如 `relative`、`absolute`
        
    - `top` / `left` / `right` / `bottom`：配合定位使用
        
4. **背景与颜色**
    
    - `background-color`：背景颜色
        
    - `background-image`：背景图
        
    - `opacity`：透明度
        
5. **其他常用属性**
    
    - `box-shadow`：阴影
        
    - `border-radius`：圆角
        
    - `cursor`：鼠标样式
        
    - `transition`：过渡动画控制
        

---

**不允许的情况：**

错误写法：

```css
banana: yellow;  /* ❌ 无效，因为 banana 不是合法 CSS 属性 */
```

浏览器会忽略无法识别的属性，不会报错，但也不会生效。

---

**如何查找合法的 CSS 属性？**

可以参考 W3C 或 MDN（Mozilla Developer Network）：

- [MDN CSS 属性大全](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference)
    

也可以在 Obsidian 使用的 CSS 文件中观察其他主题片段的写法。

---

**总结**

- HTML 自带“默认样式”，不同标签有默认显示方式
    
- CSS 的键值对中的键（属性名）**必须是标准规定的属性**
    
- 想修改 HTML 的样式，就用 CSS 为特定标签、类或 ID 编写样式规则
    
- 浏览器遇到不合法的 CSS 属性会直接忽略
    

---

如果你有兴趣，我可以帮你列一份 Obsidian 中常见 Markdown 标签渲染出来的 HTML 标签对应的默认样式，以及如何用 CSS 修改它们。是否需要？