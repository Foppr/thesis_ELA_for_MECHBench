import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = max(1, min(5, dim // 4))
        self.sine_params = np.random.uniform(0.5, 2.0, (self.fractal_depth, dim))
        self.harmonic_coeffs = np.random.uniform(-1.0, 1.0, (self.fractal_depth, dim))
        self.scale_factors = np.logspace(0, 2, self.fractal_depth)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        for depth in range(self.fractal_depth):
            scale = self.scale_factors[depth]
            sine_params = self.sine_params[depth]
            harmonic_coeffs = self.harmonic_coeffs[depth]
            
            # Chaotic sine map component
            chaotic_term = np.sum(np.sin(sine_params * x) * np.exp(-0.1 * (x**2)))
            
            # Multi-scale harmonic potential
            harmonic_potential = np.sum(harmonic_coeffs * np.cos(scale * x) * np.exp(-0.05 * (x**2)))
            
            # Combine with scaling factor
            result += scale * (chaotic_term + harmonic_potential)
        
        # Add cross-dimensional coupling with fractal structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i] - x[j])) * np.cos(0.3 * (x[i] + x[j]))
                result += 0.1 * coupling * np.exp(-0.02 * (i-j)**2)
        
        # Add a global polynomial term to ensure proper conditioning
        result += 0.5 * np.sum(x**4) + 0.3 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        return result