#!/usr/bin/env python3
"""
生成 Skills 文章所需的图片 - 专业版（无emoji）
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle, Polygon, Wedge
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义配色方案 - 专业商务风格
COLORS = {
    'primary': '#2563EB',      # 主色调-蓝色
    'secondary': '#10B981',    # 辅助色-绿色
    'accent': '#F59E0B',       # 强调色-橙色
    'warning': '#EF4444',      # 警示色-红色
    'light': '#F3F4F6',        # 浅灰色
    'dark': '#1F2937',         # 深灰色
    'white': '#FFFFFF',
    'skills': '#7C3AED',       # Skills层-紫色
    'blue_light': '#DBEAFE',
    'green_light': '#D1FAE5',
    'orange_light': '#FEF3C7',
    'red_light': '#FEE2E2',
    'purple_light': '#EDE9FE',
}

def create_image_1_four_elements():
    """图1：Skills 四个核心要素"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 中心圆
    center = Circle((6, 4), 1.3, facecolor=COLORS['skills'], edgecolor='white', linewidth=3)
    ax.add_patch(center)
    ax.text(6, 4.15, 'Skills', ha='center', va='center', fontsize=18, fontweight='bold', color='white')
    ax.text(6, 3.6, '四要素', ha='center', va='center', fontsize=14, color='white')

    # 四个要素
    elements = [
        {'pos': (3, 6.2), 'title': '角色', 'items': ['AI 以什么身份？', '服务谁？'], 'color': COLORS['primary']},
        {'pos': (9, 6.2), 'title': '依据', 'items': ['基于哪些资料？', '参考哪些规则？'], 'color': COLORS['secondary']},
        {'pos': (3, 1.8), 'title': '规则', 'items': ['什么情况下怎么答？', '边界在哪里？'], 'color': COLORS['accent']},
        {'pos': (9, 1.8), 'title': '输出', 'items': ['结果格式是什么？', '能不能直接执行？'], 'color': '#6366F1'},
    ]

    for elem in elements:
        x, y = elem['pos']
        # 背景框
        box = FancyBboxPatch((x-1.7, y-1), 3.4, 2, boxstyle="round,pad=0.1,rounding_size=0.3",
                             facecolor=elem['color'], edgecolor='white', linewidth=2)
        ax.add_patch(box)

        # 标题
        ax.text(x, y+0.5, elem['title'], ha='center', va='center', fontsize=16, fontweight='bold', color='white')

        # 内容
        for i, item in enumerate(elem['items']):
            ax.text(x, y-0.2-i*0.45, item, ha='center', va='center', fontsize=10, color='white')

        # 连接线
        ax.annotate('', xy=(6, 4), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2.5,
                                  connectionstyle='arc3,rad=0.2'))

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/01-four-elements.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 01-four-elements.png")


