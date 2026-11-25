import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with stronger randomness and multi-scale distribution
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Add additional chaotic dynamics parameters
        self.coupling_strengths = np.random.uniform(0.1, 2.0, dim)
        self.noise_amplitudes = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects and multi-scale dynamics
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        # Increased iterations and enhanced chaotic behavior
        for iteration in range(300):  # Further increased burn-in iterations
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Enhanced logistic map with parameter modulation, noise, and coupling
                r = self.r_params[i] + 0.05 * np.sin(iteration * 0.15) + self.noise_amplitudes[i] * np.random.randn()
                
                # Multi-scale chaotic evolution with enhanced coupling
                chaotic_component = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory effect with multi-exponential decay
                memory_contribution = 0.0
                for j in range(min(10, iteration)):
                    weight = np.exp(-0.2 * j) * self.memory_weights[i]
                    memory_contribution += weight * previous_values[i] if iteration > 0 else 0.0
                
                next_values[i] = chaotic_component + memory_contribution
                
                # Add cross-dimensional coupling with fractal scaling
                coupling_term = 0.0
                for j in range(max(0, i-3), min(self.dim, i+4)):
                    if i != j:
                        coupling_strength = self.coupling_strengths[i] * np.exp(-0.1 * abs(i-j))
                        coupling_term += coupling_strength * np.sin(previous_values[j]) * np.cos(previous_values[i])
                
                next_values[i] += coupling_term
                
            previous_values = next_values
            
        # Extract final chaotic values and apply enhanced fractal transformation
        final_values = previous_values
        
        # Multi-scale fractal basin boundaries with enhanced modulation and improved scaling
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            
            # Complex fractal pattern with multiple trigonometric components and exponential decay
            term1 = np.sin(scaled_x) * np.cos(scaled_x) * np.exp(-np.abs(scaled_x))
            term2 = np.sin(scale * np.pi * scaled_x) * np.cos(scale * np.pi * scaled_x)
            term3 = (1 + 0.2 * np.sin(scale * x[i]) * np.cos(scale * x[i]))
            
            fractal_terms += np.sum(term1 * term2 * term3)
        
        # Enhanced memory-dependent dynamics with long-range correlations and improved weighting
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with exponential decay and better multi-scale correlation
            decay_factor = np.exp(-0.2 * np.arange(1, min(30, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.7) * 
                                      np.cos(final_values[i] * 0.5))
        
        # Improved cross-dimensional coupling with enhanced fractal geometry, better scaling and multi-scale modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Further increased coupling range
                dist = np.abs(x[i] - x[j])
                
                # Enhanced distance-based coupling with multi-scale modulation and improved scaling
                coupling_factor = np.sin(dist) * np.cos(dist) * np.exp(-dist**2)
                modulation = (1 + 0.3 * np.sin(i+j) * np.cos(i-j)) * (1 + 0.15 * np.sin(i*j))
                
                cross_coupling += coupling_factor * modulation
        
        # Enhanced asymmetric basin boundaries using piecewise functions with multi-scale fractal modulation
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.2 * np.cos(x[i]) * np.sin(x[i])) * 
                                   (1 + 0.1 * np.sin(x[i]**2)))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.2 * np.sin(x[i]) * np.cos(x[i])) * 
                                   (1 + 0.1 * np.cos(x[i]**3)))
        
        # Enhanced composite function with better balance of components and improved weighting
        return (0.5 * np.sum(final_values**2) + 
                0.2 * fractal_terms + 
                0.15 * memory_effects + 
                0.15 * cross_coupling + 
                0.05 * boundary_effects)