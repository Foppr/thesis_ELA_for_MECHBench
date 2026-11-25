import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with quadratic scaling
        f1 = np.sum(0.7 * np.exp(0.3 * x**2))
        
        # Increased sinusoidal coupling frequency and amplitude
        f2 = 0.8 * np.sum(np.sin(2.0 * (x[:-1] + x[1:])))
        
        # Modified asymmetric ridge with cubic terms
        f3 = 0.4 * np.sum((x[:-1] - x[1:]) ** 3)
        
        # Chaotic component with higher frequency trigonometric terms
        f4 = 0.3 * np.sum(np.sin(15.0 * np.abs(x)) * np.cos(7.0 * x))
        
        # Combine all terms with adjusted weights
        return f1 + f2 + f3 + f4