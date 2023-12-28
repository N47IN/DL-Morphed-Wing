import torch
import torch.nn as nn

# Define the neural network model
class MyNetwork(nn.Module):
    def __init__(self):
        super(MyNetwork, self).__init__()
        self.fc1 = nn.Linear(10, 64)  
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)  
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(32, 2)   

    def forward(self, x):
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.fc3(x)
        return x

# Instantiate the model
model = MyNetwork()

# Print the model architecture
print(model)