def create_image_2_three_values():
    """图2：Skills 三大价值"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')

    values = [
        {'x': 2.5, 'num': '01', 'title': '统一口径', 'items': ['减少同问不同答', '减少重复确认', '降低沟通成本'], 'color': COLORS['primary']},
        {'x': 7, 'num': '02', 'title': '降低偏差', 'items': ['关键条件提前讲清', '例外情况明确标注', '边界清晰可追溯'], 'color': COLORS['secondary']},
        {'x': 11.5, 'num': '03', 'title': '经验复用', 'items': ['骨干经验沉淀', '组织能力传承', '不依赖个人'], 'color': COLORS['accent']},
    ]

    for i, val in enumerate(values):
        x = val['x']

        # 顶部编号圆
        circle = Circle((x, 5), 0.5, facecolor=val['color'], edgecolor='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, 5, val['num'], ha='center', va='center', fontsize=14, fontweight='bold', color='white')

        # 标题
        ax.text(x, 4, val['title'], ha='center', va='center', fontsize=16, fontweight='bold', color=COLORS['dark'])

        # 内容框
        box = FancyBboxPatch((x-2, 0.8), 4, 2.5, boxstyle="round,pad=0.1,rounding_size=0.2",
                             facecolor=val['color'], edgecolor='none', alpha=0.15)
        ax.add_patch(box)

        # 左侧竖线装饰
        ax.plot([x-1.7, x-1.7], [1, 3.5], color=val['color'], linewidth=3)

        # 内容
        for j, item in enumerate(val['items']):
            ax.text(x-1.4, 3.1-j*0.65, item, ha='left', va='center', fontsize=11, color=COLORS['dark'])

        # 箭头连接
        if i < len(values) - 1:
            ax.annotate('', xy=(values[i+1]['x']-1.5, 3), xytext=(x+1.5, 3),
                       arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2))

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/02-three-values.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 02-three-values.png")


def create_image_3_architecture():
    """图3：AI 架构中 Skills 的位置"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 各层定义
    layers = [
        {'y': 8.5, 'label': '用户交互层', 'items': ['员工提问', '客户咨询', '任务发起'], 'color': COLORS['blue_light']},
        {'y': 7, 'label': '模型层', 'items': ['理解意图', '推理分析', '生成回答'], 'color': '#DBEAFE'},
        {'y': 5.5, 'label': '知识层', 'items': ['制度规范', '业务FAQ', '案例库'], 'color': COLORS['green_light']},
        {'y': 4, 'label': '工具层', 'items': ['数据查询', '系统对接', '脚本执行'], 'color': COLORS['orange_light']},
        {'y': 2.5, 'label': '工作流层', 'items': ['步骤编排', '条件分支', '结果汇总'], 'color': '#FCE7F3'},
        {'y': 1, 'label': '治理层', 'items': ['权限控制', '审计日志', '边界管理'], 'color': '#E5E7EB'},
    ]

    # 绘制各层
    for layer in layers:
        y = layer['y']
        # 背景框
        box = FancyBboxPatch((0.5, y-0.5), 6.5, 1.2, boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=layer['color'], edgecolor=COLORS['dark'], linewidth=1)
        ax.add_patch(box)
        ax.text(0.8, y+0.1, layer['label'], fontsize=12, fontweight='bold', color=COLORS['dark'])

        # 子项
        for i, item in enumerate(layer['items']):
            ax.text(3.2 + i*1.2, y-0.2, item, fontsize=9, color=COLORS['dark'], ha='center')

    # Skills 编排层 - 高亮
    skills_box = FancyBboxPatch((8, 2), 5.5, 6.5, boxstyle="round,pad=0.1,rounding_size=0.2",
                                 facecolor=COLORS['skills'], edgecolor='white', linewidth=4)
    ax.add_patch(skills_box)

    # Skills 内容
    ax.text(10.75, 7.8, 'Skills 编排层', fontsize=15, fontweight='bold', color='white', ha='center')

    # 分隔线
    ax.plot([8.5, 13], [7.3, 7.3], color='white', linewidth=1, alpha=0.5)

    skills_items = ['角色定义', '规则绑定', '能力组合', '输出规范']
    for i, item in enumerate(skills_items):
        # 小圆点装饰
        circle = Circle((9, 6.5-i*1.2), 0.15, facecolor='white', edgecolor='none')
        ax.add_patch(circle)
        ax.text(9.4, 6.5-i*1.2, item, fontsize=11, color='white', va='center')

    # 连接线
    ax.annotate('', xy=(8, 5.5), xytext=(7, 5.5),
               arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2.5))

    # 注释
    ax.text(10.75, 2.5, '组织各层能力\n按规则编排', fontsize=10, color='white', ha='center',
            style='italic', alpha=0.9)

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/03-architecture.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 03-architecture.png")


