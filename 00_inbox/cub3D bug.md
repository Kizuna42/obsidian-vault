### **①** 

### **不正なマップが読み込まれても実行できてしまう**

- **現象**：
    
    　空行・カンマだらけの定義（FやC）・マップ外の文字列があっても、エラーにならず処理されてしまう。
    
- **問題点**：
    
    　**マップや構文のバリデーションが不十分**で、異常な入力もそのまま読み込んでしまう。
    
- **望ましい動作**：
    
    　不正なフォーマット（空行・余分な記号・定義漏れなど）を検出して**エラーメッセージを出して強制終了**してほしい。
    

---

### **②** 

### **テクスチャの模様がプレイヤー移動と一緒に動いてしまう**

- **現象**：
    
    　模様付きの壁にすると、プレイヤーが動いた際に模様までズレてスクロールしてしまう。
    
- **問題点**：
    
    　**テクスチャマッピングの計算（tex_xやtex_y）に誤差**があり、視点や座標の変化がテクスチャに不正に反映されている。
    
- **望ましい動作**：
    
    　壁の模様は固定されたまま、**カメラの動きに影響されずに表示**されてほしい。
    

---

### **③** 

### **プレイヤーが壁にめり込み、視点が壁内に入る**

- **現象**：
    
    　プレイヤーが壁に近づきすぎると**内部に入り込み視界が埋まる**。そのまま横を向くと視点の半分が壁の中になる。
    
- **問題点**：
    
    　**壁との接触チェック（衝突判定）が不十分**で、座標的に壁の内側まで移動できてしまう。
    
- **望ましい動作**：
    
    　壁に近づいても**一定の距離で止まり**、物理的に侵入できないようにしたい。


バグの原因を詳しく調査いたします。各問題について、関連するファイルと関数を特定し、修正方法を提案いたします。

## ① 不正なマップが読み込まれても実行できてしまう

### 🔍 **問題の調査**

Read file: src/parser/parse_colors.c
Read file: src/parser/parse_validation.c
Read file: src/parser/parser_utils.c
### 🚨 **問題①の原因と修正箇所**

#### **修正が必要なファイルと関数:**

1. **`src/parser/parse_colors.c`** - `parse_rgb_values()`関数
2. **`src/parser/parse_validation.c`** - `process_single_line()`関数
3. **`src/parser/parser_utils.c`** - 新しい検証関数の追加

#### **具体的な問題:**

```c
// 現在の実装（問題あり）
static int	parse_rgb_values(char *str, t_color *color)
{
	char	**rgb_parts;
	int		i;

	rgb_parts = ft_split(str, ',');  // カンマで分割
	if (!rgb_parts)
		return (error_msg("Failed to split RGB values"), 0);
	i = 0;
	while (rgb_parts[i])
		i++;
	if (i != 3)  // 3つの値のみチェック
		return (ft_free_split(rgb_parts),
			error_msg("RGB must have exactly 3 values"), 0);
	// 空文字列や不正な値のチェックが不十分
}
```

#### **修正案:**
```c
static int	parse_rgb_values(char *str, t_color *color)
{
	char	**rgb_parts;
	int		i;

	// 空文字列チェック
	if (!str || ft_strlen(str) == 0)
		return (error_msg("Empty RGB string"), 0);
	
	// 連続カンマチェック
	if (ft_strnstr(str, ",,", ft_strlen(str)))
		return (error_msg("Invalid RGB format: consecutive commas"), 0);
	
	// 先頭・末尾カンマチェック
	if (str[0] == ',' || str[ft_strlen(str) - 1] == ',')
		return (error_msg("Invalid RGB format: comma at start or end"), 0);
	
	rgb_parts = ft_split(str, ',');
	if (!rgb_parts)
		return (error_msg("Failed to split RGB values"), 0);
	
	i = 0;
	while (rgb_parts[i])
		i++;
	if (i != 3)
		return (ft_free_split(rgb_parts),
			error_msg("RGB must have exactly 3 values"), 0);
	
	// 各値の詳細チェック
	for (i = 0; i < 3; i++)
	{
		if (ft_strlen(rgb_parts[i]) == 0)
			return (ft_free_split(rgb_parts),
				error_msg("Empty RGB value"), 0);
	}
	
	if (!safe_atoi(rgb_parts[0], &color->r)
		|| !safe_atoi(rgb_parts[1], &color->g)
		|| !safe_atoi(rgb_parts[2], &color->b))
	{
		ft_free_split(rgb_parts);
		return (error_msg("Invalid RGB values"), 0);
	}
	ft_free_split(rgb_parts);
	return (1);
}
```

## ② テクスチャの模様がプレイヤー移動と一緒に動いてしまう

### 🔍 **問題の調査**

Read file: src/render/texture_utils.c
### 🚨 **問題②の原因と修正箇所**

#### **修正が必要なファイルと関数:**

1. **`src/render/texture_utils.c`** - `get_texture_x()`関数
2. **`src/render/draw_utils.c`** - `draw_texture_column()`関数

#### **具体的な問題:**

