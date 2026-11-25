import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Fractal-like basin term with chaotic scaling and multiple polynomial components
        basin = 0.1 * np.sum(x**2) + 0.03 * np.sum(x**4) + 0.01 * np.sum(np.abs(x)**3.5)
        
        # Highly chaotic multimodal grid terms with irrational frequency ratios and dynamic amplitudes
        grid_terms = 0
        for i in range(self.dim):
            # Irrational frequency interactions to create chaotic landscape
            grid_terms += np.sin(np.pi * np.sqrt(2) * x[i]) * np.cos(np.e * x[i])
            grid_terms += 0.4 * np.sin(np.sqrt(3) * x[i]) * np.cos(np.pi * x[i])
            grid_terms += 0.25 * np.sin(np.sqrt(5) * x[i]) * np.cos(np.sqrt(7) * x[i])
            # Add fractal-like periodic structure with varying amplitudes
            grid_terms += 0.15 * np.sin(2.718 * x[i]) * np.cos(3.141 * x[i])
        
        # Complex coupling terms with exponential interaction weights and cross-dimensional dependencies
        coupling = 0
        for i in range(self.dim-1):
            coupling += 0.2 * np.sin(x[i] * x[i+1]) * np.cos(np.exp(x[i]) + x[i+1])
            coupling += 0.1 * np.sin(np.sin(x[i]) * x[i+1]) * np.cos(x[i] * np.cos(x[i+1]))
        
        # Add a novel chaotic penalty term based on the product of all dimensions
        chaotic_penalty = 0.05 * np.prod(np.sin(x) + 0.1 * np.cos(2 * x))
        
        # Combine all terms with different weights and add noise-like perturbation
        return basin + grid_terms + coupling + chaotic_penalty + 0.01 * np.sum(np.abs(x)) + 0.003 * np.sum(x**6)