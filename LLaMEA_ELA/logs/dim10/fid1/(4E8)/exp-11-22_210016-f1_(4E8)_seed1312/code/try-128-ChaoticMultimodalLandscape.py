import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-scale radial component with nested harmonic modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / 10.0) * (1.0 + 0.3 * np.sin(r * 2.5) * np.cos(r * 1.2)) * (1.0 + 0.2 * np.tanh(r * 0.6))
        
        # Fractal-like sinusoidal modulations with chaotic frequency variations and scale adaptation
        sin_term = 0.0
        for i in range(self.dim):
            freq_i = 2.5 + 0.6 * np.sin(i * 0.7) * np.cos(i * 0.3)
            scale_i = 1.0 + 0.25 * np.sin(i * 0.5)
            sin_term += (np.sin(x[i] * freq_i * scale_i + i * 0.4) * np.cos(x[i] * (freq_i * 1.3) * scale_i + i * 0.2) +
                        0.25 * np.sin(x[i] * (freq_i * 3.5) * scale_i) * np.cos(x[i] * (freq_i * 2.8) * scale_i))
        
        # Adaptive polynomial cross-terms with fractal-weighting and dimensionally scaled interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.15 * np.abs(x[i] - x[j])**3)
                poly_term += (x[i]**2 * x[j]**6 + x[i]**6 * x[j]**2) * weight * (1.0 + 0.12 * np.sin(i * j * 0.4))
        
        # Fractal exponential interaction terms with multi-level scaling and directional bias
        exp_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.25 * np.sin(i * 0.7) * np.cos(i * 0.5)
            exp_term += np.exp(-np.abs(x[i]) / (2.5 * scale)) * np.sin(x[i] * 2.5)**3 * np.cos(x[i] * 1.2)**3
        
        # Multi-scale quartic component with fractal bias and chaotic modulation
        quartic_term = 0.0
        for i in range(self.dim):
            bias = 0.12 * np.sin(i * 1.0) * np.cos(i * 0.6)
            if x[i] >= 0:
                quartic_term += (0.03 + bias) * x[i]**4
            else:
                quartic_term += (0.10 - bias) * x[i]**4
        
        # Nested harmonic term with fractal-like complexity and multi-dimensional coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(x[i] * 4.5 + i * 0.3) * np.cos(x[i] * 3.8 + i * 0.25) * np.tanh(x[i] * 0.4)
        
        # Additional chaotic interference term for increased complexity and non-linearity
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited range coupling
                interference_term += np.sin(x[i] * x[j] * 1.8 + i * j * 0.15) * np.cos(x[i] + x[j]) * (1.0 + 0.12 * np.sin(i + j))
        
        # Combine all terms with optimized weights for maximum challenge
        result = 0.7 * radial_term + 0.5 * sin_term + 0.35 * poly_term + 0.3 * exp_term + 0.28 * quartic_term + 0.18 * harmonic_term + 0.12 * interference_term
        
        return result