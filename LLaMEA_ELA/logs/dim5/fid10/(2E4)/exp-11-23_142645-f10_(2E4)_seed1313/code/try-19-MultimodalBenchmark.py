import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial term with mixed degrees for varied curvature
        poly_term = np.sum(x_normalized**4 + 0.5 * x_normalized**3 + 0.2 * x_normalized**2)
        
        # High-frequency trigonometric components creating many local minima
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(10 * np.pi * x_normalized[i]) * np.cos(5 * np.pi * x_normalized[i])
        
        # Exponential decay terms with interaction between dimensions
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-2.0 * (x_normalized[i] - 0.5)**2)
        
        # Interaction term between all dimensions with sine modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += np.sin(np.pi * x_normalized[i] * x_normalized[j])
        
        # Combine all terms with carefully chosen weights
        return 3.0 * poly_term + 2.5 * trig_term + 0.8 * exp_term + 0.3 * interaction_term