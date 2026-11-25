import numpy as np

class AsymmetricExponentialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced asymmetric bell-shaped radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / 6.0) * (1.0 + 0.3 * np.sin(r * 2.0) * np.cos(r * 1.2)) * (1.0 + 0.1 * np.tanh(r))
        
        # Sinusoidal modulations with chaotic frequency variations
        sin_term = 0.0
        for i in range(self.dim):
            freq_i = 2.0 + 0.5 * np.sin(i * 0.7)
            sin_term += (np.sin(x[i] * freq_i + i * 0.4) * np.cos(x[i] * (freq_i * 1.3) + i * 0.2) +
                        0.2 * np.sin(x[i] * (freq_i * 3.0)) * np.cos(x[i] * (freq_i * 2.5)))
        
        # Modified polynomial cross-terms with adaptive weighting
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.1 * np.abs(x[i] - x[j])**3)
                poly_term += (x[i]**2 * x[j]**4 + x[i]**4 * x[j]**2) * weight
        
        # Refined exponential interaction terms with directional bias and chaotic scaling
        exp_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.2 * np.sin(i * 0.6)
            exp_term += np.exp(-np.abs(x[i]) / (1.5 * scale)) * np.sin(x[i] * 2.0)**3
        
        # Enhanced asymmetric quartic component with chaotic bias
        quartic_term = 0.0
        for i in range(self.dim):
            bias = 0.1 * np.sin(i * 0.8)
            if x[i] >= 0:
                quartic_term += (0.03 + bias) * x[i]**4
            else:
                quartic_term += (0.08 - bias) * x[i]**4
        
        # Additional chaotic harmonic term for increased complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(x[i] * 4.0 + i * 0.3) * np.cos(x[i] * 3.5 + i * 0.2) * np.tanh(x[i])
        
        # Combine all terms with optimized weights
        result = 0.7 * radial_term + 0.5 * sin_term + 0.3 * poly_term + 0.25 * exp_term + 0.2 * quartic_term + 0.15 * harmonic_term
        
        return result