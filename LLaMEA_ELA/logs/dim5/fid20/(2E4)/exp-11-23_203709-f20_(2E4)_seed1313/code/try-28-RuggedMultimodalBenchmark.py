import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base sinusoidal component with varying frequencies
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin((i + 1) * np.pi * x[i] / 1.5) * np.cos((i + 1) * np.pi * x[i] / 2.5)
        
        # Polynomial interaction terms with different degrees
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Adaptive exponential barriers that change based on dimension
        barriers = 0
        for i in range(self.dim):
            barriers += np.exp(-0.5 * (x[i] - 1.5)**2) + np.exp(-0.5 * (x[i] + 1.5)**2) + 0.15 * np.abs(x[i])
        
        # Ruggedness through high-frequency sinusoidal perturbations
        ruggedness = 0
        for i in range(self.dim):
            ruggedness += np.sin(12 * x[i]) * np.cos(18 * x[i])
        
        # Combine all components with appropriate scaling
        return 3.5 * sinusoidal + 2.5 * polynomial + 1.7 * barriers + 0.6 * ruggedness + 10 * self.dim