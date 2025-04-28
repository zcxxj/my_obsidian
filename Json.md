# Q：JSON快速入门
# A：
下面是对 JSON（JavaScript Object Notation）的快速入门简介，适合刚入门的你：

---

## ✅ 什么是 JSON？

**JSON** 是一种轻量级的数据交换格式，常用于前后端之间或服务之间传输数据。

- **全称**：JavaScript Object Notation
    
- **本质**：一个字符串格式的对象/数组
    
- **优点**：结构清晰、易读、语言无关
- **缩进不敏感**
---

## 🧱 JSON 的基本结构

JSON 只有两种结构：

### 1. **对象（Object）**：键值对的集合，用 `{}` 包裹

```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": false
}
```

### 2. **数组（Array）**：值的有序集合，用 `[]` 包裹

```json
[
  "apple",
  "banana",
  "cherry"
]
```

---

## 🔤 数据类型支持

JSON 中的值可以是：

|类型|示例|
|---|---|
|字符串|`"hello"`|
|数字|`123`, `3.14`|
|布尔值|`true`, `false`|
|空值|`null`|
|对象|`{...}`|
|数组|`[...]`|

---

## 🧪 一个嵌套示例

```json
{
  "name": "Bob",
  "age": 30,
  "skills": ["Python", "JavaScript"],
  "education": {
    "degree": "Master",
    "university": "XYZ University"
  },
  "isEmployed": true
}
```

---

## 🛠 JSON 的使用（Python 举例）

### 1. **读取 JSON 字符串**

```python
import json

json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)
print(data["name"])  # 输出 Alice
```

### 2. **把对象转为 JSON 字符串**

```python
data = {"name": "Bob", "age": 30}
json_str = json.dumps(data)
print(json_str)  # 输出 {"name": "Bob", "age": 30}
```

---

## ❌ JSON 注意事项

- **键**必须用**双引号**（`"key"`，不能用单引号）
    
- **不能包含注释**（不像 JS）
    
- JSON 文件一般以 `.json` 结尾
    

---

需要我帮你写一个简单的 JSON 文件例子，或者讲讲怎么在实际项目中用它吗？