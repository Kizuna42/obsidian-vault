---
project: "{{title}}"
status: planning
start_date: {{date:YYYY-MM-DD}}
due_date: 
priority: medium
tags: [project]
areas: []
---

# {{title}}

## プロジェクト概要
**目的**: 
**成果物**: 
**ステークホルダー**: 
**予算**: 
**期間**: 

## 成功基準
- [ ] 
- [ ] 
- [ ] 

## タスクブレイクダウン
### Phase 1: 準備・企画
- [ ] 

### Phase 2: 実行・開発  
- [ ] 

### Phase 3: 完成・納品
- [ ] 

## リソース・参考資料
```dataview
LIST
FROM "30_resources"
WHERE contains(tags, "{{title}}")
```

### 関連ノート
```dataview
LIST
FROM 
WHERE file.name != "{{title}}"
```

## 進捗記録
```dataview
TABLE status, due_date as "期限", priority as "優先度"
FROM "10_projects"
WHERE project = "{{title}}"
SORT due_date ASC
```

## 会議・コミュニケーション
| 日付 | 参加者 | 議題 | 決定事項 |
|------|---------|------|----------|
|      |         |      |          |

## リスクと対応策
| リスク | 発生確率 | 影響度 | 対応策 |
|--------|----------|---------|---------|
|        |          |         |         |

## レトロスペクティブ
### うまくいったこと
- 

### 改善すべきこと
- 

### 次回への学び
- 

---
**関連プロジェクト**: 
**前回レビュー**: 
**次回レビュー**: 