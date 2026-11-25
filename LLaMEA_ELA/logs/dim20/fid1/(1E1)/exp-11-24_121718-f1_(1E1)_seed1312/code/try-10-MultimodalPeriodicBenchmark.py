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
            chaotic += np.sin(15 * np.pi * x[i]) * np.cos(11 * np.pi * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Exponential barrier terms to create narrow valleys and plateaus
        barriers = 0.0
        for i in range(self.dim):
            barriers += np.exp(-0.4 * (x[i] - 2.5)**2) + np.exp(-0.4 * (x[i] + 2.5)**2) + \
                       np.exp(-0.2 * (x[i] - 4)**2) + np.exp(-0.2 * (x[i] + 4)**2)
        
        # Nested basin structure with multiple local minima
        nested = 0.0
        for i in range(self.dim):
            nested += 0.2 * np.sin(25 * np.pi * x[i]) * np.exp(-0.15 * (x[i] - 1.5)**2) + \
                      0.25 * np.cos(20 * np.pi * x[i]) * np.exp(-0.1 * (x[i] + 2)**2) + \
                      0.15 * np.sin(30 * np.pi * x[i]) * np.exp(-0.08 * (x[i] - 3.5)**2)
        
        # Additional complex interaction terms to increase landscape complexity
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(5 * np.pi * (x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combine all terms with varying weights to create a highly complex landscape
        return quadratic + 0.9 * chaotic + 0.5 * barriers + 0.4 * nested + 0.2 * interaction