def create_image_4_comparison():
    """图4：有/无 Skills 对比"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))

    for idx, (ax, title, bg_color, border_color, content) in enumerate([
        (axes[0], '没有 Skills', COLORS['red_light'], COLORS['warning'], {
            'question': '买二送一和满减能同享吗？',
            'answer': '可以的，两个活动\n可以一起参加。',
            'result': 'X 信息不完整',
            'result2': 'X 需二次确认',
            'result3': 'X 可能误导门店'
        }),
        (axes[1], '有 Skills', COLORS['green_light'], COLORS['secondary'], {
            'question': '买二送一和满减能同享吗？',
            'answer': '根据《活动规范》第3.2条：\n\nX 两者不可同享\n\n买二送一：零食/坚果类\n满减：全场（特价除外）\n\n请顾客选择更优惠的活动',
            'result': 'V 口径清晰',
            'result2': 'V 可直接执行',
            'result3': 'V 有据可查'
        })
    ]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # 背景框
        box = FancyBboxPatch((0.3, 0.3), 9.4, 9.4, boxstyle="round,pad=0.1,rounding_size=0.3",
                             facecolor=bg_color, edgecolor=border_color, linewidth=3)
        ax.add_patch(box)

        # 标题栏
        header = FancyBboxPatch((0.5, 8.5), 9, 1, boxstyle="round,pad=0.05",
                                facecolor=border_color, edgecolor='none')
        ax.add_patch(header)

        # 标题带标记
        mark = 'X' if idx == 0 else 'V'
        ax.text(5, 9, f'{mark} {title}', fontsize=16, fontweight='bold', ha='center', color='white')

        # 问题
        ax.text(0.8, 7.8, 'Q 用户问题', fontsize=11, fontweight='bold', color=COLORS['dark'])
        ax.text(0.8, 7.2, content['question'], fontsize=10, color=COLORS['dark'])

        # 回答
        ax.text(0.8, 6.2, 'A AI 回答', fontsize=11, fontweight='bold', color=COLORS['dark'])

        # 回答框
        answer_box = FancyBboxPatch((0.6, 2.8), 8.6, 3.2, boxstyle="round,pad=0.05",
                                    facecolor='white', edgecolor=COLORS['dark'], linewidth=1)
        ax.add_patch(answer_box)
        ax.text(1, 5.6, content['answer'], fontsize=9, color=COLORS['dark'], va='top')

        # 结果
        ax.text(0.8, 2.2, '结果', fontsize=11, fontweight='bold', color=COLORS['dark'])
        result_color = COLORS['warning'] if idx == 0 else COLORS['secondary']
        ax.text(0.8, 1.6, content['result'], fontsize=10, color=result_color)
        ax.text(0.8, 1.2, content['result2'], fontsize=10, color=result_color)
        ax.text(0.8, 0.8, content['result3'], fontsize=10, color=result_color)

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/04-comparison.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 04-comparison.png")


def create_image_5_workflow():
    """图5：Skills 工作流程"""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # 流程节点
    steps = [
        {'x': 1.5, 'y': 4.5, 'label': '用户\n提问', 'color': COLORS['primary']},
        {'x': 4, 'y': 4.5, 'label': '识别\n意图', 'color': COLORS['secondary']},
        {'x': 6.5, 'y': 4.5, 'label': '检索\n知识', 'color': COLORS['accent']},
        {'x': 9, 'y': 4.5, 'label': '调用\n工具', 'color': '#6366F1'},
        {'x': 11.5, 'y': 4.5, 'label': '生成\n回答', 'color': COLORS['warning']},
    ]

    # 绘制节点和连接
    for i, step in enumerate(steps):
        # 节点圆
        circle = Circle((step['x'], step['y']), 0.7, facecolor=step['color'], edgecolor='white', linewidth=3)
        ax.add_patch(circle)
        ax.text(step['x'], step['y'], step['label'], ha='center', va='center', fontsize=10, color='white', fontweight='bold')

        # 连接箭头
        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-0.8, step['y']), xytext=(step['x']+0.8, step['y']),
                       arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2.5))

    # Skills 编排层框
    skills_box = FancyBboxPatch((2.5, 1.2), 9, 2.2, boxstyle="round,pad=0.1,rounding_size=0.2",
                                 facecolor=COLORS['purple_light'], edgecolor=COLORS['skills'], linewidth=2)
    ax.add_patch(skills_box)

    # Skills 标题
    ax.text(7, 3, 'Skills 编排层', fontsize=14, fontweight='bold', ha='center', color=COLORS['skills'])

    # Skills 功能
    skills_funcs = ['角色定义', '规则绑定', '能力组合', '输出规范']
    for i, func in enumerate(skills_funcs):
        x = 3.5 + i * 2.2
        box = FancyBboxPatch((x-0.9, 1.5), 1.8, 0.8, boxstyle="round,pad=0.02",
                             facecolor=COLORS['skills'], edgecolor='none', alpha=0.9)
        ax.add_patch(box)
        ax.text(x, 1.9, func, fontsize=9, ha='center', va='center', color='white')

    # 返回箭头（复盘迭代）
    ax.annotate('', xy=(4, 4.5-0.8), xytext=(11.5, 3.4),
               arrowprops=dict(arrowstyle='->', color=COLORS['secondary'], lw=2,
                              connectionstyle='arc3,rad=-0.3', linestyle='--'))
    ax.text(8, 3.8, '复盘迭代', fontsize=9, color=COLORS['secondary'], style='italic')

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/05-workflow.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 05-workflow.png")


def create_image_6_skill_package():
    """图6：Skills 能力包结构"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 中心：Skills 能力包
    center_box = FancyBboxPatch((4, 3), 4, 2, boxstyle="round,pad=0.1,rounding_size=0.3",
                                 facecolor=COLORS['skills'], edgecolor='white', linewidth=4)
    ax.add_patch(center_box)
    ax.text(6, 4.2, 'Skills', fontsize=18, fontweight='bold', ha='center', color='white')
    ax.text(6, 3.6, '能力包', fontsize=14, ha='center', color='white')

    # 四个组成部分
    components = [
        {'pos': (2, 6.5), 'title': '技能说明', 'items': '角色 / 目标 / 规则 / 边界', 'color': COLORS['primary']},
        {'pos': (10, 6.5), 'title': '知识资料', 'items': '制度 / 流程 / FAQ / 案例', 'color': COLORS['secondary']},
        {'pos': (2, 1.5), 'title': '工具能力', 'items': '查询 / 脚本 / 外部接口', 'color': COLORS['accent']},
        {'pos': (10, 1.5), 'title': '输出规范', 'items': '格式 / 长度 / 风险提示', 'color': '#6366F1'},
    ]

    for comp in components:
        x, y = comp['pos']
        # 组件框
        box = FancyBboxPatch((x-1.8, y-0.8), 3.6, 1.6, boxstyle="round,pad=0.05,rounding_size=0.2",
                             facecolor=comp['color'], edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y+0.3, comp['title'], fontsize=13, fontweight='bold', ha='center', color='white')
        ax.text(x, y-0.3, comp['items'], fontsize=9, ha='center', color='white', alpha=0.9)

        # 连接到中心
        ax.annotate('', xy=(6, 4), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2.5, connectionstyle='arc3,rad=0.2'))

    # 输出箭头
    output_box = FancyBboxPatch((10.3, 3.3), 1.4, 1.4, boxstyle="round,pad=0.05",
                                facecolor=COLORS['secondary'], edgecolor='white', linewidth=2)
    ax.add_patch(output_box)
    ax.text(11, 4.2, '稳定', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(11, 3.7, '输出', fontsize=11, fontweight='bold', ha='center', color='white')

    ax.annotate('', xy=(10.3, 4), xytext=(8, 4),
               arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2.5))

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/06-skill-package.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 06-skill-package.png")


