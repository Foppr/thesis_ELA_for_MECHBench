import numpy as np

class MultimodalChaoticRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Sinusoidal oscillations with chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * self.chaotic_sequence[i]
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Polynomial chaos with dynamic exponents
        f3 = 0.0
        for i in range(self.dim):
            exp = 2.0 + 1.5 * np.sin(self.chaotic_sequence[i])
            f3 += (x[i]**exp) * np.sin(x[i])
        
        # Radial basis function component with chaotic centers
        f4 = 0.0
        for i in range(self.dim):
            center = 2.0 * self.chaotic_sequence[i]
            f4 -= np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.5 * np.abs(center)))**2)
        
        # Cross-dimensional coupling with sine modulation
        f5 = 0.0
        for i in range(self.dim - 1):
            f5 += np.sin(x[i] * x[i+1]) * (1.0 + 0.3 * np.cos(x[i] + x[i+1]))
        
        # Multifractal-like structure with multiple scales
        f6 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(2.0 * x[i])
            f6 += np.sin(scale * x[i]) * np.cos(3.0 * x[i])
        
        # Adaptive harmonic oscillation
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.abs(x[i]) / 5.0
            f7 += np.sin(freq * x[i]) * np.cos(2.0 * x[i])
        
        # Fractional polynomial with chaotic scaling
        f8 = 0.0
        for i in range(self.dim):
            alpha = 1.5 + 0.5 * self.chaotic_sequence[i]
            f8 += (np.abs(x[i])**alpha) * np.sin(x[i])
        
        # Sigmoidal radial component
        f9 = 0.0
        for i in range(self.dim):
            f9 -= 1.0 / (1.0 + np.exp(-x[i])) * np.cos(x[i])
        
        # Hyperbolic tangent oscillation
        f10 = 0.0
        for i in range(self.dim):
            f10 += np.tanh(x[i]) * np.sin(2.0 * x[i])
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Final function value with refined weights
        return scale_factor * (f1 + 0.5 * f2 + 0.3 * f3 + 0.4 * f4 + 0.2 * f5 + 0.6 * f6 + 0.3 * f7 + 0.4 * f8 + 0.3 * f9 + 0.2 * f10)