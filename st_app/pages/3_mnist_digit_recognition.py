import streamlit as st
from streamlit_drawable_canvas import st_canvas
import altair as alt
import numpy as np
from torch.nn import Softmax
import torch
import pytorch_lightning as pl
from torchvision import transforms



from torchvision.models import resnet18, ResNet18_Weights


from model_backend.mlp_mnist_classifier.model import MlpMnistClassifier
@st.cache_resource
def load_mnist_model():
    model = MlpMnistClassifier.load_from_checkpoint("model_backend/mlp_mnist_classifier/epoch=49-step=39100.ckpt")
    return model

model = load_mnist_model()
model.eval()
# with torch.no_grad():
#     st.text(model(torch.rand((1,784))))

input_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize(28),
    transforms.Normalize((0.1307,), (0.3081,)),
])

# for ch in model.named_children():
#     f"{ch}"
with st.container(border=True):
    auto_update_pred = st.checkbox("Predict while drawing", False)
    digit_input = st_canvas(
        background_color="black",
        stroke_color="white",
        width=400,
        update_streamlit=auto_update_pred
    )

    softmax = Softmax(0)
    # out = (((torch.rand([10])+0.5)**1.6+0.5)**1.6+0.5)**1.6
    # pred = softmax(out)
    # sorted_idcs = torch.argsort(pred, descending=True)
    # st.text(sorted_idcs)
    # pred_sorted = pred[sorted_idcs]
    # pred_sorted.tolist()

    # [{"digit": digit, "prob": prob} for digit, prob in zip(sorted_idcs.tolist(), pred_sorted.tolist())]
    # [{"digit": 1, "prob": 0.5}, {"digit": 2, "prob": 0.2}, {"digit": 3, "prob": 0.7}]
    # data = alt.Data(values=[
    #     {"digit": digit, "prob": prob}
    #     for digit, prob in zip(range(10), pred.tolist())
    # ])

    # prob_chart = alt.Chart(data).mark_bar().encode(
    #     x=alt.X('prob:Q').scale(domain=(0,1)),  # specify quantitative data
    #     y=alt.Y('digit:N'),  # specify nominal data
    # )

    # st.altair_chart(prob_chart, use_container_width=True,)
    transformed_input = input_transforms(digit_input.image_data[:,:,0]).permute(1,2,0)
    # transformed_input.shape
    flattened_input = transformed_input.view(-1,784)
    # st.text(transformed_input)
    st.image(transformed_input.numpy(),clamp=True,width=400)

    with torch.no_grad():
        pred = model(flattened_input).flatten()

    # pred = softmax(pred)
    st.text(pred.tolist())

    data = alt.Data(values=[
        {"digit": digit, "prob": prob}
        for digit, prob in zip(range(10), pred.tolist())
    ])

    data

    prob_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('prob:Q').scale(domain=(0,1)),  # specify quantitative data
        y=alt.Y('digit:N'),  # specify nominal data
    )

    st.altair_chart(prob_chart, use_container_width=True,)

