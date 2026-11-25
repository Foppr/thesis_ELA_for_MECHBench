import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Enhanced fractal-like basin term with nested chaotic structures and adaptive scaling
        basin = 0.1 * np.sum(x**2) + 0.03 * np.sum(np.sin(10.0 * x) * x**2) + 0.01 * np.sum(np.cos(15.0 * x) * x**4)
        
        # Nested fractal grid terms with recursive chaotic modulation
        grid_terms = 0
        for i in range(self.dim):
            # Primary chaotic interaction
            grid_terms += np.sin(2.0 * x[i] + np.sin(0.5 * x[i])) * np.cos(1.5 * x[i] + np.cos(0.3 * x[i]))
            
            # Nested fractal structure with higher-order chaos
            grid_terms += 0.4 * np.sin(3.5 * x[i] + np.sin(1.2 * x[i]) + np.sin(0.7 * x[i]**2)) * \
                         np.cos(2.8 * x[i] + np.cos(0.7 * x[i]) + np.cos(0.4 * x[i]**2))
            
            # Recursive fractal pattern with diminishing amplitude
            grid_terms += 0.25 * np.sin(5.0 * x[i] + np.sin(1.8 * x[i]) + np.sin(0.9 * x[i]**3)) * \
                         np.cos(4.2 * x[i] + np.cos(1.1 * x[i]) + np.cos(0.6 * x[i]**3))
            
            # Ultra-high frequency fractal component
            grid_terms += 0.15 * np.sin(7.0 * x[i] + np.sin(2.5 * x[i]) + np.sin(1.3 * x[i]**4)) * \
                         np.cos(6.0 * x[i] + np.cos(1.5 * x[i]) + np.cos(0.8 * x[i]**4))
            
            # Ultra-chaotic modulation with exponential growth
            grid_terms += 0.08 * np.sin(12.0 * x[i] + np.sin(3.0 * x[i]) + np.sin(1.5 * x[i]**5)) * \
                         np.cos(10.0 * x[i] + np.cos(2.0 * x[i]) + np.cos(1.2 * x[i]**5))
        
        # Enhanced coupling terms with nested phase shifts and cross-dimension fractals
        coupling = 0
        for i in range(self.dim-1):
            # Multi-level phase shift structure
            phase_shift = np.sin(0.3 * x[i]) * np.cos(0.4 * x[i+1]) + \
                         np.sin(0.2 * x[i]**2) * np.cos(0.1 * x[i+1]**2)
            
            coupling += 0.2 * np.sin(x[i] + x[i+1] + phase_shift) * np.cos(x[i] - x[i+1] + phase_shift)
            
            # Cross-dimensional fractal interaction
            coupling += 0.1 * np.sin(0.5 * x[i] * x[i+1] + np.sin(0.3 * x[i]**2)) * \
                       np.cos(0.3 * x[i] + 0.7 * x[i+1] + np.cos(0.2 * x[i+1]**2))
            
            # Nested higher-order coupling
            coupling += 0.05 * np.sin(0.8 * x[i] * x[i+1] * np.sin(0.4 * x[i])) * \
                       np.cos(0.6 * x[i] + 0.9 * x[i+1] * np.cos(0.3 * x[i+1]))
        
        # Novel chaotic penalty term with fractal scaling and adaptive threshold
        chaotic_penalty = 0.04 * np.sum(np.abs(np.sin(20.0 * x) + 0.5 * np.sin(40.0 * x)))
        
        # Enhanced higher-order polynomial terms with nested chaos
        high_order = 0.01 * np.sum(x**6) + 0.008 * np.sum(np.abs(x)**3) + 0.005 * np.sum(np.sin(5.0 * x))
        
        # Add nested adaptive scaling factor with fractal-like behavior
        adaptive_scaling = 0.02 * np.sum((1.0 + 0.1 * np.abs(x) + 0.05 * np.abs(x)**2) * x**2)
        
        # Add fractal basin complexity term
        fractal_basin = 0.03 * np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * x**2)
        
        # Combine all terms with different weights for improved fitness score
        return basin + grid_terms + coupling + chaotic_penalty + high_order + adaptive_scaling + fractal_basin