哲学（ギリシャ語のphilosophia、文字通り「知恵を愛すること」）とは、存在、知識、価値、理性、心、言語に関する一般的かつ根本的な問題を研究する学問である。

存在、知識、価値、理性、心、言語などに関する一般的で根本的な問題を研究する学問である。このような問いはしばしば、分析あるいは解決すべき問題として扱われる。
この言葉はピタゴラス（紀元前570年頃～前495年）によって作られたと考えられている。哲学的手法には以下が含まれる。

質問、批判的な議論、合理的な議論、体系的なプレゼンテーションなど。

古典的な哲学的問いには以下のようなものがある：何事も本当に知ることができ、証明することができるのか？最も現実的なものは何か？

最も現実的なものは何か？哲学者はまた、次のような、より実践的で具体的な問いを投げかける：哲学者はまた、次のような、より現実的で具体的な質問も投げかける。
最善の生き方はあるのか？正義と不正義のどちらがよいのか（もしそれが許されるなら）。
人間に自由意志はあるのか？

歴史的には、「哲学」という言葉はあらゆる知識体系を指していた。古代ギリシャの哲学者
古代ギリシャの哲学者アリストテレスの時代から19世紀まで、「自然哲学」は天文学、医学、物理学を含んでいた。例えば、ニュートンの1687年の著作『自然哲学の数学的原理』は、後に物理学の書物に分類された。

19世紀には、近代的な研究大学の発展により、哲学をはじめとする学問は専門化・専門分化していった。
などの学問が専門化・専門化した。近代には、伝統的に哲学の一部であった研究が、別の学問分野となったものもある、

心理学、社会学、言語学、経済学などである。
また、芸術、科学、政治、その他の追求に密接に関連する研究も、哲学の一部であることに変わりはなかった。

哲学の一部となった。例えば、美は客観的か主観的か？多くの
科学的方法はたくさんあるのか、それともひとつだけなのか？政治的ユートピアは希望に満ちた夢なのか、それとも絶望的な空想なのか？

学術哲学の主な下位分野には、形而上学（「現実と存在の根本的な性質に関わる」）、認識論（「知識の性質と根拠（および）...その限界と妥当性」に関する）がある。
および...その限界と妥当性」）、倫理学、美学、政治哲学、論理学、科学哲学などがある。
および科学哲学。

## 📋 **プロジェクト概要**

### **何を作るプロジェクト？**
**「食事する哲学者問題」** を解決するマルチスレッドプログラムです。これは計算機科学における古典的な同期問題で、**デッドロック**、**競合状態**、**リソース共有**の概念を学ぶための教材として使われています。

### **問題設定**
- 🪑 **円卓に N人の哲学者が座っている**
- 🍴 **各哲学者の間に1本のフォークがある（N本のフォーク）**
- 🧠 **哲学者は「思考」「食事」「睡眠」を繰り返す**
- 🍽️ **食事には左右2本のフォークが必要**
- ⏰ **一定時間食事しないと死亡する**

---

## 🏗️ **プロジェクト構造**

```
philo/
├── Makefile          # ビルド設定
├── include/
│   └── philo.h       # 構造体定義・関数プロトタイプ
└── src/
    ├── main.c        # エントリーポイント
    ├── input.c       # 引数検証
    ├── init.c        # 初期化処理
    ├── threads.c     # スレッド管理
    ├── actions.c     # 哲学者の行動
    ├── monitor.c     # 死亡監視
    ├── utils.c       # ユーティリティ関数
    └── utils2.c      # 追加ユーティリティ
```

---

## 🧠 **必要な知識・学習内容**

### **1. 並行プログラミング (Concurrent Programming)**

#### **🔄 スレッド (Threads)**
```c
pthread_t thread;
pthread_create(&thread, NULL, function, argument);
pthread_join(thread, NULL);
```
- **学習ポイント**: 複数の実行フローを同時に管理
- **実装**: 各哲学者が独立したスレッドで動作

#### **🔒 ミューテックス (Mutex)**
```c
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, NULL);
pthread_mutex_lock(&mutex);    // クリティカルセクション開始
// 共有リソースへのアクセス
pthread_mutex_unlock(&mutex);  // クリティカルセクション終了
```
- **学習ポイント**: 共有リソースへの排他制御
- **実装**: フォーク、死亡フラグ、出力の保護

### **2. 同期問題の解決**

#### **💀 デッドロック回避**
```c
// 悪い例：全員が左のフォークを取ると永久に待機
take_left_fork();
take_right_fork();

// 良い例：偶数番号の哲学者は順序を逆にする
if (philo->id % 2 == 0)
    ft_usleep(1);  // 微小な遅延でタイミングをずらす
```

#### **🏃‍♂️ 競合状態 (Race Condition) 防止**
```c
pthread_mutex_lock(&philo->meal_lock);
philo->last_meal = get_current_time();
philo->meals_eaten++;
pthread_mutex_unlock(&philo->meal_lock);
```