```c
// 現在の実装（問題あり）
int	get_texture_x(t_ray *ray, t_texture *texture)
{
	double	wall_x;
	int		tex_x;

	if (ray->side == 0)
		wall_x = ray->ray_dir_y * ray->perp_wall_dist;  // プレイヤー位置なし
	else
		wall_x = ray->ray_dir_x * ray->perp_wall_dist;  // プレイヤー位置なし
	wall_x -= floor(wall_x);
	tex_x = (int)(wall_x * (double)texture->width);
	// ...
}
```

#### **修正案:**
```c
int	get_texture_x(t_game *game, t_ray *ray, t_texture *texture)
{
	double	wall_x;
	int		tex_x;

	if (ray->side == 0)
	{
		// X壁（北/南壁）の場合
		wall_x = game->scene.player.pos.y + ray->perp_wall_dist * ray->ray_dir_y;
	}
	else
	{
		// Y壁（東/西壁）の場合
		wall_x = game->scene.player.pos.x + ray->perp_wall_dist * ray->ray_dir_x;
	}
	
	wall_x -= floor(wall_x);
	tex_x = (int)(wall_x * (double)texture->width);
	
	if (ray->side == 0 && ray->ray_dir_x > 0)
		tex_x = texture->width - tex_x - 1;
	if (ray->side == 1 && ray->ray_dir_y < 0)
		tex_x = texture->width - tex_x - 1;
	
	return (tex_x);
}
```

## ③ プレイヤーが壁にめり込み、視点が壁内に入る

### 🔍 **問題の調査**

Read file: src/game/movement_utils.c
### 🚨 **問題③の原因と修正箇所**

#### **修正が必要なファイルと関数:**

1. **`src/game/movement_utils.c`** - `check_collision()`関数
2. **`src/game/movement.c`** - `move_forward_backward()`, `move_left_right()`関数
3. **`include/cub3d.h`** - 定数の調整

#### **具体的な問題:**

```c
// 現在の実装（問題あり）
int	check_collision(t_game *game, double x, double y)
{
	double	radius = COLLISION_RADIUS;  // 0.2 - 小さすぎる
	int		i;
	int		j;
	double	check_x;
	double	check_y;

	radius = COLLISION_RADIUS;
	i = -1;
	while (++i <= 1)  // 3x3グリッド - 不十分
	{
		j = -1;
		while (++j <= 1)
		{
			check_x = x + i * radius;
			check_y = y + j * radius;
			if (is_wall(game, check_x, check_y))
				return (1);
		}
	}
	return (0);
}
```

#### **修正案:**
```c
int	check_collision_improved(t_game *game, double x, double y)
{
	double	radius = 0.3;  // 衝突半径を大きく
	double	check_x, check_y;
	int		steps = 8;     // より細かいチェック
	double	angle_step = TWO_PI / steps;
	double	angle;
	int		i;

	i = 0;
	while (i < steps)
	{
		angle = i * angle_step;
		check_x = x + cos(angle) * radius;
		check_y = y + sin(angle) * radius;
		
		if (is_wall(game, check_x, check_y))
			return (1);
		i++;
	}
	return (0);
}

// 視点の壁への侵入を防ぐ関数
int	check_view_collision(t_game *game)
{
	double	view_distance = 0.1;
	double	check_x, check_y;
	
	check_x = game->scene.player.pos.x + game->scene.player.dir.x * view_distance;
	check_y = game->scene.player.pos.y + game->scene.player.dir.y * view_distance;
	
	return (is_wall(game, check_x, check_y));
}
```

## �� **修正が必要なファイル一覧**

### **① 不正なマップ読み込み問題**
1. **`src/parser/parse_colors.c`**
   - `parse_rgb_values()`関数の強化
   - 空文字列、連続カンマ、不正な値のチェック追加

2. **`src/parser/parse_validation.c`**
   - `process_single_line()`関数の強化
   - より厳密な行の検証

3. **`src/parser/parser_utils.c`**
   - 新しい検証関数の追加
   - 構文チェックの強化

### **② テクスチャ模様の移動問題**
1. **`src/render/texture_utils.c`**
   - `get_texture_x()`関数の修正
   - プレイヤー位置を考慮した計算

2. **`src/render/draw_utils.c`**
   - `draw_texture_column()`関数の修正
   - 関数シグネチャの更新

3. **`include/cub3d.h`**
   - 関数プロトタイプの更新

### **③ 壁への侵入問題**
1. **`src/game/movement_utils.c`**
   - `check_collision()`関数の改善
   - 新しい衝突判定関数の追加

2. **`src/game/movement.c`**
   - 移動関数の改善
   - 視点衝突チェックの追加

3. **`include/cub3d.h`**
   - 新しい定数と関数プロトタイプの追加

## �� **修正の優先順位**

1. **高優先度**: 問題①（不正なマップ読み込み）
   - セキュリティと安定性に直結
   - 他の問題の原因となる可能性

2. **中優先度**: 問題③（壁への侵入）
   - ゲーム体験に大きく影響
   - 視覚的な問題

3. **低優先度**: 問題②（テクスチャ模様の移動）
   - 視覚的な問題のみ
   - ゲームプレイには影響しない

これらの修正により、cub3Dはより堅牢で安全なプログラムになります。