import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with wider ranges for increased complexity
        self.r_params = np.random.uniform(3.8, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Add new parameters for enhanced complexity
        self.coupling_strengths = np.random.uniform(0.1, 0.8, dim)
        self.frequency_modulators = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory effects and noise
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(200):  # Increased burn-in iterations
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Enhanced logistic map with frequency modulation and adaptive parameters
                r = self.r_params[i] + 0.1 * np.sin(iteration * self.frequency_modulators[i]) + 0.03 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory-dependent modification with multi-scale weights
                if iteration > 0:
                    # Multi-scale memory influence with exponential decay
                    memory_influence = 0.0
                    for j in range(1, min(5, iteration)):
                        weight = np.exp(-j * 0.2) * self.memory_weights[i]
                        memory_influence += weight * previous_values[i] * np.sin(j * 0.5)
                    next_values[i] += memory_influence
                    
            previous_values = next_values
            
        # Extract final chaotic values and apply enhanced fractal transformation
        final_values = previous_values
        
        # Enhanced fractal basin boundaries with multi-scale sine-cosine patterns and additional harmonics
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            # Multi-scale fractal pattern with enhanced modulation and harmonic components
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x) * 
                                  np.cos(scale * np.pi * scaled_x) *
                                  (1 + 0.15 * np.sin(2 * scaled_x) * np.cos(3 * scaled_x)))
        
        # Enhanced memory-dependent dynamics with improved long-range correlations and feedback loops
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with improved exponential decay and feedback terms
            decay_factor = np.exp(-0.15 * np.arange(1, min(20, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.5) *
                                      (1 + 0.1 * np.cos(final_values[i])))
        
        # Enhanced cross-dimensional coupling with improved fractal geometry and non-linear interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                # Distance-based coupling with improved scaling and additional nonlinear terms
                dist = np.abs(x[i] - x[j])
                coupling_term = np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * (1 + 0.15 * np.sin(i+j))
                # Add non-linear interaction terms
                cross_coupling += coupling_term * (1 + 0.08 * np.sin(x[i] * x[j]))
        
        # Improved asymmetric basin boundaries using enhanced piecewise functions with polynomial components
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += np.sin(x[i]**3) * np.exp(-x[i]**2) * (1 + 0.08 * np.cos(x[i]) + 0.05 * x[i]**2)
            else:
                boundary_effects += np.cos(x[i]**2) * np.exp(-x[i]) * (1 + 0.08 * np.sin(x[i]) + 0.05 * x[i]**3)
        
        # Additional harmonic and resonance components for increased landscape complexity
        harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_terms += np.sum(np.sin(x[i] * (i+1) * 2) * np.cos(x[i] * (i+1) * 3) * 
                                   np.exp(-0.5 * x[i]**2) * self.coupling_strengths[i])
        
        # Enhanced composite function with better balance of components and additional complexity
        return (0.25 * np.sum(final_values**2) + 
                0.4 * fractal_terms + 
                0.15 * memory_effects + 
                0.15 * cross_coupling + 
                0.03 * boundary_effects +
                0.02 * harmonic_terms)