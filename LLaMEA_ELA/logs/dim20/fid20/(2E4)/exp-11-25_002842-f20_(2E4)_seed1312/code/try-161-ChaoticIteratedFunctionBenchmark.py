import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with wider distribution for higher complexity
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Add new parameters for enhanced nonlinearity
        self.nonlinear_coeffs = np.random.uniform(0.1, 2.0, dim)
        # Modified coupling strengths for increased complexity
        self.coupling_strengths = np.random.uniform(1.0, 3.5, dim)
        # Additional complexity parameters
        self.hyperchaos_params = np.random.uniform(0.1, 1.0, dim)
        self.modulation_indices = np.random.uniform(1.0, 5.0, dim)
        # New parameters for improved fitness and challenge
        self.resonance_freqs = np.random.uniform(0.1, 2.0, dim)
        self.stochastic_amplitudes = np.random.uniform(0.05, 0.5, dim)
        self.dimensional_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects and noise
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(300):  # Increased burn-in iterations for better convergence
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with parameter variation, noise, and nonlinear modulation
                r = self.r_params[i] + 0.05 * np.sin(iteration * 0.15) + 0.02 * np.random.randn()
                # Add nonlinear coefficient influence
                chaotic_val = r * previous_values[i] * (1 - previous_values[i])
                next_values[i] = chaotic_val * self.nonlinear_coeffs[i]
                
                # Enhanced memory-dependent modification with adaptive weights and feedback loops
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    # Add recursive memory effect
                    next_values[i] += 0.1 * np.sin(previous_values[i]) * np.cos(iteration * 0.05)
                    
            previous_values = next_values
            
        # Extract final chaotic values and apply enhanced fractal transformation
        final_values = previous_values
        
        # Enhanced fractal basin boundaries using multi-scale sine-cosine patterns with improved modulation
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            # Multi-scale fractal pattern with enhanced modulation, improved scaling, and additional nonlinear terms
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x) * 
                                  np.cos(scale * np.pi * scaled_x) * 
                                  (1 + 0.2 * np.sin(scale * x[i]) * np.cos(scale * x[i])) * 
                                  np.tanh(scaled_x))
        
        # Enhanced memory-dependent dynamics with improved long-range correlations and additional feedback
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved exponential decay, better weighting, and nonlinear feedback
            decay_factor = np.exp(-0.2 * np.arange(1, min(25, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.6) * 
                                      np.cos(final_values[i] * 0.4) * 
                                      np.tanh(final_values[i]))
        
        # Improved cross-dimensional coupling with enhanced fractal geometry, better scaling, and additional nonlinear interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range for more complexity
                # Distance-based coupling with improved scaling, additional modulation, and nonlinear interaction
                dist = np.abs(x[i] - x[j])
                cross_coupling += (np.sin(dist) * np.cos(dist) * 
                                 np.exp(-dist**2) * 
                                 (1 + 0.3 * np.sin(i+j) * np.cos(i-j)) *
                                 np.tanh(dist) * 
                                 self.coupling_strengths[i] * self.coupling_strengths[j])
        
        # Enhanced asymmetric basin boundaries using improved piecewise functions with additional nonlinear terms
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.15 * np.cos(x[i]) * np.sin(x[i])) *
                                   np.tanh(x[i]))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.15 * np.sin(x[i]) * np.cos(x[i])) *
                                   np.tanh(x[i]))
        
        # Hyperchaotic enhancement with additional modulation and multi-scale coupling
        hyperchaos_terms = 0.0
        for i in range(self.dim):
            hyperchaos_terms += (self.hyperchaos_params[i] * 
                               np.sin(final_values[i] * self.modulation_indices[i]) * 
                               np.cos(final_values[i] * self.modulation_indices[i]) * 
                               np.exp(-np.abs(final_values[i])) * 
                               np.tanh(final_values[i]))
        
        # New enhanced components for better fitness and challenge
        resonance_terms = 0.0
        for i in range(self.dim):
            resonance_terms += self.stochastic_amplitudes[i] * np.sin(self.resonance_freqs[i] * x[i]) * np.cos(self.resonance_freqs[i] * x[i])
            
        dimensional_scaling = 0.0
        for i in range(self.dim):
            dimensional_scaling += self.dimensional_weights[i] * np.log(1 + np.abs(x[i])) * np.sin(x[i])
        
        # Enhanced composite function with better balance of components and improved weighting
        return (0.35 * np.sum(final_values**2) + 
                0.28 * fractal_terms + 
                0.20 * memory_effects + 
                0.15 * cross_coupling + 
                0.02 * boundary_effects +
                0.03 * hyperchaos_terms +
                0.03 * resonance_terms +
                0.02 * dimensional_scaling)