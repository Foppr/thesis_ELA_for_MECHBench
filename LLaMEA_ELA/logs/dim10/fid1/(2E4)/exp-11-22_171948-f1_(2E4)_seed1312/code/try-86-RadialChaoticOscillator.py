import numpy as np

class RadialChaoticOscillator:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial component with multi-scale sinusoidal oscillations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.sin(10 * r) + 0.5 * np.sin(30 * r) + 0.2 * np.sin(80 * r)
        result += 2.0 * radial_term**2
        
        # Angular components with varying frequencies and coupling
        for i in range(self.dim):
            angular = 0.0
            for j in range(i+1, self.dim):
                angle_diff = x[i] - x[j]
                angular += np.sin(5 * angle_diff) * np.cos(3 * angle_diff)
            result += 0.5 * angular**2
        
        # Multi-modal harmonic landscape with adaptive scaling
        for i in range(self.dim):
            # Multiple frequency components with varying amplitudes and phase shifts
            harmonic = (np.sin(20 * x[i]) + 
                       0.7 * np.sin(60 * x[i]) + 
                       0.3 * np.sin(150 * x[i]) + 
                       0.1 * np.sin(400 * x[i]))
            result += 1.2 * harmonic**2
        
        # Adaptive conditioning based on distance from origin
        conditioning = 1.0 + 0.8 * np.exp(-0.1 * r**2)
        result *= conditioning
        
        # Cross-dimensional coupling with radial dependence
        for i in range(self.dim - 1):
            coupling = np.sin(7 * (x[i] + x[i+1])) * np.cos(4 * (x[i] - x[i+1]))
            result += 0.8 * coupling * (1.0 + 0.3 * r)
        
        # Noise-like perturbations with radial dependency
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(25 * x[i] + i * 0.3) * np.cos(15 * x[i] + i * 0.4)
        result += 0.6 * noise * (1.0 + 0.2 * r)
        
        # Add quartic regularization and dimension scaling
        result += 0.1 * np.sum(x**4)
        result *= (1.0 + 0.5 * np.log(self.dim + 1))
        
        # Normalize by dimension
        result /= self.dim
        
        return result