def create_image_7_platforms():
    """图7：三大平台对比"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 三个平台
    platforms = [
        {'x': 2.5, 'name': 'Claude Code', 'file': 'SKILL.md', 'features': ['自动/手动触发', '项目级/用户级', '原生知识绑定'], 'color': COLORS['primary']},
        {'x': 7, 'name': 'OpenClaw', 'subtitle': '小龙虾', 'file': 'SKILL.md', 'features': ['开源可定制', '自托管支持', '社区生态'], 'color': COLORS['secondary']},
        {'x': 11.5, 'name': 'OpenAI Codex', 'file': 'AGENTS.md', 'features': ['云服务集成', 'Function Calling', '企业级支持'], 'color': COLORS['accent']},
    ]

    for plat in platforms:
        x = plat['x']

        # 平台框
        box = FancyBboxPatch((x-2, 1), 4, 6, boxstyle="round,pad=0.1,rounding_size=0.2",
                             facecolor=plat['color'], edgecolor='none', alpha=0.1)
        ax.add_patch(box)

        # 标题栏
        header = FancyBboxPatch((x-2, 5.5), 4, 1.5, boxstyle="round,pad=0.05",
                                facecolor=plat['color'], edgecolor='white', linewidth=2)
        ax.add_patch(header)

        ax.text(x, 6.6, plat['name'], fontsize=13, fontweight='bold', ha='center', color='white')
        if 'subtitle' in plat:
            ax.text(x, 6.1, plat['subtitle'], fontsize=10, ha='center', color='white', alpha=0.9)

        # 配置文件
        ax.text(x, 5.9 if 'subtitle' not in plat else 5.7, f'{plat["file"]}', fontsize=10, ha='center', color='white')

        # 特性
        for i, feat in enumerate(plat['features']):
            # 小圆点
            circle = Circle((x-1.5, 4.5-i*1), 0.1, facecolor=plat['color'], edgecolor='none')
            ax.add_patch(circle)
            ax.text(x-1.3, 4.5-i*1, feat, fontsize=10, ha='left', va='center', color=COLORS['dark'])

    # 底部共同目标
    goal_box = FancyBboxPatch((3, 0.2), 8, 0.8, boxstyle="round,pad=0.05",
                              facecolor=COLORS['skills'], edgecolor='white', linewidth=2)
    ax.add_patch(goal_box)
    ax.text(7, 0.6, '共同目标：让 AI 按规则做事', fontsize=12, fontweight='bold', ha='center', color='white')

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/07-platforms.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 07-platforms.png")


def create_image_8_mistakes():
    """图8：三个常见误区"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')

    mistakes = [
        {'x': 2.5, 'wrong': '模型越来越强\n就不需要 Skills', 'right': '模型变强 不等于 口径统一\nSkills 决定稳定下限', 'color': COLORS['warning']},
        {'x': 7, 'wrong': '写一段提示词\n就算做完 Skills', 'right': 'Skills 是持续迭代的\n能力包，不是一次性的', 'color': COLORS['accent']},
        {'x': 11.5, 'wrong': 'Skills 只和\n技术团队有关', 'right': '业务团队才是规则\n边界和案例的来源', 'color': COLORS['primary']},
    ]

    for i, m in enumerate(mistakes):
        x = m['x']

        # 错误理解（红色系）
        wrong_box = FancyBboxPatch((x-2, 3.3), 4, 2, boxstyle="round,pad=0.05",
                                   facecolor=COLORS['red_light'], edgecolor=m['color'], linewidth=2)
        ax.add_patch(wrong_box)

        # X 标记
        ax.text(x-1.7, 5, 'X', fontsize=12, fontweight='bold', color=m['color'])
        ax.text(x, 4.7, '误区', fontsize=10, fontweight='bold', ha='center', color=m['color'])
        ax.text(x, 3.9, m['wrong'], fontsize=9, ha='center', va='center', color=COLORS['dark'])

        # 箭头
        ax.annotate('', xy=(x, 2.9), xytext=(x, 3.3),
                   arrowprops=dict(arrowstyle='->', color=COLORS['secondary'], lw=3))

        # 正确理解（绿色系）
        right_box = FancyBboxPatch((x-2, 0.5), 4, 2, boxstyle="round,pad=0.05",
                                   facecolor=COLORS['green_light'], edgecolor=COLORS['secondary'], linewidth=2)
        ax.add_patch(right_box)

        # V 标记
        ax.text(x-1.7, 2.2, 'V', fontsize=12, fontweight='bold', color=COLORS['secondary'])
        ax.text(x, 2, '正解', fontsize=10, fontweight='bold', ha='center', color=COLORS['secondary'])
        ax.text(x, 1.3, m['right'], fontsize=9, ha='center', va='center', color=COLORS['dark'])

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/08-mistakes.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 08-mistakes.png")


