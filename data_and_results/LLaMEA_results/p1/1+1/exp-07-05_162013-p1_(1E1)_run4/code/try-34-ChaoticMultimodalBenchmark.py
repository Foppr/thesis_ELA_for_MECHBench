import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with nested logistic maps
        self.r1, self.r2 = 3.9, 3.8
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using nested logistic maps for increased complexity
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3
        for i in range(self.dim):
            x1 = self.r1 * x1 * (1 - x1)
            x2 = self.r2 * x2 * (1 - x2)
            seq[i] = 0.5 * x1 + 0.5 * x2
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic polynomial component with higher-order terms
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**6 - 6*x[i]**5 + 15*x[i]**4 - 20*x[i]**3 + 15*x[i]**2 - 6*x[i] + 1)
            
        # Trigonometric coupling with dynamic phases and amplitude modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] * np.pi
                amp = 0.5 * (1 + np.sin(self.chaotic_sequence[i] * 10))
                result += amp * np.sin(2 * np.pi * x[i] + phase) * np.cos(2 * np.pi * x[j] + phase)
                
        # Hybrid penalty with spherical and logarithmic components
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        spherical_penalty = 0.2 * np.sum((x - center)**2)
        log_penalty = 0.1 * np.sum(np.log(1 + (x - center)**2))
        result += spherical_penalty + log_penalty
        
        # High-frequency chaotic oscillation with dynamic frequency
        for i in range(self.dim):
            freq = 30 * (1 + self.chaotic_sequence[i])
            result += 0.15 * np.sin(freq * x[i])
            
        # Add a global minimum attractor with chaotic weighting
        global_attraction = 0.05 * np.sum(x**2)
        chaotic_weight = np.mean(self.chaotic_sequence)
        result += chaotic_weight * global_attraction
        
        # Introduce a secondary chaotic basin structure
        basin_shift = np.array([np.sin(self.chaotic_sequence[i] * 20) * 0.5 for i in range(self.dim)])
        result += 0.1 * np.sum((x - basin_shift)**4)
        
        return result