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
        # Generate fractional Brownian motion-like sequence using Hurst parameter
        hurst = 0.7
        seq = np.zeros(self.dim)
        for i in range(self.dim):
            seq[i] = np.sin(i * np.pi * hurst) + np.cos(i * np.pi * hurst)
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic polynomial component with varying exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponent = 2 + int(chaotic_factor * 10) % 4
            result += chaotic_factor * (x[i]**exponent - exponent*x[i]**(exponent-1) + 
                                       (exponent*(exponent-1))/2 * x[i]**(exponent-2))
            
        # Fractional Brownian motion coupling with chaotic phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.fbm_sequence[j]
                result += 0.3 * np.sin(3 * np.pi * x[i] + phase) * np.cos(3 * np.pi * x[j] + phase)
                
        # Adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 0.5 * self.chaotic_sequence[0]
        result += 0.4 * np.sum(((x - center)**2) / (radius**2 + 1e-8))
        
        # High-frequency chaotic oscillation with nested chaotic modulation
        for i in range(self.dim):
            modulator = self.chaotic_sequence[i % len(self.chaotic_sequence)]
            result += 0.15 * np.sin(30 * x[i] * modulator + np.pi * self.fbm_sequence[i])
            
        # Add nested multi-modal structure with chaotic scaling
        for i in range(self.dim):
            scale = 1.0 + 0.3 * self.chaotic_sequence[i]
            result += 0.25 * np.sin(scale * x[i]) * np.cos(scale * x[i]**2)
            
        # Global minimum attractor with chaotic modulation
        result += 0.1 * np.sum(x**2) * (1.0 + 0.1 * self.chaotic_sequence[0])
        
        # Add a complex ruggedness component
        for i in range(self.dim):
            result += 0.05 * np.sin(50 * x[i] * self.chaotic_sequence[i]) * np.cos(50 * x[i] * self.fbm_sequence[i])
            
        return result