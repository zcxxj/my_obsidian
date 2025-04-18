**Q： conda 怎么查看现有虚拟环境**

你可以使用以下命令来查看当前系统中已经创建的 Conda 虚拟环境：

```bash
conda env list
```

或者使用别名命令：

```bash
conda info --envs
```

---

### 输出说明：

这个命令的输出通常像这样：

```
# conda environments:
#
base                  *  /home/username/miniconda3
myenv                    /home/username/miniconda3/envs/myenv
another_env              /home/username/miniconda3/envs/another_env
```

- 有 `*` 号的那一行表示你当前正在使用的环境。
    
- 每一行后面是对应环境所在的路径。
    

如果你还有其他 Conda 使用上的问题，比如创建、删除、激活环境，随时可以问我。