import numpy as np

class RadialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for stability
        self.constants = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            # Radial term with variable scaling
            r_squared = np.sum((x - x[i])**2) if self.dim > 1 else x[i]**2
            result += self.constants[i] * np.exp(-0.5 * r_squared / (1.0 + 0.1 * np.abs(x[i])))
        
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling with varying frequency and amplitude
                freq = 2.0 + 0.5 * np.sin(i * 0.7)
                amp = 1.0 + 0.3 * np.cos(j * 0.9)
                result += amp * np.sin(freq * (x[i] + x[j])) * \
                         np.cos(0.5 * (x[i] - x[j])) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive polynomial terms with dimension-dependent exponents
        for i in range(self.dim):
            # Higher-order polynomial with adaptive coefficients
            result += 0.3 * (x[i]**6) * np.sin(x[i]) + \
                     0.2 * (x[i]**4) * np.cos(x[i]) + \
                     0.15 * x[i]**3 * np.tan(0.5 * x[i])
        
        # Add a global shaping term with sigmoidal behavior
        result += 0.5 * np.sum(np.tanh(x)) + \
                 0.2 * np.sum(np.log(1.0 + np.exp(x)))
        
        # Add a noise component for robustness testing
        result += 0.02 * np.random.standard_normal()
        
        return result