# Q：HTML DOM和HTML是什么关系，是HTML DOM定义了HTML的语法吗，还是说只是定义了一种HTML的代码书写规范

# A：
[[JavaScript#Q： JavaScript 通过 HTML DOM 来操作HTML代码|HTML DOM与JavaScript的关系]]


HTML DOM 和 HTML 是两个密切相关但功能不同的概念：

---

### **HTML 是什么？**

**HTML（HyperText Markup Language）超文本标记语言** 是一种**标记语言**，用于定义网页的结构和内容。比如：

```html
<h1>标题</h1>
<p>这是段落</p>
```

这只是一个**文本文件**，浏览器读取后会将它**渲染为网页**。

---

### **HTML DOM 是什么？**

**HTML DOM（Document Object Model）文档对象模型** 是浏览器**在加载 HTML 页面后**，为页面构建的一种**树状结构的对象模型**。它是用来**表示和操作网页结构的编程接口（API）**，通常用 JavaScript 来操作。

简单地说：

> HTML 是“内容”，HTML DOM 是“浏览器理解并可操作的结构化版本”。

例如，下面这段 HTML：

```html
<body>
  <p>Hello</p>
</body>
```

在 HTML DOM 中会被转换成如下结构：

```
document
 └── html
     └── body
         └── p
             └── "Hello"
```

你可以通过 JavaScript 操作它，比如：

```js
document.querySelector('p').innerText = 'Hi!';
```

这就是**通过 DOM 修改页面内容**。

---

### 回到你的问题：

#### ❓ HTML DOM 是不是定义了 HTML 的语法？

不是。

HTML 的语法由 HTML 的**规范（specification）**决定，比如由 [WHATWG](https://html.spec.whatwg.org/) 维护的 HTML Living Standard。

HTML DOM 是在浏览器**解析完 HTML 之后**构建出来的模型，它是**基于 HTML 结构的一种抽象表示和操作接口**，而不是语法的定义者。

---

### 简单类比：

|概念|类比|说明|
|---|---|---|
|HTML|Word文档的内容|描述网页的结构和内容|
|HTML DOM|Word文档的对象模型|浏览器内部根据 HTML 构建的数据结构，用于操作页面|

---

### 总结一句话：

> **HTML 定义网页的内容和结构，HTML DOM 提供浏览器对这些内容进行“理解”和“编程控制”的方式。**

如果你还在疑惑“HTML DOM 有没有规范书写 HTML 的作用”，可以这么理解：

- **HTML DOM 不定义 HTML 语法**
    
- **HTML DOM 对应的是浏览器提供的“编程接口”**
    
- 书写 HTML 时需要遵循 HTML 的语法规范，不是 DOM 规范
    

如果你想我再给一个更形象的例子或补充代码例子，可以说一声～




