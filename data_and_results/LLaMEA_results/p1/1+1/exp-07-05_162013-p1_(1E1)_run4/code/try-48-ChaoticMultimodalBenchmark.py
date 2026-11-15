import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with improved parameter selection
        self.r = 3.8  # Slightly reduced for better control
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
        
        # Enhanced chaotic polynomial component with higher degree terms
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**5 - 5*x[i]**4 + 10*x[i]**3 - 10*x[i]**2 + 5*x[i] - 1)
            
        # Enhanced trigonometric coupling with multiple phase combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase1 = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                phase2 = np.sin(self.chaotic_sequence[i] + self.chaotic_sequence[j])
                result += 0.3 * np.sin(3 * np.pi * x[i] + phase1) * np.cos(3 * np.pi * x[j] + phase2)
                
        # Adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 0.5 * np.mean(self.chaotic_sequence)
        result += 0.4 * np.sum((x - center)**2) / (radius**2 + 1e-8)
        
        # Enhanced high-frequency chaotic oscillation with variable frequency
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i]
            result += 0.25 * np.sin(freq * x[i] * self.chaotic_sequence[i])
            
        # Add a global minimum attractor with chaotic weighting
        weight = np.mean(self.chaotic_sequence) + 0.5
        result += weight * 0.1 * np.sum(x**2)
        
        # Add a secondary chaotic landscape component for increased complexity
        for i in range(self.dim):
            result += 0.1 * np.cos(5 * x[i] * self.chaotic_sequence[i]) * np.sin(7 * x[i] * self.chaotic_sequence[i])
            
        return result