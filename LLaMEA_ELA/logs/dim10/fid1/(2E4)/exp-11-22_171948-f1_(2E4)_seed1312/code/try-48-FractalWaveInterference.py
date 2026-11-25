import numpy as np

class FractalWaveInterference:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Base fractal-like hierarchical structure using recursive sine waves
        for i in range(self.dim):
            # Multi-scale sine wave with exponentially increasing frequency
            scale_factor = 2.0 ** (i % 3)
            freq = 2 * np.pi * scale_factor
            wave = np.sin(freq * x[i])
            result += 0.5 * wave**4
        
        # Adaptive frequency modulation based on position and dimension
        for i in range(self.dim):
            # Position-dependent frequency modulation
            mod_freq = 1.0 + 0.5 * np.sin(x[i] * 0.5)
            # Dimensional coupling effect
            coupling = 1.0 + 0.3 * np.cos(i * 0.25)
            result += 0.3 * np.sin(mod_freq * coupling * x[i])**3
        
        # Cross-dimensional wave interference with phase coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-coupled interaction between dimensions
                phase = np.sin(0.5 * (x[i] + x[j]))
                interference = np.cos(3 * (x[i] - x[j]) + phase)
                result += 0.2 * interference**2
        
        # Hierarchical fractal ridge structure with self-similar patterns
        for i in range(self.dim):
            # Fractal-like ridge with recursive pattern
            ridge = np.sin(5 * x[i]) + 0.5 * np.sin(25 * x[i]) + 0.1 * np.sin(125 * x[i])
            result += 0.4 * ridge**3
        
        # Adaptive conditioning based on solution proximity to boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += (5.0 - abs(x[i]))**2
        result += 0.1 * boundary_penalty
        
        # Multi-scale noise-like perturbations with varying intensity
        noise = 0.0
        for i in range(self.dim):
            # Different frequency components for each dimension
            noise += (np.sin(7 * x[i]) + 
                     0.4 * np.sin(31 * x[i]) + 
                     0.1 * np.sin(127 * x[i]))
        result += 0.2 * noise**2
        
        # Dimensionality scaling with logarithmic growth
        result *= (1.0 + 0.2 * np.log(self.dim + 1))
        
        # Final normalization and regularization
        result /= self.dim
        result += 0.005 * np.sum(x**6) / self.dim
        
        return result