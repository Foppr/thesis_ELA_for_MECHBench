import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component
        logistic_component = 0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Logistic map with adaptive parameter
            logistic_val = x[i]
            for _ in range(5):  # Iterate to reach chaotic regime
                logistic_val = r * logistic_val * (1 - logistic_val)
            logistic_component += np.sin(logistic_val * np.pi) * np.exp(-0.1 * x[i]**2)
        
        # Spherical harmonic interaction terms
        sph_harm_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance between dimensions
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                # Spherical harmonic with degree and order
                sph_harm = np.sin(3 * np.arctan2(x[j], x[i])) * np.cos(2 * dist)
                sph_harm_component += sph_harm * np.exp(-0.5 * (dist / 2.0)**2)
        
        # Adaptive elliptic valley component
        elliptic_component = 0
        for i in range(self.dim):
            # Elliptic valley with adaptive axis ratio
            axis_ratio = 1.0 + 0.5 * np.sin(0.3 * x[i])
            elliptic_component += (x[i]**2) / (axis_ratio**2) + 0.1 * np.cos(2 * x[i])
        
        # Cross-dimensional coupling with Gaussian kernel
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Kernel-based coupling with dynamic bandwidth
                bandwidth = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                kernel_val = np.exp(-0.5 * ((x[i] - x[j])**2) / (bandwidth**2))
                coupling_component += kernel_val * (x[i]**2 + x[j]**2)
        
        # Fractal-like power law with dynamic exponent
        fractal_component = 0
        for i in range(self.dim):
            # Dynamic exponent based on neighboring values
            exp_val = 1.5 + 0.5 * np.sin(0.2 * x[i])
            fractal_component += np.abs(x[i])**exp_val
        
        # Global scaling and mixing
        scale_factor = 1.0 + 0.3 * np.cos(0.4 * self.dim)
        
        return scale_factor * (0.25 * logistic_component + 
                              0.3 * sph_harm_component + 
                              0.2 * elliptic_component + 
                              0.15 * coupling_component + 
                              0.1 * fractal_component)