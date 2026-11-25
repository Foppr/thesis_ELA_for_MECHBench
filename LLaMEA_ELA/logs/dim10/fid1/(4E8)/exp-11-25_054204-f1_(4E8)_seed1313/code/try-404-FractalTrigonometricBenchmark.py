import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like sequence for dynamic scaling
        self.fractal_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f1 = np.sum(x**4)
        
        # Trigonometric coupling with fractal modulation
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * self.fractal_sequence[i]
            f2 += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial fractal interaction with dynamic scaling
        radial = np.sum(x**2)
        f3 = 0.7 * np.sin(np.sqrt(radial) * 4.0) * np.cos(np.sqrt(radial) * 3.0)
        
        # Cross-dimensional coupling with polynomial weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = (i + 1) / (self.dim + 1)
            cross_interaction += weight * np.sin(x[i] + x[i+1])
        f4 = 0.6 * cross_interaction
        
        # Polynomial chaos with fractal-like behavior
        f5 = 0.5 * np.sum((x**3) * np.sin(2.0 * x))
        
        # Sigmoidal scaling with trigonometric modulation
        f6 = 0.4 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 2.5 + 2.0 * np.sin(np.sum(x**2) / 15.0)
        f7 = 0.5 * np.sum(np.sin(freq * x) * np.cos(4.0 * x))
        
        # Nonlinear correlation with exponential weighting
        f8 = 0.4 * np.sum(np.exp(-x**2) * x**2)
        
        # Additional higher-order terms for increased complexity
        f9 = 0.3 * np.sum(x**5 * np.cos(x/2))
        f10 = 0.35 * np.sum(np.abs(x)**3.5)
        
        # Fractal-like coupling with cubic interaction
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2])
        f11 = 0.4 * fractal_coupling
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1)
        
        # Additional multimodal component for enhanced conditioning
        f12 = 0.3 * np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * np.exp(-x**2 / 7.0))
        
        # Modified fractal coupling with quartic interaction
        f13 = 0.3 * np.sum(np.sin(x**4) * np.cos(x**3))
        
        # New term: ninth-order polynomial with modified frequency
        f14 = 0.25 * np.sum((x**9) * np.cos(2.0 * x))
        
        # Mutated cross-dimensional coupling with inverse weighting
        cross_interaction_inv = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + i * 0.8)
            cross_interaction_inv += weight * np.cos(x[i] * x[i+1])
        f15 = 0.35 * cross_interaction_inv
        
        # Additional chaotic harmonic with modified exponent
        f16 = 0.3 * np.sum(np.sin(x**1.7) * np.cos(3.0 * x))
        
        # Intensified chaotic coupling term
        f17 = 0.4 * np.sum(np.sin(x**2) * np.cos(x**3) * np.exp(-x**2 / 10.0))
        
        # Enhanced radial basis function modulation
        f18 = 0.35 * np.sum(np.exp(-np.sqrt(radial)) * np.sin(radial))
        
        # Cross-dimensional fractal coupling with higher-order terms
        f19 = 0.25 * np.sum(np.sin(x**2 + x**3) * np.cos(x**4))
        
        # Final combined function with refined weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19)