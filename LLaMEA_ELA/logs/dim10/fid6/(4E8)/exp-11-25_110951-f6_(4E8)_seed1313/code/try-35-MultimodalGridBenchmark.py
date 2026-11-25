import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Enhanced fractal-like basin term with adaptive scaling and chaotic components
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
        
        # Add a novel chaotic penalty term with enhanced nonlinearity
        chaotic_penalty = 0.03 * np.sum(np.abs(np.sin(20.0 * x))**1.5)
        
        # Add improved higher-order polynomial terms for better conditioning
        high_order = 0.01 * np.sum(x**6) + 0.008 * np.sum(np.abs(x)**3) + 0.005 * np.sum(np.sin(25.0 * x))
        
        # Add a new adaptive scaling term that varies with dimensionality
        adaptive_scaling = 0.02 * np.sum((x**2) * np.cos(5.0 * x))
        
        # Combine all terms with optimized weights
        return basin + grid_terms + coupling + chaotic_penalty + high_order + adaptive_scaling + 0.003 * np.sum(np.exp(-x**2))