def create_image_9_scenarios():
    """图9：Skills 适用场景矩阵"""
    fig, ax = plt.subplots(figsize=(10, 10))

    # 四象限图
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # 绘制四象限背景
    ax.axhline(y=5, color=COLORS['dark'], linewidth=1, alpha=0.3)
    ax.axvline(x=5, color=COLORS['dark'], linewidth=1, alpha=0.3)

    # 四象限标签
    ax.fill_between([5, 10], 5, 10, alpha=0.2, color=COLORS['warning'])  # 右上-重点投入
    ax.fill_between([0, 5], 5, 10, alpha=0.2, color=COLORS['secondary'])  # 左上-优先建设
    ax.fill_between([5, 10], 0, 5, alpha=0.2, color=COLORS['primary'])    # 右下-逐步完善
    ax.fill_between([0, 5], 0, 5, alpha=0.2, color=COLORS['accent'])      # 左下-按需建设

    ax.text(7.5, 8.5, '重点投入', fontsize=12, fontweight='bold', ha='center', color=COLORS['warning'])
    ax.text(2.5, 8.5, '优先建设', fontsize=12, fontweight='bold', ha='center', color=COLORS['secondary'])
    ax.text(7.5, 1.5, '逐步完善', fontsize=12, fontweight='bold', ha='center', color=COLORS['primary'])
    ax.text(2.5, 1.5, '按需建设', fontsize=12, fontweight='bold', ha='center', color=COLORS['accent'])

    # 场景点
    scenarios = [
        {'x': 8, 'y': 7, 'label': '客服异常处理', 'size': 1500},
        {'x': 7, 'y': 6.5, 'label': '门店活动问答', 'size': 1200},
        {'x': 3, 'y': 7.5, 'label': '培训问答助手', 'size': 800},
        {'x': 4, 'y': 6, 'label': '门店SOP查询', 'size': 600},
        {'x': 6, 'y': 4, 'label': '营运复盘助手', 'size': 500},
        {'x': 3, 'y': 3, 'label': '财务报销问答', 'size': 700},
    ]

    for s in scenarios:
        ax.scatter(s['x'], s['y'], s=s['size'], alpha=0.6, color=COLORS['primary'])
        ax.text(s['x'], s['y']-0.5, s['label'], fontsize=10, ha='center', color=COLORS['dark'])

    # 坐标轴标签
    ax.text(5, 0, '< 低复用          高复用 >', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(0.3, 5, '高风险', fontsize=10, ha='center', va='center', color=COLORS['dark'], rotation=90)
    ax.text(9.7, 5, '低风险', fontsize=10, ha='center', va='center', color=COLORS['dark'], rotation=90)

    ax.set_title('Skills 适用场景矩阵', fontsize=14, fontweight='bold', pad=20)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('/Users/caoxingming/laiyifen-codes/ai_coding/hiagent-knowledge-base/skills-images/09-scenarios.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 生成: 09-scenarios.png")


if __name__ == '__main__':
    print("开始生成 Skills 图片（专业版）...")
    print("-" * 40)

    create_image_1_four_elements()
    create_image_2_three_values()
    create_image_3_architecture()
    create_image_4_comparison()
    create_image_5_workflow()
    create_image_6_skill_package()
    create_image_7_platforms()
    create_image_8_mistakes()
    create_image_9_scenarios()

    print("-" * 40)
    print("✅ 所有图片生成完成！")
    print("图片保存在: skills-images/")
