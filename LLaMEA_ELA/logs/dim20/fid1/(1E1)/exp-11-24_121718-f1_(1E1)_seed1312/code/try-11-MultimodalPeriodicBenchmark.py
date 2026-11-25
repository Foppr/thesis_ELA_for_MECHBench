import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # High-frequency periodic multimodal component with chaotic interference
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Exponential barrier terms to create narrow valleys and plateaus
        barriers = 0.0
        for i in range(self.dim):
            barriers += np.exp(-0.5 * (x[i] - 3)**2) + np.exp(-0.5 * (x[i] + 3)**2) + np.exp(-0.3 * x[i]**2)
        
        # Nested basin structure with multiple local minima
        nested = 0.0
        for i in range(self.dim):
            nested += 0.1 * np.sin(20 * np.pi * x[i]) * np.exp(-0.1 * (x[i] - 2)**2) + \
                      0.15 * np.cos(15 * np.pi * x[i]) * np.exp(-0.05 * (x[i] + 1)**2)
        
        # Combine all terms with varying weights to create a highly complex landscape
        return quadratic + 0.8 * chaotic + 0.4 * barriers + 0.3 * nested