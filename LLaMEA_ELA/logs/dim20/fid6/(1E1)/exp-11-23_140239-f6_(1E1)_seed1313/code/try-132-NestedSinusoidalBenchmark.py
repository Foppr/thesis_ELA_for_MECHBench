import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = 0.1 * np.sum(x**2)
        
        # Add nested sinusoidal terms with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 20)):
            # Radial component with adaptive scaling
            r = np.sqrt(np.sum(x**2))
            
            # Nested oscillations with increasing frequency
            freq = i * 3.0
            amp = 10.0 / (i + 1.0)
            
            # Add radial sinusoidal modulation
            result += amp * np.sin(freq * r) * np.cos(freq * np.sum(x[:min(i, self.dim)]))
            
            # Add angular component for multidirectional complexity
            if i < self.dim:
                angle = np.arctan2(x[i-1], x[i]) if i > 0 else 0.0
                result += amp * np.sin(freq * angle) * np.cos(freq * r)
        
        # Add adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.5 * np.sin(self.dim * 0.7)
        
        # Add cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(5.0 * (x[i] + x[j]))
        
        # Add multi-scale harmonic terms
        harmonic = 0.0
        for scale in [1, 2, 3, 5]:
            harmonic += np.sum(np.sin(scale * x) * np.cos(scale * x * 0.5))
        
        # Add fractal-like self-similarity through recursive application
        fractal = 0.0
        for i in range(1, min(4, self.dim + 1)):
            fractal += np.sum(np.sin(2**i * x) * np.cos(3**i * x))
        
        return (result * cond_factor + coupling + harmonic + fractal)