### **3. 時間管理**

#### **⏱️ 高精度時間計測**
```c
size_t get_current_time(void)
{
    struct timeval time;
    gettimeofday(&time, NULL);
    return (time.tv_sec * 1000 + time.tv_usec / 1000);
}
```

#### **😴 精密な待機**
```c
int ft_usleep(size_t milliseconds)
{
    size_t start = get_current_time();
    while ((get_current_time() - start) < milliseconds)
        usleep(500);  // CPUを占有しない短い待機
    return (0);
}
```

---

## 🎯 **核心的な学習テーマ**

### **1. 哲学者問題の本質**
- **リソース競合**: 限られたフォークを複数の哲学者が奪い合う
- **デッドロック**: 全員が左のフォークを持って右を待つ状況
- **飢餓状態**: 特定の哲学者が永続的に食事できない状況

### **2. 解決戦略**
```c
void *philo_routine(void *pointer)
{
    t_philo *philo = (t_philo *)pointer;
    
    // 偶数番号の哲学者は少し待機（デッドロック回避）
    if (philo->id % 2 == 0)
        ft_usleep(1);
        
    while (!check_if_dead(philo))
    {
        eat(philo);        // 食事
        philo_sleep(philo); // 睡眠
        think(philo);      // 思考
    }
    return (pointer);
}
```

### **3. 監視システム**
```c
void *monitor(void *pointer)
{
    t_philo *philos = (t_philo *)pointer;
    
    while (1)
    {
        // 死亡チェック または 全員食事完了チェック
        if (check_death_and_set_flag(philos) || check_if_all_ate(philos))
            break;
    }
    return (pointer);
}
```

---

## 🔧 **技術的な実装ポイント**

### **1. データ構造設計**
```c
typedef struct s_philo
{
    pthread_t       thread;        // 哲学者のスレッド
    int             id;            // 哲学者ID
    size_t          last_meal;     // 最後の食事時刻
    int             meals_eaten;   // 食事回数
    pthread_mutex_t *l_fork;       // 左のフォーク
    pthread_mutex_t *r_fork;       // 右のフォーク
    pthread_mutex_t *dead_lock;    // 死亡フラグ保護
    pthread_mutex_t *meal_lock;    // 食事情報保護
    pthread_mutex_t *write_lock;   // 出力保護
} t_philo;
```

### **2. フォーク管理**
```c
void take_forks(t_philo *philo)
{
    pthread_mutex_lock(philo->l_fork);
    print_message("has taken a fork", philo, philo->id);
    pthread_mutex_lock(philo->r_fork);
    print_message("has taken a fork", philo, philo->id);
}
```

### **3. 死亡判定**
```c
int philosopher_dead(t_philo *philo, size_t time_to_die)
{
    pthread_mutex_lock(philo->meal_lock);
    if (get_current_time() - philo->last_meal >= time_to_die 
        && philo->eating == 0)
    {
        pthread_mutex_unlock(philo->meal_lock);
        return (1);
    }
    pthread_mutex_unlock(philo->meal_lock);
    return (0);
}
```

---

## 📚 **学習の段階的アプローチ**

### **Phase 1: 基礎理解**
1. **pthread ライブラリの基本**
2. **mutex の概念と使い方**
3. **時間計測とusleep**

### **Phase 2: 問題分析**
1. **哲学者問題の理論的理解**
2. **デッドロックが発生する条件**
3. **解決策の検討**

### **Phase 3: 実装**
1. **データ構造の設計**
2. **スレッド間通信の実装**
3. **同期メカニズムの構築**

### **Phase 4: デバッグ・最適化**
1. **競合状態の検出と修正**
2. **メモリリークの解決**
3. **パフォーマンス調整**

---

## 🎓 **このプロジェクトで身につくスキル**

### **技術スキル**
- ✅ **マルチスレッドプログラミング**
- ✅ **同期プリミティブの使用**
- ✅ **デッドロック回避技術**
- ✅ **リアルタイム制約の処理**
- ✅ **システムプログラミング**

### **問題解決スキル**
- ✅ **複雑な並行システムの設計**
- ✅ **競合状態の分析と解決**
- ✅ **リソース管理の最適化**
- ✅ **デバッグ技術の向上**

### **実務応用**
- 🌐 **Webサーバーの並行処理**
- 🎮 **ゲームエンジンのマルチスレッド**
- 💾 **データベースの同期制御**
- 🔄 **分散システムの設計**

---

## 🚀 **発展的な学習**

このプロジェクトをマスターした後は：

1. **セマフォを使った実装** (philo_bonus)
2. **プロセス間通信** (IPC)
3. **分散システムの哲学者問題**
4. **リーダー選出アルゴリズム**
5. **コンセンサスアルゴリズム**

**Philosophers プロジェクトは、並行プログラミングの入門として最適で、実際のシステム開発で必要となる重要な概念を実践的に学べる素晴らしい教材です！** 🎯
