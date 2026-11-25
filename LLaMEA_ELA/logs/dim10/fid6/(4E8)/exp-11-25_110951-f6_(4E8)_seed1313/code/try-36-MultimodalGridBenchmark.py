import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Fractal-like basin term with adaptive scaling and chaotic components
        basin = 0.1 * np.sum(x**2) + 0.03 * np.sum(np.sin(10.0 * x) * x**2) + 0.01 * np.sum(np.cos(15.0 * x) * x**4)
        
        # Highly chaotic multimodal grid terms with non-linear frequency modulation
        grid_terms = 0
        for i in range(self.dim):
            # Complex sine-cosine combinations with varying frequencies and amplitudes
            grid_terms += np.sin(2.0 * x[i] + np.sin(0.5 * x[i])) * np.cos(1.5 * x[i] + np.cos(0.3 * x[i]))
            grid_terms += 0.4 * np.sin(3.5 * x[i] + np.sin(1.2 * x[i])) * np.cos(2.8 * x[i] + np.cos(0.7 * x[i]))
            grid_terms += 0.25 * np.sin(5.0 * x[i] + np.sin(1.8 * x[i])) * np.cos(4.2 * x[i] + np.cos(1.1 * x[i]))
            # Add fractal-like periodic structure
            grid_terms += 0.15 * np.sin(7.0 * x[i] + np.sin(2.5 * x[i])) * np.cos(6.0 * x[i] + np.cos(1.5 * x[i]))
        
        # Enhanced coupling terms with chaotic phase shifts between dimensions
        coupling = 0
        for i in range(self.dim-1):
            phase_shift = np.sin(0.3 * x[i]) * np.cos(0.4 * x[i+1])
            coupling += 0.2 * np.sin(x[i] + x[i+1] + phase_shift) * np.cos(x[i] - x[i+1] + phase_shift)
        
        # Add a novel chaotic penalty term
        chaotic_penalty = 0.03 * np.sum(np.abs(np.sin(20.0 * x)))
        
        # Saddle-point dominant term with exponential scaling
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += np.exp(-0.5 * (x[i]**2)) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Add exponential interaction between dimensions
        exp_interaction = 0
        for i in range(self.dim-1):
            exp_interaction += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(x[i] * x[i+1])
        
        # Combine all terms with different weights
        return basin + grid_terms + coupling + chaotic_penalty + 0.01 * np.sum(x**6) + 0.008 * np.sum(np.abs(x)**3) + saddle_term + exp_interaction