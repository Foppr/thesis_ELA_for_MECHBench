import numpy as np

class NestedParabolicValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested parabolic valleys with varying depths and widths
        valley_term = 0.0
        for i in range(self.dim):
            # Create nested parabolic structures with dynamic scaling
            scale = 1.0 + 0.5 * np.sin(0.2 * i)
            depth = 0.8 + 0.3 * np.cos(0.15 * i)
            width = 1.2 + 0.4 * np.sin(0.25 * i)
            
            # Nested parabolic valley component
            valley_term += depth * (x[i] - scale * np.sin(0.5 * x[i]))**2 / width
            
        # Saddle point structure with cross-dimensional interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced cross-dimensional saddle interaction
                saddle_term += 0.5 * (x[i]**2 - x[j]**2) * np.sin(0.4 * (x[i] + x[j]))
                
        # Dynamic gradient modulation with periodic forcing
        grad_mod = 0.0
        for i in range(self.dim):
            # Periodic modulation of gradient magnitude
            mod_factor = 1.0 + 0.5 * np.sin(0.8 * x[i] + 0.4 * i)
            grad_mod += mod_factor * x[i]**3
            
        # Multi-scale oscillatory component for fine structure exploration
        osc_term = 0.0
        frequencies = [2.0, 4.0, 6.0, 8.0]
        for i, freq in enumerate(frequencies):
            if i < self.dim:
                osc_term += np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim])
                
        # Asymmetric basin structure to challenge symmetry-breaking algorithms
        basin_term = 0.0
        for i in range(self.dim):
            # Asymmetric parabolic basins with modified coefficients
            asym_factor = 1.0 + 0.4 * np.sin(0.5 * i)
            basin_term += asym_factor * (x[i] - 0.5)**2 + 0.3 * x[i]**4
            
        # Add dimension-dependent scaling factor for conditioning
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 1) + 0.07 * np.sum(np.abs(x))
        
        # Combine all components with appropriate weights
        return scale_factor * (0.7 * valley_term + 0.4 * saddle_term + 
                              0.25 * grad_mod + 0.18 * osc_term + 0.3 * basin_term)