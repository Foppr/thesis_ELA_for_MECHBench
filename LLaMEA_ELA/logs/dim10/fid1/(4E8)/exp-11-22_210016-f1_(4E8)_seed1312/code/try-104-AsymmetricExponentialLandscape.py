import numpy as np

class AsymmetricExponentialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial component with modified exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / 6.0) * (1.0 + 0.7 * np.sin(r * 2.0) * np.cos(r * 1.2))
        
        # Enhanced sinusoidal modulations with chaotic frequency variations
        sin_term = 0.0
        for i in range(self.dim):
            freq_i = 2.0 + 0.3 * np.sin(i * 1.7)
            sin_term += (np.sin(x[i] * freq_i + i * 0.4) * np.cos(x[i] * (freq_i * 0.8) + i * 0.2) +
                        0.4 * np.sin(x[i] * (freq_i * 1.5)) * np.cos(x[i] * (freq_i * 1.3)))
        
        # Modified polynomial cross-terms with chaotic weighting
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.2 * np.sin(i * 0.7) * np.cos(j * 0.5)
                poly_term += weight * (x[i]**2 * x[j]**3 + x[i]**3 * x[j]**2) / (1.0 + np.abs(x[i] - x[j])**1.5)
        
        # Enhanced exponential interaction terms with directional bias
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-np.abs(x[i]) / 1.8) * (np.sin(x[i] * 2.1)**2 + 0.3 * np.cos(x[i] * 1.9)**2)
        
        # Modified asymmetric quartic component with chaotic scaling
        quartic_term = 0.0
        for i in range(self.dim):
            scale_factor = 0.08 + 0.02 * np.sin(i * 1.3)
            if x[i] >= 0:
                quartic_term += scale_factor * x[i]**4
            else:
                quartic_term += scale_factor * 1.5 * x[i]**4
        
        # Additional chaotic cross-dimensional coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.5) * np.cos((x[i] + x[j]) * 0.3)
        
        # Combine all terms with adjusted weights
        result = 0.9 * radial_term + 0.7 * sin_term + 0.5 * poly_term + 0.4 * exp_term + 0.3 * quartic_term + 0.15 * cross_term
        
        return result