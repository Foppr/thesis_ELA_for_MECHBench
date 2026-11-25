import numpy as np

class ChaoticIteratedFunctionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with quantum-inspired distributions
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        # Add quantum phase parameters for enhanced complexity
        self.phase_params = np.random.uniform(0, 2*np.pi, dim)
        # Adaptive coupling weights with exponential decay
        self.coupling_weights = np.random.exponential(0.5, dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range for logistic maps
        x_norm = (x + 5.0) / 10.0
        
        # Chaotic iterated function system with quantum phase modulation
        chaotic_sum = 0.0
        previous_values = np.zeros(self.dim)
        
        for iteration in range(300):  # Increased burn-in iterations
            next_values = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with quantum phase modulation and noise
                r = self.r_params[i] + 0.05 * np.sin(iteration * 0.15 + self.phase_params[i])
                r += 0.02 * np.random.randn()
                next_values[i] = r * previous_values[i] * (1 - previous_values[i])
                
                # Enhanced memory-dependent modification with quantum interference
                if iteration > 0:
                    next_values[i] += self.memory_weights[i] * previous_values[i]
                    # Add quantum-like interference terms
                    next_values[i] += 0.03 * np.sin(previous_values[i] * (iteration + i)) * np.cos(previous_values[i] * (iteration - i))
                    
            previous_values = next_values
            
        # Extract final chaotic values and apply nested fractal transformation
        final_values = previous_values
        
        # Nested fractal basin boundaries with quantum-inspired patterns
        fractal_terms = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[i]
            scaled_x = x_norm * scale
            # Nested fractal pattern with quantum interference and improved scaling
            base_term = np.sin(scaled_x) * np.cos(scaled_x) * np.exp(-np.abs(scaled_x))
            quantum_mod = np.sin(scale * np.pi * scaled_x + self.phase_params[i]) * np.cos(scale * np.pi * scaled_x + self.phase_params[i])
            fractal_terms += base_term * quantum_mod * (1 + 0.2 * np.sin(scale * x[i] + self.phase_params[i]))
        
        # Quantum-enhanced memory-dependent dynamics
        memory_effects = 0.0
        for i in range(self.dim):
            # Incorporate past values with quantum-like exponential decay and interference
            decay_factor = np.exp(-0.2 * np.arange(1, min(25, self.dim)))
            if len(decay_factor) > 0:
                memory_effects += np.sum(decay_factor * 
                                      np.sin(final_values[i] * (i + 1)) * 
                                      np.cos(final_values[i] * (i + 2)) * 
                                      np.sin(final_values[i] * 0.6 + self.phase_params[i]) * 
                                      np.cos(final_values[i] * 0.4 + self.phase_params[i]))
        
        # Adaptive cross-dimensional coupling with quantum interference
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range
                # Distance-based coupling with quantum phase modulation and additional interference
                dist = np.abs(x[i] - x[j])
                coupling_term = np.sin(dist) * np.cos(dist) * np.exp(-dist**2)
                phase_mod = np.sin(i + j + self.phase_params[i] + self.phase_params[j]) * np.cos(i - j + self.phase_params[i] - self.phase_params[j])
                cross_coupling += coupling_term * phase_mod * (1 + 0.3 * np.sin(i+j) * np.cos(i-j) * np.sin(self.phase_params[i] + self.phase_params[j]))
        
        # Quantum-inspired asymmetric basin boundaries
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += np.sin(x[i]**3 + self.phase_params[i]) * np.exp(-x[i]**2) * (1 + 0.15 * np.cos(x[i] + self.phase_params[i]) * np.sin(x[i] + self.phase_params[i]))
            else:
                boundary_effects += np.cos(x[i]**2 + self.phase_params[i]) * np.exp(-x[i]) * (1 + 0.15 * np.sin(x[i] + self.phase_params[i]) * np.cos(x[i] + self.phase_params[i]))
        
        # Enhanced composite function with quantum-enhanced components
        return (0.35 * np.sum(final_values**2) + 
                0.28 * fractal_terms + 
                0.20 * memory_effects + 
                0.15 * cross_coupling + 
                0.02 * boundary_effects)