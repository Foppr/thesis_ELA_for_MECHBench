import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants
        self.r = 3.9  # Logistic map parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map for dimensionality
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic polynomial component
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**4 - 4*x[i]**3 + 6*x[i]**2 - 4*x[i] + 1)
            
        # Trigonometric coupling with chaotic phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                result += 0.5 * np.sin(2 * np.pi * x[i] + phase) * np.cos(2 * np.pi * x[j] + phase)
                
        # Spherical penalty with chaotic center
        center = np.array([self.chaotic_sequence[i] * 2.0 for i in range(self.dim)])
        result += 0.3 * np.sum((x - center)**2)
        
        # High-frequency chaotic oscillation
        for i in range(self.dim):
            result += 0.2 * np.sin(20 * x[i] * self.chaotic_sequence[i])
            
        # Add a global minimum attractor
        result += 0.1 * np.sum(x**2)
        
        return result