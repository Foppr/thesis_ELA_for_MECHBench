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
            freq = 2**(i % 5 + 2)  # Increased frequency range
            amp = 1.5 + 0.8 * np.sin(i * 0.5)  # Increased amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] - 0.15)**2)
        
        # Add a complex penalty term with multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.3 * (x_normalized[i]**6 - 3 * x_normalized[i]**4 + 2 * x_normalized[i]**2) + \
                       0.1 * np.sin(5 * np.pi * x_normalized[i]) * np.cos(3 * np.pi * x_normalized[i])
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.1 * np.sin(15 * np.pi * x_normalized[i]) * np.exp(-0.15 * x_normalized[i]**2) + \
                            0.05 * np.cos(10 * np.pi * x_normalized[i]) * np.sin(7 * np.pi * x_normalized[i])
            
        # Add a highly oscillatory term to increase complexity
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += 0.4 * np.sin(25 * np.pi * x_normalized[i]) * np.cos(20 * np.pi * x_normalized[i]) + \
                          0.2 * np.sin(30 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Add a cross-term interaction to increase dimensionality challenge
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(8 * np.pi * x_normalized[i]) * np.cos(6 * np.pi * x_normalized[j])
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + cross_term