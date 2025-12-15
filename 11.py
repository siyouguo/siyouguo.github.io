from graphviz import Digraph

def create_roadmap():
    # 初始化图表
    dot = Digraph('Deepfake_Roadmap', comment='Deepfake Review Roadmap')
    
    # === 全局设置 ===
    # rankdir='LR': 从左到右布局
    # splines='ortho': 线条使用直角折线 (显得整洁)
    # nodesep='0.6': 节点间距
    dot.attr(rankdir='LR', splines='ortho', nodesep='0.6', ranksep='0.5', pad='0.5')
    dot.attr('node', fontname='Arial', fontsize='12')
    
    # === 配色方案 (莫兰迪色系) ===
    colors = {
        'main_bg': '#2C3E50',      # 主轴背景 (深蓝灰)
        'main_font': '#FFFFFF',    # 主轴文字 (白)
        'gen_bg': '#E8F6F3',       # 生成-背景 (淡青)
        'gen_border': '#1ABC9C',   # 生成-边框 (青)
        'det_bg': '#EBF5FB',       # 检测-背景 (淡蓝)
        'det_border': '#3498DB',   # 检测-边框 (蓝)
        'loc_bg': '#FEF5E7',       # 定位-背景 (淡橙)
        'loc_border': '#F39C12',   # 定位-边框 (橙)
        'eval_bg': '#F4ECF7',      # 评估-背景 (淡紫)
        'eval_border': '#9B59B6',  # 评估-边框 (紫)
        'fut_bg': '#F8F9F9',       # 未来-背景 (灰白)
        'fut_border': '#95A5A6'    # 未来-边框 (灰)
    }

    # === 定义 HTML 样式的卡片内容 ===
    # 这里使用 Graphviz 的 HTML-like Labels 功能来排版复杂的列表
    
    # 1. Generation Content
    label_gen = f'''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4" CELLPADDING="4" BGCOLOR="{colors['gen_bg']}">
        <TR><TD ALIGN="LEFT"><B><FONT COLOR="{colors['gen_border']}" POINT-SIZE="14">§2 Deepfake Generation</FONT></B></TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF"><B>Deep Generative Models</B><BR/>• VAEs / GANs / Diffusion Models</TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF"><B>Face-centric Manipulation</B><BR/>• Face Swapping & Reenactment<BR/>• Talking Face & Attribute Editing</TD></TR>
    </TABLE>>'''

    # 2. Detection Content
    label_det = f'''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4" CELLPADDING="4" BGCOLOR="{colors['det_bg']}">
        <TR><TD ALIGN="LEFT"><B><FONT COLOR="{colors['det_border']}" POINT-SIZE="14">§3 Deepfake Detection</FONT></B></TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF"><B>Spatial Domain</B><BR/>• Color, Boundary, Noise, Texture</TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF"><B>Temporal Domain</B><BR/>• Physio-signals, Inter-frame Consistency</TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF"><B>Freq & Multi-modal</B><BR/>• Frequency Spectra, Audio-Visual Cues</TD></TR>
    </TABLE>>'''

    # 3. Localization Content
    label_loc = f'''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4" CELLPADDING="4" BGCOLOR="{colors['loc_bg']}">
        <TR><TD ALIGN="LEFT"><B><FONT COLOR="{colors['loc_border']}" POINT-SIZE="14">§4 Localization & Adv.</FONT></B></TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF">• Attention-Based Methods<BR/>• Artifact/Anomaly-Based<BR/>• Spatio-temporal/Motion-based<BR/>• Proactive Defense (Watermarking)</TD></TR>
    </TABLE>>'''

    # 4. Evaluation Content
    label_eval = f'''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4" CELLPADDING="4" BGCOLOR="{colors['eval_bg']}">
        <TR><TD ALIGN="LEFT"><B><FONT COLOR="{colors['eval_border']}" POINT-SIZE="14">§5 Eval & Benchmarks</FONT></B></TD></TR>
        <TR><TD ALIGN="LEFT" BGCOLOR="#FFFFFF">• Benchmark Datasets<BR/>• Evaluation Metrics<BR/>• Performance Analysis</TD></TR>
    </TABLE>>'''

    # 5. Future Content
    label_fut = f'''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4" CELLPADDING="4" BGCOLOR="{colors['fut_bg']}">
        <TR><TD ALIGN="LEFT"><B><FONT COLOR="{colors['fut_border']}" POINT-SIZE="14">§6 Future Prospects</FONT></B></TD></TR>
        <TR><TD ALIGN="LEFT">• Proactive Defense & Attribution<BR/>• Generalization vs Unseen Threats<BR/>• Robustness (Compression/Noise)<BR/>• Real-time Detection</TD></TR>
    </TABLE>>'''

    # === 创建主轴节点 (Main Backbone) ===
    # 使用统一的深色胶囊形状
    main_node_attr = {
        'shape': 'rect', 'style': 'filled,rounded', 
        'fillcolor': colors['main_bg'], 'fontcolor': colors['main_font'],
        'penwidth': '0', 'height': '0.6', 'width': '1.5'
    }

    dot.node('S1', '§1 Introduction', **main_node_attr)
    dot.node('S2', '§2 Generation', **main_node_attr)
    dot.node('S3', '§3 Detection', **main_node_attr)
    dot.node('S4', '§4 Localization', **main_node_attr)
    dot.node('S5', '§5 Benchmark', **main_node_attr)
    dot.node('S6', '§6 Future', **main_node_attr)
    dot.node('S7', '§7 Conclusion', **main_node_attr)

    # === 创建详情节点 (Detail Cards) ===
    # shape='plain' 意味着没有外框，完全由 HTML 表格控制样式
    dot.node('S2_Det', label_gen, shape='plain')
    dot.node('S3_Det', label_det, shape='plain')
    dot.node('S4_Det', label_loc, shape='plain')
    dot.node('S5_Det', label_eval, shape='plain')
    dot.node('S6_Det', label_fut, shape='plain')

    # === 布局对齐逻辑 ===
    # 使用 subgraph 和 rank='same' 强制详情卡片与对应的主节点在同一垂直线上
    
    # Generation: 详情在上方
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('S2_Det')
        s.node('S2')

    # Detection: 详情在下方 (通过连接顺序微调，Graphviz有时需要尝试，或者用 invisible edge)
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('S3')
        s.node('S3_Det')

    # Localization: 详情在上方
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('S4_Det')
        s.node('S4')
        
    # Evaluation: 详情在下方
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('S5')
        s.node('S5_Det')
        
    # Future: 详情在上方
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('S6_Det')
        s.node('S6')

    # === 绘制连接线 ===
    
    # 1. 主轴连接 (粗箭头)
    edge_attr = {'penwidth': '3', 'color': '#2C3E50', 'arrowsize': '0.8'}
    dot.edge('S1', 'S2', **edge_attr)
    dot.edge('S2', 'S3', **edge_attr)
    dot.edge('S3', 'S4', **edge_attr)
    dot.edge('S4', 'S5', **edge_attr)
    dot.edge('S5', 'S6', **edge_attr)
    dot.edge('S6', 'S7', **edge_attr)

    # 2. 详情连接 (虚线，灰色)
    # Dir='none' 表示无箭头，单纯的连接线
    detail_edge_attr = {'style': 'dashed', 'color': '#95A5A6', 'penwidth': '1.5', 'dir': 'none'}
    
    dot.edge('S2', 'S2_Det', **detail_edge_attr)
    dot.edge('S3', 'S3_Det', **detail_edge_attr)
    dot.edge('S4', 'S4_Det', **detail_edge_attr)
    dot.edge('S5', 'S5_Det', **detail_edge_attr)
    dot.edge('S6', 'S6_Det', **detail_edge_attr)

    # === 输出文件 ===
    # format='png' 或者 'pdf' (PDF 适合插入 LaTeX 论文)
    output_path = dot.render(filename='deepfake_roadmap', format='png', cleanup=True, view=False)
    print(f"Roadmap generated successfully at: {output_path}")

if __name__ == '__main__':
    create_roadmap()