import streamlit as st
from torchvision.models import resnet18, ResNet18_Weights

model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

for ch in model.named_children():
    f"{ch}"
