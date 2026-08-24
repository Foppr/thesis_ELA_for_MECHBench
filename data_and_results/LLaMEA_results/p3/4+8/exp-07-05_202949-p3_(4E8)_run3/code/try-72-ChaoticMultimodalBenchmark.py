import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / dim) * np.exp(-np.arange(dim) / dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic quadratic terms with dynamic scaling
        result = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * self.chaotic_sequence[i]
            result += scale * (x[i] - 0.5)**2 + 0.1 * (x[i] + 0.5)**4
        
        # Fractional polynomial interactions with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 1.5 + 0.5 * np.sin(i)
                exp_j = 1.5 + 0.5 * np.cos(j)
                result += 0.3 * (x[i]**exp_i) * (x[j]**exp_j)
        
        # Nested sinusoidal modulations with multiple frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 0.3 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i])
        
        # Dynamically shifted global minimum using chaotic sequence
        shift = np.array([self.chaotic_sequence[i] * 0.3 for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add chaotic noise component with varying amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * np.pi * (i + 1)) * np.cos(x[i] * np.pi * (i + 2))
        result += 0.1 * noise
        
        # Higher-order polynomial with fractional exponents for increased complexity
        result += 0.001 * np.sum(np.abs(x)**1.7) + 0.0005 * np.sum(np.abs(x)**3.1)
        
        return result