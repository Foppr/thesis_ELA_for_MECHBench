import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 2.5) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - 1.0)**2 + 0.3 * (x[i] + 1.0)**2 + 0.01 * x[i]**4
        
        # Chaotic interaction terms with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 1.0 + 4.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                result += dynamic_scale * (x[i] - x[j])**2 * np.sin(3.0 * (x[i] + x[j]))
        
        # Add chaotic sinusoidal components with varying frequencies
        for i in range(self.dim):
            result += 1.2 * np.sin(2.0 * x[i] + self.chaotic_sequence[i]) * np.cos(2.5 * x[i]) + \
                      0.6 * np.sin(4.5 * x[i] + self.chaotic_sequence[i]**2)
        
        # Add a global minimum shift based on chaotic sequence
        shift = np.array([self.chaotic_sequence[i] * 0.3 for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add high-frequency noise to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.2 * self.chaotic_sequence[i])
        result += noise
        
        # Add a complex polynomial term with mixed degrees
        result += 0.002 * np.sum(x**3) + 0.001 * np.sum(x**5) + 0.0005 * np.sum(x**7)
        
        return result