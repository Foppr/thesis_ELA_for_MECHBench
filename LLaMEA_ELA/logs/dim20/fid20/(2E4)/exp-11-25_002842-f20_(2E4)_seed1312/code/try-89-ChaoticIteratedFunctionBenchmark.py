import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.3, 0.3, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with memory effects
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(100):  # Burn-in iterations
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with parameter variation
                r = self.r_params[i] + 0.1 * np.sin(iteration * 0.15)
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Memory-dependent modification with stronger influence
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    
            previous_values = next_values
            
        # Extract final chaotic values and apply fractal transformation
        final_values = previous_values
        
        # Fractal basin boundaries using multiple scaling factors
        fractal_terms = 0.0
        scales = [1.0, 2.0, 3.0, 5.0, 7.0]
        
        for scale in scales:
            scaled_x = x_norm * scale
            # Multi-scale fractal pattern with sine-cosine modulation
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x))
        
        # Memory-dependent dynamics with long-range correlations - improved
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with exponential decay - more aggressive
            decay_factor = np.exp(-0.2 * np.arange(1, min(15, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)))
        
        # Enhanced cross-dimensional coupling with fractal geometry
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with fractal scaling - more sensitive
                dist = np.abs(x[i] - x[j])
                cross_coupling += np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * (1 + 0.5 * np.sin(i * j))
        
        # Improved asymmetric basin boundaries using piecewise functions
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += np.sin(x[i]**3) * np.exp(-x[i]**2) * (1 + 0.1 * x[i])
            else:
                boundary_effects += np.cos(x[i]**2) * np.exp(-x[i]) * (1 + 0.1 * x[i])
        
        # Additional harmonic coupling between dimensions
        harmonic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_coupling += np.sin((x[i] - x[j])**2) * np.cos((x[i] + x[j])**2)
        
        # Final composite function with multiple chaotic components - adjusted weights
        return (0.4 * np.sum(final_values**2) + 
                0.25 * fractal_terms + 
                0.15 * memory_effects + 
                0.1 * cross_coupling + 
                0.08 * boundary_effects + 
                0.02 * harmonic_coupling)