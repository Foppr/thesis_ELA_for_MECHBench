import numpy as np

class RadialChaoticOscillator:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced radial component with modified sinusoidal oscillations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.sin(12 * r) + 0.6 * np.sin(40 * r) + 0.3 * np.sin(100 * r)
        result += 1.8 * radial_term**2
        
        # Improved angular components with stronger coupling
        for i in range(self.dim):
            angular = 0.0
            for j in range(i+1, self.dim):
                angle_diff = x[i] - x[j]
                angular += np.sin(6 * angle_diff) * np.cos(4 * angle_diff)
            result += 0.7 * angular**2
        
        # Enhanced multi-modal harmonic landscape with modified amplitudes
        for i in range(self.dim):
            # Multiple frequency components with varying amplitudes and phase shifts
            harmonic = (np.sin(25 * x[i]) + 
                       0.8 * np.sin(70 * x[i]) + 
                       0.4 * np.sin(180 * x[i]) + 
                       0.2 * np.sin(500 * x[i]))
            result += 1.0 * harmonic**2
        
        # Improved adaptive conditioning based on distance from origin
        conditioning = 1.0 + 0.9 * np.exp(-0.15 * r**2)
        result *= conditioning
        
        # Enhanced cross-dimensional coupling with radial dependence
        for i in range(self.dim - 1):
            coupling = np.sin(8 * (x[i] + x[i+1])) * np.cos(5 * (x[i] - x[i+1]))
            result += 0.9 * coupling * (1.0 + 0.4 * r)
        
        # Enhanced noise-like perturbations with radial dependency
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(30 * x[i] + i * 0.35) * np.cos(20 * x[i] + i * 0.45)
        result += 0.7 * noise * (1.0 + 0.25 * r)
        
        # Modified quartic regularization and dimension scaling
        result += 0.12 * np.sum(x**4)
        result *= (1.0 + 0.6 * np.log(self.dim + 1))
        
        # Normalize by dimension
        result /= self.dim
        
        return result