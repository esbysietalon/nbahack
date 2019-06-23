import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.array([[-1.0]]) #np.random.rand(self.input.shape[1],1) 
        self.weights2   = np.array([[-1.0]]) #np.random.rand(1,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        print(self.layer1)
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        print(self.output)


    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
        print(d_weights2)
        print(d_weights1)

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        print(self.weights1)
        print(self.weights2)


if __name__ == "__main__":
    X = np.array([[0.0]])
    y = np.array([[1]])
    nn = NeuralNetwork(X,y)

    for i in range(3):
        nn.feedforward()
        print(nn.feedforward())
        nn.backprop()
        print(nn.backprop())
    print(nn.output)