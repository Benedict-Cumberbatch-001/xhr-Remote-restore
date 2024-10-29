## Science Direct：
### 检索关键词
`AND`
用于两个或多个关键词间，要求同时出现
`OR`
用于两个或多个关键词间，要求有其中一个出现
`NOT`
限制某个关键词不出现
```
Eg:(3D reconstruction OR intelligent robot ) AND (rock mass) AND (security OR safety)
AB=eg
TI=eg
```
从摘要或标题中搜索
### 注意事项
在`Science Direct`检索文献时，还有这些`Tips`不可忽略：
在`Science Direct`中，检索条件不区分大小写，因此输入某个单词或词组时使用大写或小写字母对检索结果并无影响。但是，布尔运算符必须以大写形式输入。
括号()用于定义运算符之间的逻辑，让括号内的表达式优先执行，同时分组和逻辑也更清晰明确。例如：
使用 `(a OR b) AND (c OR d)`，而非直接检索 `a OR b AND c OR d` 。
用空格隔开的多个单词将按各个单词分别搜索，但可以使用引号" "指定必须彼此相邻出现的术语，即将检索关键词放在双引号中，这样检索时会将引号内所有单词作为一个整体进行检索，检索结果也将出现与引号内部分一致的内容。在搜索地名、人名、机构名称和其他专有名称的时候，尽量使用引号精确检索。例如：
```
("heart attack" OR "myocardial infarction") AND diabetes AND NOT cancer
```
上面的例子也可以更简洁地表达为: `("heart attack" OR "myocardial infarction")` `diabetes -cancer`
一般情况下，使用单数名词作为搜索条件时，系统也会搜索复数或所有格形式；使用美式或英式拼法对搜索结果并无影响。例如：
检索 "`heart attack`" 包括了 "`heart attacks`" 的结果；检索 "`color code`" 包括了 "`colour code`" 的结果。
布尔值运算符优先级如下：
`NOT > AND > OR`
规则
短语搜索中会忽略标点符号。搜索“`heart-attack`”和“`heart attack`”会返回相同的结果。
包含复数和拼写变形：“`heart attack`”包含“`heart attacks`”，“`color code`”包含“`colour code`”。(不用使用 通配符*)s
## Google Scholar：
### 单属性检索
#### 关键词检索
1. 单关键词的检索
比如我们想要查一下安全行为`（safety behavior）`的相关研究， 那么我们在谷歌学术的检索框里边输入的检索码为 "`safety behavior`"， 其中我们通过英文字符的双引号进行限定。
2. 多关键词的检索
比如我们想查一下建筑领域的安全行为的相关研究，那么我们的检索码为 "`construction`" `AND` "`safety behavior`"。
那么我们是不是也可以将检索码设定为"`construction safety behhavior`"? 这两种检索方式有什么区别呢？其实区别很大，第一种检索方式不要求得到的相关研究里 `construction` 和 `safety behavior`是在同一位置出现，而第二种检索方式是要求的。
#### 检索关键词限定标题
整体来说我们用`intitle`: 来限定，其中检索码整体为`intitle`:检索关键词（组），其中`intitle`后边的冒号为英文字符，同时`intitle`:与检索词（组）之间不存在空格。
1. 单关键词的检索
比如我们想要查一下文章标题中出现安全行为（safety behavior）的相关研究， 那么我们在谷歌学术的检索框里边输入的检索码为 `intitle:"safety behavior"`。
2. 多关键词的检索
比如我们想了解一下文章标题中同时出现建筑和安全行为的相关研究，那么我们的检索码为 `intitle:("construction" AND "safety behavior")`。
#### 检索关键词限定文章
整体来说我们用`intext`: 来限定，其中检索码整体为`intext`:检索关键词（组），其中`intext`后边的冒号为英文字符，同时`intext`:与检索词（组）之间不存在空格。
1. 单关键词的检索
比如我们想要查一下文章内容（正文）中出现安全行为`（safety behavior）`的相关研究， 那么我们在谷歌学术的检索框里边输入的检索码为 `intext:"safety behavior"`。
2. 多关键词的检索
比如我们想了解一下文章标题中同时出现建筑和安全行为的相关研究，那么我们的检索码为 `intext"(construction" AND "safety behavior")`

