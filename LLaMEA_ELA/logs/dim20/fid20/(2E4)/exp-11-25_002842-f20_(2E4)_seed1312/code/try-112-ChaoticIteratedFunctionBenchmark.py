import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced variability
        self.r_params = np.random.uniform(3.8, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Add additional chaotic parameters for enhanced complexity
        self.coupling_strengths = np.random.uniform(0.1, 0.8, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects and multiple attractors
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        attractor_states = []
        
        for iteration in range(200):  # Increased iterations for better attractor exploration
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Enhanced logistic map with parameter modulation and multi-frequency noise
                r = self.r_params[i] + 0.1 * np.sin(iteration * 0.2) + 0.08 * np.cos(iteration * 0.15) + 0.03 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory-dependent modification with multiple time delays
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    if iteration > 5:
                        next_values[i] += 0.3 * self.memory_weights[i] * attractor_states[-5][i]
                    
            previous_values = next_values
            if iteration >= 150:  # Store attractor states for memory effects
                attractor_states.append(next_values.copy())
                
        # Extract final chaotic values and apply enhanced fractal transformation
        final_values = previous_values
        
        # Enhanced fractal basin boundaries using multi-scale sine-cosine patterns with phase shifts
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale + self.phase_shifts[i]
            # Multi-scale fractal pattern with enhanced modulation and complex geometry
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x) * 
                                  np.cos(scale * np.pi * scaled_x) *
                                  np.tanh(scaled_x) * 
                                  np.log(1 + np.abs(scaled_x)))
        
        # Enhanced memory-dependent dynamics with improved long-range correlations and multiple time scales
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved exponential decay and multiple time scales
            decay_factor = np.exp(-0.1 * np.arange(1, min(20, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.5) *
                                      np.exp(-0.05 * i))
        
        # Enhanced cross-dimensional coupling with improved fractal geometry and non-linear interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                # Distance-based coupling with improved scaling and phase modulation
                dist = np.abs(x[i] - x[j])
                phase = np.sin((i + j) * 0.5)
                cross_coupling += (np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * 
                                 (1 + 0.15 * np.sin(i+j)) * 
                                 np.tanh(dist) * 
                                 phase * 
                                 self.coupling_strengths[i])
        
        # Enhanced asymmetric basin boundaries using improved piecewise functions with fractal characteristics
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.08 * np.cos(x[i])) *
                                   np.tanh(x[i]) *
                                   np.log(1 + np.abs(x[i])))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.08 * np.sin(x[i])) *
                                   np.tanh(x[i]) *
                                   np.log(1 + x[i]))
        
        # Enhanced composite function with better balance of components and additional complexity
        return (0.25 * np.sum(final_values**2) + 
                0.30 * fractal_terms + 
                0.15 * memory_effects + 
                0.20 * cross_coupling + 
                0.10 * boundary_effects)