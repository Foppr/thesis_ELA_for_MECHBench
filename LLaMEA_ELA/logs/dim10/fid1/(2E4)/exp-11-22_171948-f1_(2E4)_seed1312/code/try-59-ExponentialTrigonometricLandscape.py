import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay components with trigonometric modulation
        for i in range(self.dim):
            exp_term = np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i])
            result += exp_term**2
        
        # Trigonometric interference with radial symmetry
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.cos(5 * x[i])
        radial_component = np.exp(-0.1 * radial_sum**2)
        
        # Cross-dimensional coupling with adaptive strength
        coupling_strength = 1.0 + 0.5 * np.sin(np.sum(x**2) / self.dim)
        for i in range(self.dim - 1):
            coupling = coupling_strength * np.sin(3 * (x[i] - x[i+1])) * np.cos(2 * (x[i] + x[i+1]))
            result += 0.8 * coupling
        
        # Radial symmetry with multi-scale harmonics
        r_squared = np.sum(x**2)
        radial_harmonic = np.sin(20 * np.sqrt(r_squared)) + 0.5 * np.sin(40 * np.sqrt(r_squared))
        result += 0.6 * radial_harmonic**2
        
        # Adaptive conditioning based on position and dimensionality
        condition_factor = 1.0 + 0.3 * np.tanh(np.sum(x**2) / self.dim)
        result *= condition_factor
        
        # Multi-modal structure with enhanced peak complexity
        for i in range(self.dim):
            peak_component = np.sin(15 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.2 * x[i]**2)
            result += 0.4 * peak_component**2
        
        # Noise-like perturbations with chaotic phase coupling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(30 * x[i] + i * 0.1) * np.cos(15 * x[i] + i * 0.2)
        result += 0.3 * noise
        
        # Add dimensionality scaling with logarithmic growth
        result *= (1.0 + 0.2 * np.log(self.dim + 1))
        
        # Final regularization with quartic terms
        result += 0.02 * np.sum(x**4) / self.dim
        
        return result