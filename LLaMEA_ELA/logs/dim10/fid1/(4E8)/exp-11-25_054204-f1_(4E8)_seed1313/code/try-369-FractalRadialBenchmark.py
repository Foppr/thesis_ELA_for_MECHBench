import numpy as np

class FractalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = np.power(0.5, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Fractal Brownian motion component with varying Hurst parameter
        f2 = 0.0
        for i in range(self.dim):
            hurst = 0.3 + 0.4 * np.sin(i * 0.7)  # Dynamic Hurst parameter
            f2 += self.fractal_factors[i] * np.sin((i + 1) * x[i]) * np.cos((i + 1) * x[i])
        
        # Radial basis function with adaptive width
        f3 = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.cos(i * 0.8)
            f3 += np.exp(-0.5 * (x[i]**2) / (width**2)) * np.sin(x[i])
        
        # Sine-cosine coupling with dynamic frequency modulation
        f4 = 0.0
        for i in range(self.dim - 1):
            freq = 1.0 + 2.0 * np.sin(i * 0.5)  # Dynamic frequency
            f4 += np.sin(freq * x[i]) * np.cos(freq * x[i+1])
        
        # Multifractal interaction with polynomial scaling
        f5 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.9)
            f5 += (x[i]**3) * np.cos(scale * x[i]) * np.sin(x[i])
        
        # Adaptive chaotic modulation with logistic map
        f6 = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.2 * np.cos(i * 0.6)
            logistic_val = r * np.abs(x[i]) * (1 - np.abs(x[i]))
            f6 += logistic_val * np.sin(2.5 * x[i])
        
        # Cross-dimensional coupling with exponential weighting
        cross_term = 0.0
        for i in range(self.dim - 2):
            weight = np.exp(-i / (self.dim + 2))
            cross_term += weight * np.sin(x[i] * x[i+1] * x[i+2])
        f7 = 0.5 * cross_term
        
        # Polynomial chaos with fractal-like behavior
        f8 = 0.0
        for i in range(self.dim):
            poly_exp = 3.0 + 0.5 * np.sin(i * 0.4)
            f8 += (x[i]**poly_exp) * np.cos(x[i])
        
        # Radial harmonic component with dynamic modulation
        radial_harmonic = np.sum(x**2)
        f9 = 0.3 * np.sin(2.0 * np.sqrt(radial_harmonic)) * np.cos(1.5 * radial_harmonic)
        
        # Sigmoidal scaling with fractal influence
        f10 = 0.0
        for i in range(self.dim):
            sig = 1.0 / (1.0 + np.exp(-x[i]))
            f10 += sig * np.cos(x[i] * 0.5)
        
        # Multimodal sine-cosine coupling with dynamic phase
        f11 = 0.0
        for i in range(self.dim):
            phase = 0.5 + 0.3 * np.sin(i * 0.8)
            f11 += np.sin(x[i] + phase) * np.cos(2.0 * x[i] + phase)
        
        # Modified fractal coupling with cubic interaction
        f12 = 0.0
        for i in range(self.dim - 2):
            f12 += np.sin(x[i]**3) * np.cos(x[i+1]**3) * np.sin(x[i+2]**3)
        
        # Dynamic exponential weighting with fractal scaling
        f13 = 0.0
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim + 1))
            f13 += weight * np.cos(x[i]**2) * np.sin(x[i])
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1)
        
        # Final function with refined weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13)