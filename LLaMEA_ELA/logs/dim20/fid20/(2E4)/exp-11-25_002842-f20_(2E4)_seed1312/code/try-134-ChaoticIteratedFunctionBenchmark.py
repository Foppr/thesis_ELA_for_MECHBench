import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with improved distribution
        self.r_params = np.random.uniform(3.6, 3.95, dim)
        self.memory_weights = np.random.uniform(-0.3, 0.3, dim)
        self.fractal_scales = np.random.uniform(0.7, 2.5, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(200):  # Increased burn-in iterations for better convergence
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with parameter variation and noise
                r = self.r_params[i] + 0.03 * np.sin(iteration * 0.12) + 0.015 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory-dependent modification with adaptive weights
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    
            previous_values = next_values
            
        # Extract final chaotic values and apply enhanced fractal transformation
        final_values = previous_values
        
        # Enhanced fractal basin boundaries using multi-scale sine-cosine patterns with improved modulation
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            # Multi-scale fractal pattern with enhanced modulation and improved scaling
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x) * 
                                  np.cos(scale * np.pi * scaled_x) * 
                                  (1 + 0.1 * np.sin(scale * x[i])))
        
        # Enhanced memory-dependent dynamics with improved long-range correlations
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved exponential decay and better weighting
            decay_factor = np.exp(-0.15 * np.arange(1, min(20, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.6) * 
                                      np.cos(final_values[i] * 0.4))
        
        # Improved cross-dimensional coupling with enhanced fractal geometry and better scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Slightly increased coupling range
                # Distance-based coupling with improved scaling and additional modulation
                dist = np.abs(x[i] - x[j])
                cross_coupling += np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * (1 + 0.2 * np.sin(i+j) * np.cos(i-j))
        
        # Enhanced asymmetric basin boundaries using improved piecewise functions
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += np.sin(x[i]**3) * np.exp(-x[i]**2) * (1 + 0.1 * np.cos(x[i]) * np.sin(x[i]))
            else:
                boundary_effects += np.cos(x[i]**2) * np.exp(-x[i]) * (1 + 0.1 * np.sin(x[i]) * np.cos(x[i]))
        
        # Enhanced composite function with better balance of components and improved weighting
        return (0.4 * np.sum(final_values**2) + 
                0.25 * fractal_terms + 
                0.18 * memory_effects + 
                0.12 * cross_coupling + 
                0.05 * boundary_effects)