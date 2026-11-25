import numpy as np

class MultimodalFBM:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension
        self.hurst_params = np.array([0.3 + 0.4 * np.sin(i * 0.5) for i in range(dim)])
        self.scale_factors = np.array([1.0 + 0.5 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial basis function component with varying scales
        for i in range(self.dim):
            # Multiple RBF centers with dynamic positioning
            center = 2.0 * np.sin(i * 0.8) + 1.5 * np.cos(i * 0.4)
            sigma = 0.5 + 0.3 * np.sin(i * 0.6)
            rbf_value = np.exp(-0.5 * ((x[i] - center) / sigma)**2)
            result += rbf_value * self.scale_factors[i]
            
        # Add fractional Brownian motion component with dimension-specific Hurst parameters
        for i in range(self.dim):
            # Simple FBM approximation using multiple sine waves with varying frequencies and amplitudes
            fbm_term = 0.0
            for k in range(1, 6):
                freq = k * (i + 1) * 0.2
                amp = self.hurst_params[i] / (k**2)
                fbm_term += amp * np.sin(freq * x[i])
            result += fbm_term
            
        # Add cross-dimensional interaction terms with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                coupling_strength = 0.1 * (1 + np.sin(i * 0.5) * np.cos(j * 0.3))
                interaction = coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                result += interaction
                
        # Add global scaling with periodic modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        periodic_factor = 1.0 + 0.2 * np.sin(0.2 * dist_from_origin) * np.cos(0.5 * dist_from_origin)
        result *= periodic_factor
        
        # Add noise component with dimension-specific characteristics
        noise = 0.02 * np.sum(np.sin(x * 3) * np.cos(x * 0.7))
        result += noise
        
        return result