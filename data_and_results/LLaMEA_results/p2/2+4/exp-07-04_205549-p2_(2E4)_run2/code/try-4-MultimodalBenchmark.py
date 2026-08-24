import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic component with exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-np.abs(x_scaled[i])) * np.sin(10 * np.pi * x_scaled[i])
        
        # Sinusoidal modulation with varying frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(3 * np.pi * x_scaled[i]) * np.cos(7 * np.pi * x_scaled[i])
        
        # Add a multi-modal penalty term with exponential decay
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * np.exp(-0.5 * (x_scaled[i] - 0.3)**2) * (x_scaled[i]**2 - 0.1)
            
        # Combine all components
        return quadratic + 0.3 * chaotic + 0.2 * sinusoidal + penalty