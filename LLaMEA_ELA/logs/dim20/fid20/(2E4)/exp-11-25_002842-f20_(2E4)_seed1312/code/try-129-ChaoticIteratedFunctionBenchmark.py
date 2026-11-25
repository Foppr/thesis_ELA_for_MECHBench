import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with extreme variability and fractal distribution
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 2.0, dim)
        self.nonlinear_exponents = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range with enhanced boundary effects
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with extreme memory effects and multi-scale dynamics
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(300):  # Increased burn-in iterations
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Enhanced logistic map with time-varying parameters and multi-frequency noise
                r = self.r_params[i] + 0.05 * np.sin(iteration * 0.15) + 0.02 * np.sin(iteration * 0.3) + 0.01 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Multi-scale memory effects with fractional decay and complex weighting
                if iteration > 0:
                    memory_contribution = self.memory_weights[i] * previous_values[i]
                    # Add fractal memory modulation
                    fractal_mod = np.sin(iteration * 0.05) * np.cos(iteration * 0.03)
                    next_values[i] += memory_contribution * (1 + 0.2 * fractal_mod)
                    
                # Add nonlinear transformation based on dimension index
                next_values[i] = np.sign(next_values[i]) * np.abs(next_values[i])**self.nonlinear_exponents[i]
                
            previous_values = next_values
            
        # Extract final chaotic values and apply multi-fractal transformation
        final_values = previous_values
        
        # Multi-scale fractal basin boundaries with enhanced geometric complexity
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            
            # Complex multi-fractal pattern with multiple harmonic components and adaptive modulation
            term1 = np.sin(scaled_x) * np.cos(scaled_x) * np.exp(-np.abs(scaled_x))
            term2 = np.sin(scale * np.pi * scaled_x) * np.cos(scale * np.pi * scaled_x)
            term3 = (1 + 0.15 * np.sin(scale * x[i]) * np.cos(scale * x[i]))
            term4 = np.sin(np.sqrt(np.abs(x[i]))) * np.cos(np.log(np.abs(x[i]) + 1))
            
            fractal_terms += np.sum(term1 * term2 * term3 * term4)
        
        # Enhanced memory-dependent dynamics with long-range correlations and fractional Brownian motion
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved fractional decay and complex weighting
            decay_factor = np.exp(-0.2 * np.arange(1, min(30, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.6) * 
                                      np.cos(final_values[i] * 0.4) *
                                      np.exp(-np.abs(final_values[i])))
        
        # Novel cross-dimensional coupling with quantum-inspired interference patterns
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended coupling range
                # Quantum-like interference coupling with phase modulation and amplitude scaling
                dist = np.abs(x[i] - x[j])
                phase = np.sin(dist * np.pi / 2) * np.cos(dist * np.pi / 3)
                amplitude = (1 + 0.3 * np.sin(i+j) * np.cos(i-j)) * self.coupling_strengths[i]
                cross_coupling += amplitude * np.sin(dist) * np.cos(dist) * phase * np.exp(-dist**2)
        
        # Highly complex asymmetric basin boundaries with fractal boundary conditions
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.15 * np.cos(x[i]) * np.sin(x[i])) *
                                   np.sin(np.log(np.abs(x[i]) + 1)))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.15 * np.sin(x[i]) * np.cos(x[i])) *
                                   np.cos(np.sqrt(np.abs(x[i]))))
        
        # Extremely complex composite function with highly modified weighting scheme
        return (0.35 * np.sum(final_values**2) + 
                0.28 * fractal_terms + 
                0.15 * memory_effects + 
                0.14 * cross_coupling + 
                0.08 * boundary_effects)