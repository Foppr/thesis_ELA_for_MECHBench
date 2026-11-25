import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced complexity and randomness
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, (dim, dim))
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects and multi-scale dynamics
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        # Extended burn-in period for better convergence
        for iteration in range(300):
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with time-varying parameters and enhanced noise
                r = self.r_params[i] + 0.05 * np.sin(iteration * 0.15) + 0.02 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory-dependent modification with adaptive weights and feedback loops
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    
                    # Add cross-dimensional memory effects
                    for j in range(self.dim):
                        if i != j:
                            next_values[i] += self.coupling_strengths[i, j] * previous_values[j] * np.sin(iteration * 0.05)
            
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
                                  (1 + 0.15 * np.sin(scale * x[i]) * np.cos(scale * x[i])))
        
        # Enhanced memory-dependent dynamics with improved long-range correlations and multi-scale feedback
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved exponential decay and better weighting
            decay_factor = np.exp(-0.2 * np.arange(1, min(30, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.6) * 
                                      np.cos(final_values[i] * 0.4) * 
                                      np.exp(-0.1 * i))
        
        # Improved cross-dimensional coupling with enhanced fractal geometry and better scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range
                # Distance-based coupling with improved scaling and additional modulation
                dist = np.abs(x[i] - x[j])
                cross_coupling += (self.coupling_strengths[i, j] * 
                                 np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * 
                                 (1 + 0.25 * np.sin(i+j) * np.cos(i-j)) * 
                                 np.sin(0.5 * np.pi * dist) * np.cos(0.5 * np.pi * dist))
        
        # Enhanced asymmetric basin boundaries using improved piecewise functions with fractal characteristics
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.15 * np.cos(x[i]) * np.sin(x[i])) * 
                                   np.sin(0.3 * np.pi * x[i]))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.15 * np.sin(x[i]) * np.cos(x[i])) * 
                                   np.cos(0.3 * np.pi * x[i]))
        
        # Enhanced composite function with better balance of components and improved weighting
        return (0.35 * np.sum(final_values**2) + 
                0.28 * fractal_terms + 
                0.20 * memory_effects + 
                0.15 * cross_coupling + 
                0.02 * boundary_effects)