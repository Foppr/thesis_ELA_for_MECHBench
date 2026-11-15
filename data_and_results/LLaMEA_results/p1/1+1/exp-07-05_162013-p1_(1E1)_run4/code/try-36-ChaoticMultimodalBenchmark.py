import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with enhanced complexity
        self.r = 3.8  # Slightly different logistic map parameter for more chaos
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map with enhanced sensitivity
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
        
        # Chaotic polynomial component with higher degree terms
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**5 - 5*x[i]**4 + 10*x[i]**3 - 10*x[i]**2 + 5*x[i] - 1)
            
        # Enhanced trigonometric coupling with multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                result += 0.3 * np.sin(3 * np.pi * x[i] + phase) * np.cos(3 * np.pi * x[j] + phase) + \
                         0.2 * np.sin(5 * np.pi * x[i] + phase) * np.cos(5 * np.pi * x[j] + phase)
                
        # Adaptive spherical penalty with chaotic center and variable weights
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        weights = np.array([self.chaotic_sequence[i] * 0.5 + 0.5 for i in range(self.dim)])
        result += 0.4 * np.sum(weights * (x - center)**2)
        
        # High-frequency chaotic oscillation with variable frequency
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i]
            result += 0.15 * np.sin(freq * x[i] * self.chaotic_sequence[i])
            
        # Add a global minimum attractor with chaotic scaling
        scale = np.mean(self.chaotic_sequence) * 0.5 + 0.5
        result += 0.05 * scale * np.sum(x**2)
        
        # Add a secondary chaotic basin to increase multimodality
        basin_shift = np.array([np.sin(self.chaotic_sequence[i] * np.pi) * 2.0 for i in range(self.dim)])
        result += 0.2 * np.sum((x - basin_shift)**4)
        
        return result