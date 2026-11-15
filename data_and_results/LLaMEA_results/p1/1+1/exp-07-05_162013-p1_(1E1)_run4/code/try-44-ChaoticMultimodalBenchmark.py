import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with fractional exponents
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.fractional_exponents = np.random.uniform(0.3, 1.7, dim)
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using nested logistic maps for dimensionality
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        # Apply fractional transformation for added complexity
        seq = np.power(seq, 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.7))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic polynomial component with varying exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponent = self.fractional_exponents[i]
            result += chaotic_factor * np.power(x[i], 5) * np.sin(exponent * x[i])
            
        # Fractional Brownian motion-like coupling with chaotic correlations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlation = np.sin(self.chaotic_sequence[i] * self.chaotic_sequence[j] * 3.14159)
                result += 0.3 * correlation * np.sin(3 * x[i]) * np.cos(2 * x[j])
                
        # Adaptive spherical penalty with chaotic center and time-varying radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 0.5 * np.sin(np.sum(self.chaotic_sequence))
        result += 0.4 * np.sum(((x - center) / radius)**2)
        
        # Fractal-like high-frequency chaotic oscillation
        for i in range(self.dim):
            freq = 10 + 20 * self.chaotic_sequence[i]
            result += 0.15 * np.sin(freq * x[i] * self.chaotic_sequence[i]) * np.cos(freq * x[i] * self.chaotic_sequence[i])
            
        # Add global minimum attractor with chaotic scaling
        scaling = 0.5 + 0.5 * np.prod(self.chaotic_sequence)
        result += 0.05 * scaling * np.sum(x**2)
        
        # Add a secondary chaotic basin with different scaling
        basin_shift = np.sin(self.chaotic_sequence[:min(3, self.dim)])
        if len(basin_shift) > 0:
            result += 0.2 * np.sum((x[:len(basin_shift)] - basin_shift)**4)
            
        return result