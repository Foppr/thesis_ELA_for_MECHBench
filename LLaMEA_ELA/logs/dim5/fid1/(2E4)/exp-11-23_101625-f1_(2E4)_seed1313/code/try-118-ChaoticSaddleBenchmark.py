import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic saddle points with logistic map dynamics
        for i in range(self.dim):
            # Create chaotic attractor-like structures using logistic map
            logistic_val = 3.9 * (x[i] / 5.0) * (1 - x[i] / 5.0)
            result += 2.0 * np.abs(logistic_val - x[i] / 5.0) * np.exp(-0.5 * (x[i] / 5.0)**2)
            
        # Logarithmic barrier structures with adaptive exponents
        for i in range(self.dim):
            # Create logarithmic barriers near boundaries
            if x[i] > 0:
                result += 1.5 * np.log(1 + np.abs(x[i]) / 5.0) * np.exp(-0.1 * x[i]**2)
            else:
                result += 1.5 * np.log(1 + np.abs(x[i]) / 5.0) * np.exp(-0.1 * x[i]**2)
                
        # Adaptive coupling terms with dynamic interaction strengths
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Dynamic coupling strength based on position and dimension
                    coupling_strength = 1.0 + 0.5 * np.sin(i * 0.3 + j * 0.4 + np.sum(x) * 0.1)
                    distance = np.abs(x[i] - x[j])
                    coupling_sum += coupling_strength * np.exp(-distance**2 / (2.0 * (0.5 + 0.5 * np.cos(i * 0.2 + j * 0.3))))
            result += 0.8 * coupling_sum
            
        # Multi-scale harmonic components with chaotic phase modulation
        for i in range(self.dim):
            harmonic_sum = 0.0
            for k in range(1, 5):
                freq = k * np.pi * (1 + 0.3 * np.sin(i * 0.2 + np.sum(x) * 0.1))
                phase = k * 0.5 * np.sin(i * 0.3 + np.sum(x) * 0.2)
                harmonic_sum += (1.0 / k**1.5) * np.sin(freq * x[i] + phase)
            result += 1.2 * harmonic_sum**2
            
        # Fractal-like ridge patterns with varying smoothness
        for i in range(self.dim):
            ridge_val = 0.0
            for k in range(1, 8):
                scale = 2**(k // 2)
                freq = 2.0 * np.pi * scale
                ridge_val += (1.0 / scale**0.7) * np.cos(freq * x[i])
            result += 1.5 * ridge_val**3
            
        # Time-varying energy wells with chaotic position shifts
        for i in range(self.dim):
            # Create wells with positions that depend on chaotic dynamics
            well_pos = 2.0 * np.sin(i * 0.4 + np.sum(x) * 0.15) + 0.5 * np.sin(3 * i * 0.3 + np.sum(x) * 0.2)
            well_depth = 2.5 + 1.0 * np.cos(i * 0.5 + np.sum(x) * 0.1)
            result += well_depth * np.exp(-0.5 * ((x[i] - well_pos) / 0.7)**2)
            
        # Asymmetric exponential terms with chaotic scaling
        for i in range(self.dim):
            asym_scale = 1.0 + 0.3 * np.sin(i * 0.2 + np.sum(x) * 0.1)
            result += asym_scale * np.exp(0.8 * abs(x[i]) / 5.0) * (1 + 0.4 * np.cos(x[i] * 1.5))
            
        # Global irregularity with fractal dimensionality effect
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            irregularity_factor = 1.0 + 0.5 * np.sin(r * 0.3) * np.cos(r * 0.1)
            result *= irregularity_factor
            
        return result