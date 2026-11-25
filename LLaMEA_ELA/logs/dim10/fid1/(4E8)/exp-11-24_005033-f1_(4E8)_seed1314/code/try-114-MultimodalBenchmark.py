import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with higher degree terms and adaptive conditioning
        poly_term = np.sum(0.2 * x**6 + 0.4 * x**5 + 1.5 * x**4 + 2.0 * x**3 + 3.0 * x**2)
        
        # Chaotic trigonometric components with fractal-like frequency modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.5 * i + np.sin(i))
            amp = 1.5 + 0.8 * np.cos(0.3 * i + np.cos(i))
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential decay with long-range coupling and cross-dimensional interactions
        exp_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                dist = np.abs(x[i] - x[j])
                exp_term += np.exp(-0.3 * dist) * np.sin(5 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
        
        # Enhanced basin structure with multi-scale adaptive scaling and chaotic modulation
        basin_term = 0.0
        for i in range(self.dim):
            scale = 1.5 + 0.5 * np.sin(0.8 * i + np.sin(0.3 * i))
            basin_term += scale * (np.abs(x[i]) - 2.5)**3 * np.exp(-0.2 * x[i]**2)
        
        # Fractal-inspired mixed components with recursive harmonic interactions
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += np.sin(7 * x[i]) * np.cos(9 * x[i]) * np.sin(4 * x[i]) * np.cos(6 * x[i])
            
        # Dynamic conditioning with time-varying parameters and chaotic modulation
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = 1.2 + 0.8 * np.sin(x[i] / 3.0 + np.sin(x[i] / 2.0))
            cond_term += cond_factor * x[i]**4
        
        # Additional chaotic coupling terms between groups of dimensions
        chaos_term = 0.0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                group_sum = x[i] + x[i+1] + x[i+2]
                chaos_term += np.sin(4 * group_sum) * np.cos(3 * group_sum) * np.exp(-0.1 * group_sum**2)
        
        # Combine all terms with optimized weights for maximum multimodality
        result = 0.25 * poly_term + 0.35 * trig_term + 0.2 * exp_term + 0.1 * basin_term + 0.1 * mixed_term + 0.05 * cond_term + 0.05 * chaos_term
        
        return result