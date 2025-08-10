# Supabase ローカル環境構築 & Next.js プロジェクト設定 (1)

## 前提条件

以下がインストールされていることを確認してください：

- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) (推奨: 最新のLTSバージョン)
- [Git](https://git-scm.com/)

---

## Supabase ローカル環境構築

### 1. Supabase CLI のインストール

Supabase CLI をインストールするには、公式ドキュメントに従って以下のコマンドを実行します。

```bash
# macOS / Linux
brew install supabase/tap/supabase-cli

# Windows (via Scoop)
scoop install supabase/tap/supabase-cli

```

インストールが完了したら、バージョンを確認して正しくインストールされていることを確認します。

```bash
supabase --version

```

### 2. プロジェクトの初期化

Supabase プロジェクトを初期化します。

```bash
supabase init

```

これにより、`supabase`というフォルダが作成され、必要な設定ファイルが生成されます。

### 3. Supabase サーバーの起動

ローカル環境で Supabase サーバーを起動します。

```bash
supabase start

```

起動後、以下のコンポーネントが利用可能になります：

- API URL: `http://localhost:54321`
- Studio (管理画面): `http://localhost:54323`
- Postgres データベース: ローカルで接続可能

### 4. ローカルデータベースへの接続

Postgres クライアントを使用してローカルデータベースに接続する場合、以下の接続情報を使用します。

- ホスト: `localhost`
- ポート: `54322`
- ユーザー: `postgres`
- パスワード: `postgres`
- データベース名: `postgres`

---

## Next.js プロジェクトの設定

### 1. Next.js プロジェクトの作成

```bash
npx create-next-app@latest my-supabase-app

```

以下のオプションを選択します：

- **TypeScript**: Yes
- **ESLint**: Yes
- **Tailwind CSS**: Yes
- **`src/` directory**: Yes
- **App Router**: Yes
- **Import alias**: Yes

プロジェクトディレクトリに移動します。

```bash
cd my-supabase-app

```

### 2. Supabase クライアントのインストール

Supabase 用のライブラリをインストールします。

```bash
npm install @supabase/supabase-js

```

### 3. 環境変数の設定

プロジェクトのルートに `.env.local` ファイルを作成し、以下を追加します。

```
NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key

```

`your-anon-key` は Supabase 管理画面から取得できます。

### 4. Supabase クライアントの設定

`src/lib/supabase.ts` ファイルを作成し、以下のコードを追加します。

```tsx
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

```

### 5. API の使用例

### ユーザー一覧の取得 (App Router を使用)

`src/app/api/users/route.ts`:

```tsx
import { NextResponse } from 'next/server';
import { supabase } from '@/lib/supabase';

export async function GET() {
  const { data, error } = await supabase.from('users').select('*');

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  return NextResponse.json(data, { status: 200 });
}

```

---

## 動作確認

1. `supabase start` でローカル環境を起動します。
2. `npm run dev` で Next.js サーバーを起動します。
3. ブラウザで `http://localhost:3000/api/users` を開き、API をテストします。

これでローカル環境で Supabase と Next.js (App Router) を連携した開発が行えます！