import numpy as np

class AsymmetricExponentialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-scale radial component with nested harmonic modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / 8.0) * (1.0 + 0.4 * np.sin(r * 3.0) * np.cos(r * 1.5)) * (1.0 + 0.15 * np.tanh(r * 0.5))
        
        # Fractal-like sinusoidal modulations with chaotic frequency variations and scale adaptation
        sin_term = 0.0
        for i in range(self.dim):
            freq_i = 3.0 + 0.8 * np.sin(i * 0.9) * np.cos(i * 0.4)
            scale_i = 1.0 + 0.3 * np.sin(i * 0.7)
            sin_term += (np.sin(x[i] * freq_i * scale_i + i * 0.5) * np.cos(x[i] * (freq_i * 1.4) * scale_i + i * 0.3) +
                        0.3 * np.sin(x[i] * (freq_i * 4.0) * scale_i) * np.cos(x[i] * (freq_i * 3.2) * scale_i))
        
        # Adaptive polynomial cross-terms with fractal-weighting and dimensionally scaled interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.2 * np.abs(x[i] - x[j])**4)
                poly_term += (x[i]**3 * x[j]**5 + x[i]**5 * x[j]**3) * weight * (1.0 + 0.1 * np.sin(i * j * 0.3))
        
        # Fractal exponential interaction terms with multi-level scaling and directional bias
        exp_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.8) * np.cos(i * 0.6)
            exp_term += np.exp(-np.abs(x[i]) / (2.0 * scale)) * np.sin(x[i] * 3.0)**4 * np.cos(x[i] * 1.5)**2
        
        # Multi-scale quartic component with fractal bias and chaotic modulation
        quartic_term = 0.0
        for i in range(self.dim):
            bias = 0.15 * np.sin(i * 1.2) * np.cos(i * 0.8)
            if x[i] >= 0:
                quartic_term += (0.04 + bias) * x[i]**4
            else:
                quartic_term += (0.12 - bias) * x[i]**4
        
        # Nested harmonic term with fractal-like complexity and multi-dimensional coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(x[i] * 5.0 + i * 0.4) * np.cos(x[i] * 4.2 + i * 0.3) * np.tanh(x[i] * 0.5)
        
        # Additional chaotic interference term for increased complexity and non-linearity
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                interference_term += np.sin(x[i] * x[j] * 2.0 + i * j * 0.2) * np.cos(x[i] + x[j]) * (1.0 + 0.1 * np.sin(i + j))
        
        # Combine all terms with optimized weights for maximum challenge
        result = 0.8 * radial_term + 0.6 * sin_term + 0.4 * poly_term + 0.35 * exp_term + 0.25 * quartic_term + 0.2 * harmonic_term + 0.1 * interference_term
        
        return result