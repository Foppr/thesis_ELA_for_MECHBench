import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like oscillatory terms with increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            # Use varying frequencies and amplitudes for more complex patterns
            freq1 = 2.0 + 0.3 * np.sin(i * 0.5)
            freq2 = 1.5 + 0.4 * np.cos(i * 0.3)
            # Combine multiple oscillatory components with different weights
            fractal_term += (0.4 * np.sin(freq1 * x[i]) * 
                            np.cos(freq2 * x[i]) * 
                            np.exp(-0.15 * np.abs(x[i])) + 
                            0.2 * np.sin(3 * freq1 * x[i]) * 
                            np.cos(2 * freq2 * x[i]) +
                            0.1 * np.sin(5 * x[i]) * np.exp(-0.05 * x[i]**2))
        
        # Modified adaptive ridge structure with non-linear scaling
        ridge_term = 0.0
        for i in range(self.dim):
            # Apply a more complex ridge function with sigmoidal and polynomial components
            ridge_height = 0.6 * (1 + np.tanh(x[i] / (0.8 + i * 0.15))) * (1 - np.exp(-0.5 * x[i]**2))
            ridge_term += ridge_height * np.exp(-0.3 * x[i]**2)
        
        # Enhanced cross-dimensional interaction with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                # Use a more sophisticated distance-based scaling with exponential decay
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                scale_factor = 1.0 / (1.0 + dist**3) * np.exp(-0.1 * dist)
                cross_term += scale_factor * np.sin(2.5 * x[i]) * np.cos(3.5 * x[j])
        
        # Improved global modulation with polynomial and trigonometric components
        global_mod = 0.0
        for i in range(self.dim):
            # Apply a more complex combination of polynomial and sinusoidal scaling
            global_mod += 0.3 * (x[i]**4) * np.exp(-0.1 * np.abs(x[i])) * np.sin(0.6 * x[i]) + \
                         0.15 * x[i] * np.cos(0.8 * x[i])
        
        # Add a small constant to ensure non-zero fitness for all inputs
        return fractal_term + ridge_term + cross_term + global_mod + 0.01 * np.sum(x**2)