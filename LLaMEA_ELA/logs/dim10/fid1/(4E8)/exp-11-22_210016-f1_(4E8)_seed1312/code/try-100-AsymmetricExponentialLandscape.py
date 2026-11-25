import numpy as np

class AsymmetricExponentialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Asymmetric bell-shaped radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / 8.0) * (1.0 + 0.5 * np.sin(r * 1.5) * np.cos(r * 0.8))
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(x[i] * 2.0 + i * 0.5) * np.cos(x[i] * 1.3 + i * 0.3) +
                        0.3 * np.sin(x[i] * 3.7) * np.cos(x[i] * 2.9))
        
        # Polynomial cross-terms with asymmetric weighting
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2 * x[j]**3 + x[i]**3 * x[j]**2) / (1.0 + np.abs(x[i] - x[j])**2)
        
        # Exponential interaction terms with directional bias
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-np.abs(x[i]) / 2.0) * np.sin(x[i] * 1.7)**2
        
        # Asymmetric quartic component
        quartic_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                quartic_term += 0.05 * x[i]**4
            else:
                quartic_term += 0.1 * x[i]**4
        
        # Combine all terms with different weights
        result = 0.8 * radial_term + 0.6 * sin_term + 0.4 * poly_term + 0.3 * exp_term + 0.25 * quartic_term
        
        return result