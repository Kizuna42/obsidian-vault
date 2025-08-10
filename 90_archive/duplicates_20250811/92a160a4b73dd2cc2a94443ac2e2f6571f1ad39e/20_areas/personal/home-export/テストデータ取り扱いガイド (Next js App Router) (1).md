# テストデータ取り扱いガイド (Next.js / App Router) (1)

## 概要

本ガイドでは、Next.js (App Router) を使用したフロントエンド開発において、将来的なデータベース実装を念頭に置いたテストデータ管理手法を示します。テーブル名に相当する JSON ファイルを `/data` ディレクトリに配置し、各ページから容易に参照できる構成を目指します。

## メリット

- **将来のDB移行容易化**：テーブル名に対応した JSON ファイルを用意しておくことで、将来的にデータベース化する際、実際のテーブルとの対応が明確で、置き換えがスムーズ。
- **独立性・可読性**：テストデータを `/data` ディレクトリ内で一元管理し、表示ロジックから分離することで、開発中の UI 調整が容易。
- **保守性**：本番リリース時には、この `/data` ディレクトリ内の JSON をデータフェッチ処理（DBやAPI）に置換するだけで対応可能。

## ディレクトリ構成例

```
src/
  app/
    home/
      page.tsx
  data/
    home.json     // homeページ用テストデータ
    users.json    // 例：将来的なユーザテーブル相当データ
    posts.json    // 例：将来的な投稿テーブル相当データ
    ... etc.

```

## 実装手順

### 1. テストデータファイルの用意

`/data` ディレクトリに、将来的なテーブル名に相当する JSON ファイルを配置し、テスト用データを定義します。

**例:** `home.json`

```json
{
  "id": 1,
  "title": "Home Test Data",
  "description": "This is a sample description for the home page."
}

```

### 2. ページコンポーネントでのインポート

`page.tsx` 内で、`/data` ディレクトリから JSON ファイルをインポートして使用します。

**例:** `src/app/home/page.tsx`

```tsx
import homeData from "@/data/home.json";

export default function Page() {
  const data = homeData;

  return (
    <div>
      <h1>{data.title}</h1>
      <p>{data.description}</p>
    </div>
  );
}

```

### 3. データ名とテーブル名の対応付け

`/data` ディレクトリに配置する JSON ファイルは、将来データベースで想定されるテーブル名やエンドポイント名と揃えておくことで、本番実装時にデータ取得部分を置換する際、ファイル名からDBテーブル名へ移行する作業がスムーズになります。

## ベストプラクティス

- **構造化ルール**：`/data` ディレクトリには、DBテーブル名（もしくはそれに相当する概念）をファイル名とした JSON データを配置します。
- **命名規則**：テーブル名が複数形であれば JSON ファイル名も複数形にし、DB実装時の対応を取りやすくします（例: `users.json` -> `users` テーブル想定）。
- **共通化**： 複数ページで使う共通データがある場合は、`/data` ディレクトリ配下に共通データ用 JSON ファイルを置いて、そこから各ページへインポートする形をとります。

## 参考情報

- [Next.js App Router Documentation](https://nextjs.org/docs/app/building-your-application)
- [JSON Basics](https://www.json.org/)

---

上記ガイドに従うことで、テストデータを将来的なデータベース実装とスムーズにマッピングでき、開発から本番リリースまでの移行を容易にします。