import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic frequencies for dynamic modulation
        self.frequencies = 2.0 + 3.0 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with Gaussian kernels
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2) * np.cos(2.0 * x[i])
        
        # Trigonometric coupling with dynamic frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            trig_coupling += np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Cross-dimensional interaction with radial scaling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Chaotic modulation with logistic map
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(np.pi * np.log(1.0 + np.abs(x[i])) * np.cos(3.0 * x[i]))
        
        # Polynomial chaos with exponential weighting
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**3) * np.sin(2.5 * x[i]) * np.exp(-i / (self.dim + 1))
        
        # Sine-cosine harmonic interaction with variable amplitude
        harmonic = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            harmonic += amp * np.sin(x[i]) * np.cos(2.0 * x[i])
        
        # Fractal-like coupling with recursive interaction
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(0.5 * (x[i] + x[i+1] + x[i+2]))
        
        # Adaptive scaling based on dimensionality
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined function with refined weights
        return scale * (0.8 * rbf + 0.7 * trig_coupling + 0.6 * cross_interaction + 
                       0.5 * chaotic_mod + 0.4 * poly_chaos + 0.3 * harmonic + 
                       0.2 * fractal_coupling)