_ 가 있는 현제 변수가 바뀜

broadcasting 

img_t = torch.randn(3, 5, 5) # 채널, x사이즈, y사이즈 크기를 가진 랜덤 텐서
batch_t = torch.randn(2,3,5,5) # 배치 크기 2, 채널 3, 높이와 너비가 5
weight = torch.tensor([0.2126 0.7152, 0.0722]) # RGB 채널에 대한 가중치 값, 일반적으로 이미지의 밝기를 계산할 때 사용
weight.shape

unsqueezed_weights = weights.unsqueez(-1).unsqueez_(-1) # unsqueeze(-1): 텐서의 마지막 차원에 새로운 차원을 추가합니다. 따라서 (3,)는 (3, 1)이 됩니다.
# unsqueeze_(-1): 동일한 방식으로 마지막에 또 하나의 차원을 추가하여 (3, 1)을 (3, 1, 1)로 변환합니다.
unsqueezed.shape