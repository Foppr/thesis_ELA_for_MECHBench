import numpy as np

class RadialChaoticOscillator:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced radial component with multi-scale sinusoidal oscillations
        r = np.sqrt(np.sum(x**2))
        radial_term = np.sin(15 * r) + 0.6 * np.sin(40 * r) + 0.3 * np.sin(100 * r) + 0.1 * np.sin(200 * r)
        result += 3.0 * radial_term**2
        
        # Enhanced angular components with stronger coupling
        for i in range(self.dim):
            angular = 0.0
            for j in range(i+1, self.dim):
                angle_diff = x[i] - x[j]
                angular += np.sin(8 * angle_diff) * np.cos(5 * angle_diff) + 0.5 * np.sin(12 * angle_diff)
            result += 0.7 * angular**2
        
        # Enhanced multi-modal harmonic landscape with more frequency components
        for i in range(self.dim):
            # Multiple frequency components with varying amplitudes and phase shifts
            harmonic = (np.sin(25 * x[i]) + 
                       0.8 * np.sin(70 * x[i]) + 
                       0.4 * np.sin(180 * x[i]) + 
                       0.2 * np.sin(500 * x[i]) +
                       0.1 * np.sin(800 * x[i]))
            result += 1.5 * harmonic**2
        
        # Stronger adaptive conditioning based on distance from origin
        conditioning = 1.0 + 1.2 * np.exp(-0.15 * r**2)
        result *= conditioning
        
        # Enhanced cross-dimensional coupling with stronger radial dependence
        for i in range(self.dim - 1):
            coupling = np.sin(10 * (x[i] + x[i+1])) * np.cos(6 * (x[i] - x[i+1]))
            result += 1.2 * coupling * (1.0 + 0.5 * r)
        
        # Enhanced noise-like perturbations with stronger radial dependency
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(30 * x[i] + i * 0.4) * np.cos(20 * x[i] + i * 0.5) + 0.3 * np.sin(50 * x[i] + i * 0.6)
        result += 1.0 * noise * (1.0 + 0.4 * r)
        
        # Increased quartic regularization and stronger dimension scaling
        result += 0.2 * np.sum(x**4)
        result *= (1.0 + 0.8 * np.log(self.dim + 1))
        
        # Normalize by dimension
        result /= self.dim
        
        return result