import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with slight modification
        self.r = 3.85  # Slightly reduced logistic map parameter
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
        
        # Chaotic polynomial component with modified coefficients
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**4 - 3.5*x[i]**3 + 5.5*x[i]**2 - 3*x[i] + 0.8)
            
        # Trigonometric coupling with enhanced chaotic phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] * 1.5
                result += 0.7 * np.sin(2 * np.pi * x[i] + phase) * np.cos(2 * np.pi * x[j] + phase)
                
        # Spherical penalty with shifted chaotic center
        center = np.array([self.chaotic_sequence[i] * 1.8 for i in range(self.dim)])
        result += 0.4 * np.sum((x - center)**2)
        
        # High-frequency chaotic oscillation with modified amplitude
        for i in range(self.dim):
            result += 0.25 * np.sin(25 * x[i] * self.chaotic_sequence[i])
            
        # Add a global minimum attractor with different weight
        result += 0.12 * np.sum(x**2)
        
        return result