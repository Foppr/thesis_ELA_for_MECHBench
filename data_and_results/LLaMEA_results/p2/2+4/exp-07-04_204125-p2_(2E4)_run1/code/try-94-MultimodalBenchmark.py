import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for performance
        self.constants = {
            'quadratic_coeff': 0.5,
            'sin_freq': 2.0,
            ' coupling_strength': 0.3,
            'noise_amplitude': 0.1,
            'conditioning_factor': 1.0 + 0.05 * dim
        }
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quadratic basin terms with varying conditioning
        for i in range(self.dim):
            # Base quadratic term with conditioning
            result += self.constants['quadratic_coeff'] * (x[i] - 1.0)**2 * (1.0 + 0.1 * i)
            
            # Sinusoidal modulation with varying frequency
            result += np.sin(self.constants['sin_freq'] * x[i]) * np.cos(0.5 * x[i])
            
            # Cross-dimensional coupling with exponential decay
            if i < self.dim - 1:
                coupling = self.constants['coupling_strength'] * np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * (x[i] + x[i+1])**2
                result += coupling
        
        # Add a set of non-smooth, piecewise linear perturbations
        for i in range(self.dim):
            result += np.abs(x[i]) * np.sin(10.0 * x[i]) + 0.05 * np.abs(x[i])**1.5
        
        # Add a fractal-like component with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += 0.2 * fractal_term
        
        # Add noise-like irregularities
        noise = np.sum(np.sin(50.0 * x) * np.cos(25.0 * x))
        result += self.constants['noise_amplitude'] * noise
        
        # Apply dimensionality scaling factor
        dim_scaling = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= dim_scaling
        
        return result