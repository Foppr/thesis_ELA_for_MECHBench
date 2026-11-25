import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive conditioning
        poly_term = np.sum(0.1 * x**4 + 0.5 * x**3 + 2.0 * x**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            amp = 1.0 + 0.3 * np.cos(i)
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential decay with dynamic coupling
        exp_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.abs(x[i] - x[j])
                exp_term += np.exp(-0.5 * dist) * np.sin(3 * (x[i] + x[j]))
        
        # Adaptive basin structure with dynamic scaling
        basin_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.2 * np.sin(0.7 * i)
            basin_term += scale * (np.abs(x[i]) - 3.0)**2 * np.exp(-0.1 * x[i]**2)
        
        # Mixed harmonic and fractal components
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Dynamic conditioning based on position
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(x[i] / 2.0)
            cond_term += cond_factor * x[i]**2
        
        # Combine all terms with different weights
        result = 0.3 * poly_term + 0.4 * trig_term + 0.2 * exp_term + 0.1 * basin_term + 0.15 * mixed_term + 0.05 * cond_term
        
        return result