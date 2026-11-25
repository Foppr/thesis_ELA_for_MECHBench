import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Enhanced fractal-like basin term with adaptive scaling and chaotic components
        basin = 0.1 * np.sum(x**2) + 0.03 * np.sum(np.sin(10.0 * x) * x**2) + 0.01 * np.sum(np.cos(15.0 * x) * x**4)
        
        # Highly chaotic multimodal grid terms with non-linear frequency modulation and improved coupling
        grid_terms = 0
        for i in range(self.dim):
            # Complex sine-cosine combinations with varying frequencies and amplitudes
            grid_terms += np.sin(2.0 * x[i] + np.sin(0.5 * x[i])) * np.cos(1.5 * x[i] + np.cos(0.3 * x[i]))
            grid_terms += 0.4 * np.sin(3.5 * x[i] + np.sin(1.2 * x[i])) * np.cos(2.8 * x[i] + np.cos(0.7 * x[i]))
            grid_terms += 0.25 * np.sin(5.0 * x[i] + np.sin(1.8 * x[i])) * np.cos(4.2 * x[i] + np.cos(1.1 * x[i]))
            # Add fractal-like periodic structure with enhanced complexity
            grid_terms += 0.15 * np.sin(7.0 * x[i] + np.sin(2.5 * x[i])) * np.cos(6.0 * x[i] + np.cos(1.5 * x[i]))
            # Add chaotic modulation to increase difficulty
            grid_terms += 0.08 * np.sin(12.0 * x[i] + np.sin(3.0 * x[i])) * np.cos(10.0 * x[i] + np.cos(2.0 * x[i]))
        
        # Enhanced coupling terms with chaotic phase shifts between dimensions
        coupling = 0
        for i in range(self.dim-1):
            phase_shift = np.sin(0.3 * x[i]) * np.cos(0.4 * x[i+1])
            coupling += 0.2 * np.sin(x[i] + x[i+1] + phase_shift) * np.cos(x[i] - x[i+1] + phase_shift)
            # Add additional cross-dimensional interaction
            coupling += 0.1 * np.sin(0.5 * x[i] * x[i+1]) * np.cos(0.3 * x[i] + 0.7 * x[i+1])
        
        # Add a novel chaotic penalty term with improved scaling
        chaotic_penalty = 0.04 * np.sum(np.abs(np.sin(20.0 * x)))
        
        # Add enhanced higher-order polynomial terms for better conditioning
        high_order = 0.01 * np.sum(x**6) + 0.008 * np.sum(np.abs(x)**3) + 0.005 * np.sum(np.sin(5.0 * x))
        
        # Add adaptive scaling factor to improve conditioning across dimensions
        adaptive_scaling = 0.02 * np.sum((1.0 + 0.1 * np.abs(x)) * x**2)
        
        # Combine all terms with different weights for improved fitness score
        return basin + grid_terms + coupling + chaotic_penalty + high_order + adaptive_scaling