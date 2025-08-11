---
created: {{date:YYYY-MM-DD}}
tags: [daily]
aliases: [{{date:YYYY-MM-DD dddd}}]
---

# {{date:YYYY-MM-DD dddd}}

## 今日の焦点
- 

## 進捗記録

### 完了したタスク
```dataview
TASK
FROM "10_projects"
WHERE completed
WHERE completion = this.file.day
```

### 今日作成したノート
```dataview
LIST
WHERE file.cday = this.file.day
WHERE !contains(file.path, "01_daily")
SORT file.name ASC
```

### 今日更新したノート  
```dataview
LIST
WHERE file.mday = this.file.day
WHERE file.cday != this.file.day
WHERE !contains(file.path, "01_daily")
SORT file.mtime DESC
LIMIT 10
```

## 学んだこと・気づき
- 

## 明日への引き継ぎ
- 

## エネルギーレベル
朝: ⭐⭐⭐⭐⭐
昼: ⭐⭐⭐⭐⭐  
夜: ⭐⭐⭐⭐⭐

---
←  |  →