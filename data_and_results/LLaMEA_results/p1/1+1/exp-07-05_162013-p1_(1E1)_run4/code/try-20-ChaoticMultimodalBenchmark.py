import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants
        self.r = 3.9  # Logistic map parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.fbm_sequence = self._generate_fbm_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map for dimensionality
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def _generate_fbm_sequence(self):
        # Generate fractional Brownian motion-like sequence
        seq = np.zeros(self.dim)
        for i in range(self.dim):
            seq[i] = np.sin(i * 0.1) * np.cos(i * 0.05) + np.random.normal(0, 0.1)
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic polynomial component with varying exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponent = 2 + 3 * chaotic_factor  # Varying exponents
            result += chaotic_factor * (x[i]**exponent - exponent*x[i]**(exponent-1) + 
                                       (exponent*(exponent-1)/2)*x[i]**(exponent-2))
            
        # Fractional Brownian motion coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fbm_phase = self.fbm_sequence[i] * self.fbm_sequence[j]
                result += 0.3 * np.sin(3 * np.pi * x[i] + fbm_phase) * np.cos(3 * np.pi * x[j] + fbm_phase)
                
        # Adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 2.0 * np.mean(self.chaotic_sequence)
        result += 0.4 * np.sum((x - center)**2) / radius
        
        # Multi-scale chaotic oscillation
        for i in range(self.dim):
            scale = 10 + 20 * self.chaotic_sequence[i]
            result += 0.15 * np.sin(scale * x[i] * self.chaotic_sequence[i])
            
        # Nested attractor landscape
        for i in range(self.dim):
            nested_factor = 0.5 + 0.5 * np.sin(5 * np.pi * x[i])
            result += 0.25 * nested_factor * (x[i] - 2.5)**2
        
        # Add global minimum attractor with chaotic perturbation
        global_min = np.array([2.0 * self.chaotic_sequence[i] for i in range(self.dim)])
        result += 0.1 * np.sum((x - global_min)**2)
        
        # High-frequency chaotic modulation
        for i in range(self.dim):
            modulation = 1.0 + 0.5 * np.sin(50 * x[i] * self.chaotic_sequence[i])
            result += 0.1 * modulation * np.sin(30 * x[i])
            
        return result