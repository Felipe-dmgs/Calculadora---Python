import Back_End as back;
import streamlit as st;


import streamlit as st
import plotly.graph_objects as go
import time

st.title("🔵 Barra de Progresso Circular Completa")

# placeholder pro gráfico
placeholder = st.empty()

for progresso in range(0, 101):
    fig = go.Figure(go.Pie(
        values=[progresso, 100 - progresso],
        hole=0.7,
        sort=False,
        direction="clockwise",
        marker=dict(colors=["#276653", "#454141"]),
        textinfo="none"
    ))

    # Adiciona o texto central (percentual)
    fig.add_annotation(
        text=f"{progresso}%",
        x=0.5, y=0.5,
        font_size=30,
        showarrow=False
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        width=300,
        height=300
    )

    placeholder.plotly_chart(fig, use_container_width=True)
    time.sleep(0.05)

st.success("✅ Concluído!")
