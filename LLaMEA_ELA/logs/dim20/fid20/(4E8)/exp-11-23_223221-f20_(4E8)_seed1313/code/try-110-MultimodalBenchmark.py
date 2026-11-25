import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar Gaussian peak components with fractal scaling
        peak_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.5)
            peak_term += scale * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(i * 0.3)) / (0.5 + 0.2 * np.cos(i * 0.4)))**2)
        
        # Harmonic interference patterns with varying frequencies
        harm_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.8)
            harm_term += np.sin(freq * x[i]) * np.cos(2.0 * freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive ridge structures with dimension-dependent steepness
        ridge_term = 0.0
        for i in range(self.dim):
            steepness = 2.0 + 1.5 * np.sin(i * 0.6)
            ridge_term += (x[i] * np.cos(steepness * x[i]))**2 / (1.0 + 0.1 * np.abs(x[i]))
        
        # Multi-scale sinusoidal modulations with exponentially decaying amplitudes
        mod_term = 0.0
        for i in range(self.dim):
            amp = 0.5 * np.exp(-0.1 * i)
            freq = 3.0 + 2.0 * np.sin(i * 0.7)
            mod_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Logarithmic basin boundary interactions
        basin_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                basin_term += (np.log(dist + 1.0) / (dist + 1.0)) * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
        
        # Combined function with global scaling and regularization
        result = peak_term + harm_term + ridge_term + mod_term + basin_term
        
        # Add small regularization term for better conditioning
        result += 0.01 * np.sum(x**4)
        
        return result