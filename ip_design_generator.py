#!/usr/bin/env python3
"""IP设计程序：访谈式采集需求并一键生成完整IP套件。"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from textwrap import dedent


@dataclass
class IPBrief:
    project_name: str
    character_name: str
    role_title: str
    locale_context: str
    keywords: str
    target_audience: str
    personality: str
    color_preferences: str
    usage_scenarios: str
    story_background: str
    slogan: str
    output_style: str


def ask(prompt: str, default: str = "") -> str:
    value = input(f"{prompt}{f'（默认：{default}）' if default else ''}: ").strip()
    return value or default


def interview_user(preset: str | None = None) -> IPBrief:
    if preset == "huangpu_rabbit":
        defaults = {
            "project_name": "黄埔豫园",
            "character_name": "豫兔YUTO",
            "role_title": "品牌代言人",
            "locale_context": "上海黄浦区豫园商圈",
            "keywords": "海派,国潮,灵动,亲和,节庆",
            "target_audience": "家庭游客、年轻消费者、城市文旅人群",
            "personality": "机灵、温暖、懂礼、爱分享",
            "color_preferences": "豫园红、琉璃金、玉石白",
            "usage_scenarios": "文旅导览、节庆活动、联名周边、社媒传播",
            "story_background": "来自豫园灯会的一束灵光，化作守护街巷烟火气的小兔子",
            "slogan": "豫见好时光",
            "output_style": "国潮剪影+现代扁平",
        }
    else:
        defaults = {
            "project_name": "星旅计划",
            "character_name": "星仔",
            "role_title": "品牌形象代言人",
            "locale_context": "城市文旅与年轻社群",
            "keywords": "科技,治愈,冒险",
            "target_audience": "15-35岁泛二次元与文旅人群",
            "personality": "好奇、勇敢、温暖",
            "color_preferences": "电光蓝、暖橙、云白",
            "usage_scenarios": "海报、社媒、文创、导视",
            "story_background": "来自流星带的导航员，帮助城市找回想象力",
            "slogan": "和想象力一起出发",
            "output_style": "扁平几何+轻拟物",
        }

    print("\n🎨 欢迎使用IP设计程序。请回答以下问题，系统将自动产出整套IP方案。\n")
    return IPBrief(
        project_name=ask("1) 项目名称", defaults["project_name"]),
        character_name=ask("2) IP形象名称", defaults["character_name"]),
        role_title=ask("3) 形象定位", defaults["role_title"]),
        locale_context=ask("4) 地域/场景背景", defaults["locale_context"]),
        keywords=ask("5) 关键词（逗号分隔）", defaults["keywords"]),
        target_audience=ask("6) 目标受众", defaults["target_audience"]),
        personality=ask("7) 形象性格", defaults["personality"]),
        color_preferences=ask("8) 色彩偏好", defaults["color_preferences"]),
        usage_scenarios=ask("9) 应用场景", defaults["usage_scenarios"]),
        story_background=ask("10) 故事背景", defaults["story_background"]),
        slogan=ask("11) 宣传语", defaults["slogan"]),
        output_style=ask("12) 输出风格", defaults["output_style"]),
    )


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build_character_svg(brief: IPBrief) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1400" viewBox="0 0 1400 1400">
<rect width="1400" height="1400" fill="#FFF7F1"/>
<ellipse cx="700" cy="810" rx="300" ry="260" fill="#F45A5A"/>
<circle cx="700" cy="560" r="250" fill="#FFFFFF" stroke="#E54242" stroke-width="18"/>
<ellipse cx="610" cy="340" rx="80" ry="210" fill="#FFFFFF" stroke="#E54242" stroke-width="16"/>
<ellipse cx="790" cy="340" rx="80" ry="210" fill="#FFFFFF" stroke="#E54242" stroke-width="16"/>
<circle cx="620" cy="550" r="22" fill="#3B2A2A"/><circle cx="780" cy="550" r="22" fill="#3B2A2A"/>
<path d="M620 650 Q700 720 780 650" stroke="#3B2A2A" stroke-width="16" fill="none" stroke-linecap="round"/>
<text x="700" y="130" text-anchor="middle" font-size="62" fill="#8D1A1A">{brief.project_name} · {brief.character_name}</text>
<text x="700" y="1220" text-anchor="middle" font-size="40" fill="#8D1A1A">{brief.role_title}｜{brief.slogan}</text>
</svg>'''


def build_three_view_svg(brief: IPBrief) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="900" viewBox="0 0 1400 900">
<rect width="1400" height="900" fill="#FFFFFF"/>
<text x="700" y="90" text-anchor="middle" font-size="56" fill="#8D1A1A">{brief.character_name} 三视图（{brief.output_style}）</text>
<g transform="translate(220,190)"><ellipse cx="0" cy="80" rx="44" ry="120" fill="#fff" stroke="#E54242" stroke-width="10"/><ellipse cx="70" cy="80" rx="44" ry="120" fill="#fff" stroke="#E54242" stroke-width="10"/><circle cx="35" cy="230" r="110" fill="#fff" stroke="#E54242" stroke-width="10"/><text x="35" y="420" text-anchor="middle" font-size="30">正视图</text></g>
<g transform="translate(650,190)"><ellipse cx="20" cy="80" rx="40" ry="120" fill="#fff" stroke="#E54242" stroke-width="10"/><circle cx="0" cy="230" r="100" fill="#fff" stroke="#E54242" stroke-width="10"/><text x="0" y="420" text-anchor="middle" font-size="30">侧视图</text></g>
<g transform="translate(1050,190)"><ellipse cx="-20" cy="80" rx="44" ry="120" fill="#fff" stroke="#E54242" stroke-width="10"/><ellipse cx="50" cy="80" rx="44" ry="120" fill="#fff" stroke="#E54242" stroke-width="10"/><circle cx="15" cy="230" r="110" fill="#fff" stroke="#E54242" stroke-width="10"/><text x="15" y="420" text-anchor="middle" font-size="30">背视图</text></g>
</svg>'''


def build_poster_svg(brief: IPBrief, idx: int) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1620" viewBox="0 0 1080 1620">
<defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop offset="0%" stop-color="#D94141"/><stop offset="100%" stop-color="#F7A44A"/></linearGradient></defs>
<rect width="1080" height="1620" fill="url(#g)"/>
<text x="540" y="190" text-anchor="middle" fill="#fff" font-size="72">{brief.project_name}</text>
<text x="540" y="270" text-anchor="middle" fill="#FFF2D9" font-size="40">{brief.character_name} 海报 {idx}</text>
<circle cx="540" cy="780" r="260" fill="#FFFFFF22"/>
<text x="540" y="1350" text-anchor="middle" fill="#fff" font-size="48">{brief.slogan}</text>
</svg>'''


def build_pattern_svg(brief: IPBrief) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200">
<rect width="1200" height="1200" fill="#FFF7F1"/>
<g fill="#E5424240">
<path d="M150 180 q60 -90 120 0 q-60 90 -120 0z"/><path d="M450 180 q60 -90 120 0 q-60 90 -120 0z"/><path d="M750 180 q60 -90 120 0 q-60 90 -120 0z"/>
<path d="M150 520 q60 -90 120 0 q-60 90 -120 0z"/><path d="M450 520 q60 -90 120 0 q-60 90 -120 0z"/><path d="M750 520 q60 -90 120 0 q-60 90 -120 0z"/>
<path d="M150 860 q60 -90 120 0 q-60 90 -120 0z"/><path d="M450 860 q60 -90 120 0 q-60 90 -120 0z"/><path d="M750 860 q60 -90 120 0 q-60 90 -120 0z"/>
</g>
<text x="600" y="1140" text-anchor="middle" font-size="36" fill="#8D1A1A">{brief.character_name} 底纹</text>
</svg>'''


def build_docs(brief: IPBrief) -> dict[str, str]:
    return {
        "03_font_system.md": f"# IP文字字体系统\n- 主题字体：站酷庆科黄油体（标题）\n- 正文字体：思源黑体\n- 英文辅助：Poppins\n- 关键词：{brief.keywords}\n- 色彩建议：{brief.color_preferences}\n",
        "05_application_guide.md": f"# IP海报系列及应用规范\n- 场景：{brief.usage_scenarios}\n- 版式：主角占比45%-65%\n- 安全区：四周≥1x字高\n- 应用尺寸：1080x1080 / 1080x1920 / A1\n",
        "06_text_usage.md": "# IP文字应用规范\n- 中文最小字号：24px\n- 标题和正文对比：≥1.6x\n- 禁止：描边过粗、拉伸、随意换色\n",
        "07_logo_combo.md": f"# 文字与形象组合规范\n- 横版：左图右字\n- 竖版：上图下字\n- 最小宽度：120px\n- 推荐口号：{brief.slogan}\n",
        "08_pattern_usage.md": "# IP底纹及应用\n- 默认透明度30%\n- 深色背景透明度15%\n- 可用于票券背面、包装内页、导视边框\n",
        "09_storyboard.md": f"# IP故事画板\n1. 在{brief.locale_context}登场，向游客问好。\n2. 引导用户探索在地文化与美食。\n3. 节庆夜晚点亮灯彩，成为城市记忆符号。\n4. 延展至盲盒、徽章、导览手册等文创。\n\n背景：{brief.story_background}\n",
        "10_extra_content.md": f"# 其他内容\n- 角色设定：{brief.character_name}，定位：{brief.role_title}\n- 受众：{brief.target_audience}\n- 输出风格：{brief.output_style}\n",
    }


def generate_suite(brief: IPBrief, out_dir: str) -> None:
    ensure_dir(out_dir)
    ensure_dir(os.path.join(out_dir, "assets"))
    ensure_dir(os.path.join(out_dir, "docs"))

    save(os.path.join(out_dir, "brief.json"), json.dumps(asdict(brief), ensure_ascii=False, indent=2))
    save(os.path.join(out_dir, "assets", "01_character_main.svg"), build_character_svg(brief))
    save(os.path.join(out_dir, "assets", "02_three_view.svg"), build_three_view_svg(brief))
    save(os.path.join(out_dir, "assets", "08_pattern.svg"), build_pattern_svg(brief))
    for i in range(1, 4):
        save(os.path.join(out_dir, "assets", f"04_poster_{i}.svg"), build_poster_svg(brief, i))
    for filename, content in build_docs(brief).items():
        save(os.path.join(out_dir, "docs", filename), content)

    readme = dedent(f"""
    # {brief.project_name} IP套件

    - 角色：{brief.character_name}（{brief.role_title}）
    - 地域：{brief.locale_context}
    - 生成时间：{datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

    ## 内容清单
    - IP形象主图：assets/01_character_main.svg
    - IP三视图：assets/02_three_view.svg
    - IP文字字体系统：docs/03_font_system.md
    - IP海报系列：assets/04_poster_1.svg ~ 04_poster_3.svg
    - IP海报系列及应用规范：docs/05_application_guide.md
    - IP文字应用规范：docs/06_text_usage.md
    - 文字与形象组合规范：docs/07_logo_combo.md
    - IP底纹及应用：assets/08_pattern.svg + docs/08_pattern_usage.md
    - IP故事画板：docs/09_storyboard.md
    - 其他内容：docs/10_extra_content.md
    """).strip() + "\n"
    save(os.path.join(out_dir, "README.md"), readme)


def main() -> None:
    parser = argparse.ArgumentParser(description="一键生成IP设计套件")
    parser.add_argument("--preset", choices=["huangpu_rabbit"], default=None, help="使用预设（如：黄埔豫园小兔子）")
    parser.add_argument("--out", default=None, help="输出目录名")
    args = parser.parse_args()

    brief = interview_user(args.preset)
    out_dir = args.out or f"output_{brief.project_name}_{brief.character_name}".replace(" ", "_")
    generate_suite(brief, out_dir)
    print(f"\n✅ 已生成：{out_dir}")


if __name__ == "__main__":
    main()
