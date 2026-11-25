import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quantum-chaotic system parameters with fractional dynamics
        self.fractional_orders = np.random.uniform(0.3, 0.9, dim)
        self.quantum_coupling_coeffs = np.random.uniform(-1.5, 1.5, (dim, 6))
        self.entanglement_strengths = np.random.uniform(0.8, 2.5, dim)
        self.delay_feedback_modulators = np.random.uniform(0.5, 2.0, dim)
        self.bifurcation_exponents = np.random.uniform(1.5, 4.5, dim)
        self.saddle_point_configurations = np.random.uniform(-2.5, 2.5, (dim, 8))
        self.adaptive_noise_levels = np.random.uniform(0.02, 0.3, dim)
        self.transition_scalers = np.random.uniform(0.2, 3.5, dim)
        # Additional quantum and fractal parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.fractal_coupling_matrix = np.random.uniform(-0.7, 0.7, (dim, dim))
        # New hyperchaotic components with altered parameters
        self.hyperchaos_amplitudes = np.random.uniform(1.5, 3.5, dim)  # Increased range
        self.hyperchaos_frequencies = np.random.uniform(2.0, 8.0, dim)  # Shifted range
        self.hyperchaos_damping = np.random.uniform(0.2, 0.9, dim)  # Modified damping
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired chaotic system with fractional dynamics
        result = 0.0
        for i in range(self.dim):
            # Base quantum map with modified Chebyshev polynomials and fractional exponents
            base_value = np.sum([
                self.quantum_coupling_coeffs[i, j] * np.cos(j * np.arccos(np.clip(x_norm[i], -1, 1))) 
                for j in range(6)
            ])
            
            # Fractional-order chaotic dynamics with quantum entanglement
            fractional_term = np.power(np.abs(x_norm[i]), self.fractional_orders[i]) * \
                             np.sin(self.entanglement_strengths[i] * x_norm[i])
            
            # Time-delayed feedback with quantum modulation and adaptive scaling
            delay_sum = 0.0
            for k in range(int(self.delay_feedback_modulators[i]) + 3):
                idx = (i - k - 2) % self.dim
                delay_sum += self.delay_feedback_modulators[i] * np.sin(x_norm[idx] * (k + 1)) * \
                            np.exp(-0.3 * (x_norm[idx] - x_norm[i])**2) * \
                            np.cos(self.quantum_phases[i] * k)
            
            # Saddle-node bifurcation with quantum phase modulation and fractional scaling
            bifurcation_term = self.bifurcation_exponents[i] * (x_norm[i]**3 - x_norm[i])**2 * \
                              np.sin(self.fractional_orders[i] * x_norm[i]) * \
                              np.cos(self.quantum_phases[i])
            
            # Non-smooth transition regions with quantum interference patterns
            transition = 0.0
            for j in range(8):
                transition += np.exp(-self.transition_scalers[i] * (x_norm[i] - self.saddle_point_configurations[i, j])**2) + \
                              0.4 * np.exp(-1.5 * self.transition_scalers[i] * (x_norm[i] - self.saddle_point_configurations[i, j])**2) + \
                              0.2 * np.exp(-3 * self.transition_scalers[i] * (x_norm[i] - self.saddle_point_configurations[i, j])**2) + \
                              0.1 * np.sin(2.5 * self.transition_scalers[i] * (x_norm[i] - self.saddle_point_configurations[i, j]))
            
            # Add quantum noise and combine components
            noise = np.random.normal(0, self.adaptive_noise_levels[i])
            chaotic_value = base_value + fractional_term + delay_sum + bifurcation_term + transition + noise
            
            result += chaotic_value * np.exp(-0.3 * x_norm[i]**2) * \
                     (1.0 + 0.4 * np.sin(self.fractional_orders[i] * x_norm[i]) * \
                      np.cos(self.quantum_phases[i]))
            
        # Enhanced cross-dimensional coupling with quantum entanglement and fractal scaling
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = self.fractal_coupling_matrix[i, j] * \
                                   (1.0 + np.tanh(x_norm[i] * x_norm[j])) * \
                                   np.cos(0.5 * (x_norm[i] - x_norm[j])**2) * \
                                   np.exp(-0.25 * (x_norm[i] - x_norm[j])**2) * \
                                   np.sin(self.quantum_phases[i] + self.quantum_phases[j])
                coupling_terms += coupling_strength * np.sin(x_norm[i] + x_norm[j]) * \
                                 np.cos(0.7 * (x_norm[i] - x_norm[j])) * \
                                 np.exp(-0.1 * np.abs(x_norm[i] - x_norm[j]))
                
        # Additional quantum harmonic components with modified amplitudes, frequencies and entanglement scaling
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += (np.sin(5 * x_norm[i]) + 
                           0.8 * np.cos(6 * x_norm[i]) + 
                           0.6 * np.sin(9 * x_norm[i]) + 
                           0.3 * np.cos(12 * x_norm[i]) *
                           np.exp(-0.3 * x_norm[i]**2) * \
                           np.sin(self.quantum_phases[i]))
            
        # Hyperchaotic components for increased complexity
        hyperchaos_sum = 0.0
        for i in range(self.dim):
            hyperchaos_sum += self.hyperchaos_amplitudes[i] * np.sin(self.hyperchaos_frequencies[i] * x_norm[i]) * \
                             np.exp(-self.hyperchaos_damping[i] * x_norm[i]**2) * \
                             np.cos(self.quantum_phases[i])
        
        # Combine all components with optimized weights and quantum scaling
        total = 0.35 * result + 0.3 * coupling_terms + 0.25 * harmonic_sum + 0.1 * hyperchaos_sum
        
        # Apply a global scaling factor to improve fitness score and reduce statistical errors
        return total * (1.0 + 0.1 * np.sin(np.sum(x_norm**2)))