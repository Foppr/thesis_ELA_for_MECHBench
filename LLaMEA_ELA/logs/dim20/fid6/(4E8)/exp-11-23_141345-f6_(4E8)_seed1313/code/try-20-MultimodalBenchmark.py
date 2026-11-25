import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial base term with varying degrees
        f1 = np.sum(x_scaled**6)
        
        # Trigonometric modulation with multiple frequencies
        f2 = 0.2 * np.sum(np.sin(3 * x_scaled) * np.cos(5 * x_scaled))
        
        # Exponential interaction terms to induce steep gradients
        f3 = 0.1 * np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        # Cross-term interactions with sinusoidal modulation
        f4 = 0.08 * np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Additional high-frequency oscillation to increase complexity
        f5 = 0.05 * np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5