import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Varying frequencies
            amp = 1.0 + 0.5 * np.sin(i)  # Varying amplitudes
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2)
        
        # Add a complex penalty term with multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.2 * (x_normalized[i]**6 - 3 * x_normalized[i]**4 + 2 * x_normalized[i]**2)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.05 * np.sin(10 * np.pi * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += 0.3 * np.sin(20 * np.pi * x_normalized[i]) * np.cos(15 * np.pi * x_normalized[i])
            
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory