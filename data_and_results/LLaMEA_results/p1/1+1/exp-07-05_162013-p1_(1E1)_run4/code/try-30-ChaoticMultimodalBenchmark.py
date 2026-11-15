import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants
        self.r1 = 3.9  # Logistic map parameter
        self.r2 = 3.8  # Secondary chaotic parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.hyperchaotic_sequence = self._generate_hyperchaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map for dimensionality
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r1 * x * (1 - x)
            seq[i] = x
        return seq
    
    def _generate_hyperchaotic_sequence(self):
        # Generate a hyperchaotic sequence using coupled logistic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.5
        for i in range(self.dim):
            x1 = self.r1 * x1 * (1 - x1)
            x2 = self.r2 * x2 * (1 - x2)
            seq[i] = x1 + 0.1 * x2  # Coupled hyperchaotic component
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic polynomial component with hyperchaotic modulation
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            hyperchaotic_factor = self.hyperchaotic_sequence[i]
            result += chaotic_factor * (x[i]**4 - 4*x[i]**3 + 6*x[i]**2 - 4*x[i] + 1) + \
                     0.5 * hyperchaotic_factor * (x[i]**3 - 3*x[i]**2 + 3*x[i] - 1)
            
        # Trigonometric coupling with chaotic phases and hyperchaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                hyper_phase = self.hyperchaotic_sequence[i] * self.hyperchaotic_sequence[j]
                result += 0.5 * np.sin(2 * np.pi * x[i] + phase) * np.cos(2 * np.pi * x[j] + phase) + \
                         0.3 * np.sin(3 * np.pi * x[i] + hyper_phase) * np.cos(3 * np.pi * x[j] + hyper_phase)
                
        # Spherical penalty with chaotic and hyperchaotic centers
        center1 = np.array([self.chaotic_sequence[i] * 2.0 for i in range(self.dim)])
        center2 = np.array([self.hyperchaotic_sequence[i] * 1.5 for i in range(self.dim)])
        result += 0.3 * np.sum((x - center1)**2) + 0.2 * np.sum((x - center2)**2)
        
        # High-frequency chaotic oscillation with hyperchaotic modulation
        for i in range(self.dim):
            result += 0.2 * np.sin(20 * x[i] * self.chaotic_sequence[i]) + \
                     0.1 * np.cos(15 * x[i] * self.hyperchaotic_sequence[i])
            
        # Add a global minimum attractor with chaotic modulation
        result += 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(5 * x) * self.chaotic_sequence)
        
        # Cross-dimensional hyperchaotic interaction term
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.hyperchaotic_sequence[i] * self.hyperchaotic_sequence[j] * np.sin(x[i] + x[j])
        result += 0.15 * cross_term
        
        return result