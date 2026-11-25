import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced randomness
        self.r_params = np.random.uniform(3.6, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Additional chaotic parameters for enhanced complexity
        self.coupling_strengths = np.random.uniform(0.1, 0.8, dim)
        self.noise_amplitudes = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with enhanced memory and noise
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(200):  # Increased iterations for better chaos
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Enhanced logistic map with time-varying parameters and noise
                r = self.r_params[i] + 0.1 * np.sin(iteration * 0.2) + self.noise_amplitudes[i] * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory effects with nonlinear decay
                if iteration > 0:
                    memory_contribution = self.memory_weights[i] * previous_values[i] * np.exp(-0.05 * iteration)
                    next_values[i] += memory_contribution
                    
            previous_values = next_values
            
        # Extract final chaotic values
        final_values = previous_values
        
        # Multi-scale fractal transformation with enhanced sine-cosine patterns
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            
            # Enhanced fractal pattern with additional trigonometric components
            fractal_terms += np.sum(np.sin(scaled_x) * np.cos(scaled_x) * 
                                  np.exp(-np.abs(scaled_x)) * 
                                  np.sin(scale * np.pi * scaled_x) * 
                                  np.cos(scale * np.pi * scaled_x) * 
                                  np.tan(0.5 * scaled_x))
        
        # Enhanced memory-dependent dynamics with long-range correlations
        memory_effects = 0.0
        for i in range(self.dim):
            # Improved exponential decay with adaptive coefficients
            decay_factor = np.exp(-0.15 * np.arange(1, min(20, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.5) * 
                                      np.exp(-0.02 * i))
        
        # Enhanced cross-dimensional coupling with non-linear scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                # Non-linear coupling with improved scaling and additional terms
                coupling = np.sin(dist) * np.cos(dist) * np.exp(-dist**2) * (1 + 0.2 * np.sin(i+j)) * \
                          np.log(1 + dist) * np.tan(0.1 * dist)
                cross_coupling += coupling
        
        # Novel asymmetric basin boundaries with enhanced piecewise functions
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += (np.sin(x[i]**3) * np.exp(-x[i]**2) * 
                                   (1 + 0.1 * np.cos(x[i])) * np.log(1 - x[i]))
            else:
                boundary_effects += (np.cos(x[i]**2) * np.exp(-x[i]) * 
                                   (1 + 0.1 * np.sin(x[i])) * np.log(1 + x[i]))
        
        # Additional nonlinear terms for enhanced complexity
        nonlinear_terms = 0.0
        for i in range(self.dim):
            nonlinear_terms += np.sin(final_values[i] * np.pi) * np.cos(final_values[i] * np.pi/2) * \
                             np.exp(-0.5 * (x[i]**2))
        
        # Enhanced composite function with improved balance and new components
        return (0.3 * np.sum(final_values**2) + 
                0.25 * fractal_terms + 
                0.18 * memory_effects + 
                0.17 * cross_coupling + 
                0.08 * boundary_effects + 
                0.02 * nonlinear_terms)