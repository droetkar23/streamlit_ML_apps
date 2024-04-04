import streamlit as st
from streamlit_drawable_canvas import st_canvas
import altair as alt
import numpy as np
from torch.nn import Softmax
import torch



from torchvision.models import resnet18, ResNet18_Weights

# model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

# for ch in model.named_children():
#     f"{ch}"
with st.container(border=True):
    auto_update_pred = st.checkbox("Predict while drawing", False)
    canv = st_canvas(
        background_color="black",
        stroke_color="white",
        width=400,
        update_streamlit=auto_update_pred
    )

    softmax = Softmax(0)
    out = (((torch.rand([10])+0.5)**1.6+0.5)**1.6+0.5)**1.6
    pred = softmax(out)
    # sorted_idcs = torch.argsort(pred, descending=True)
    # st.text(sorted_idcs)
    # pred_sorted = pred[sorted_idcs]
    # pred_sorted.tolist()

    # [{"digit": digit, "prob": prob} for digit, prob in zip(sorted_idcs.tolist(), pred_sorted.tolist())]
    # [{"digit": 1, "prob": 0.5}, {"digit": 2, "prob": 0.2}, {"digit": 3, "prob": 0.7}]
    data = alt.Data(values=[
        {"digit": digit, "prob": prob}
        for digit, prob in zip(range(10), pred.tolist())
    ])

    prob_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('prob:Q').scale(domain=(0,1)),  # specify quantitative data
        y=alt.Y('digit:N'),  # specify nominal data
    )

    st.altair_chart(prob_chart, use_container_width=True)