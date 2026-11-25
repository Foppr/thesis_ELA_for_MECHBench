import numpy as np

class ChaoticQuaternionPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quaternion-based potential parameters
        self.quaternion_amplitudes = np.random.uniform(1.0, 5.0, dim)
        self.quaternion_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.quaternion_phases = np.random.uniform(0, 2*np.pi, dim)
        # Adaptive gradient modulation parameters
        self.gradient_strengths = np.random.uniform(0.1, 2.0, dim)
        self.gradient_exponents = np.random.uniform(1.0, 4.0, dim)
        # Dynamic dimensional coupling
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.coupling_delays = np.random.randint(1, 6, (dim, dim))
        # Chaotic time-varying parameters
        self.time_varying_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.time_varying_frequencies = np.random.uniform(2.0, 8.0, dim)
        # Dimensional scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-based potential components
        quaternion_potential = 0
        for i in range(self.dim):
            xi = x[i]
            # Create quaternion-like interaction with imaginary components
            real_part = self.quaternion_amplitudes[i] * np.sin(self.quaternion_frequencies[i] * xi + self.quaternion_phases[i])
            imag_part = self.quaternion_amplitudes[i] * np.cos(self.quaternion_frequencies[i] * xi + self.quaternion_phases[i])
            quaternion_potential += real_part * imag_part
        
        # Adaptive gradient modulation
        gradient_modulation = 0
        for i in range(self.dim):
            xi = x[i]
            # Apply adaptive scaling based on position and gradient strength
            grad_term = self.gradient_strengths[i] * np.power(abs(xi), self.gradient_exponents[i])
            gradient_modulation += grad_term
        
        # Dynamic dimensional coupling
        coupling_term = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Apply delayed coupling with time-varying weights
                    delayed_xj = x[j] * np.sin(self.coupling_delays[i][j] * x[i])
                    coupling_term += self.coupling_weights[i][j] * np.sin(x[i] + delayed_xj)
        
        # Time-varying chaotic component
        time_varying_component = 0
        for i in range(self.dim):
            xi = x[i]
            # Add time-varying modulation with dynamic frequency
            time_mod = self.time_varying_amplitudes[i] * np.cos(self.time_varying_frequencies[i] * xi)
            time_varying_component += time_mod
        
        # Apply dimensional scaling
        scaled_terms = 0
        for i in range(self.dim):
            scaled_terms += self.scaling_factors[i] * x[i]**2
        
        # Combine all components with chaotic weighting
        result = (0.8 * quaternion_potential + 
                 1.2 * gradient_modulation + 
                 0.9 * coupling_term + 
                 0.7 * time_varying_component + 
                 0.6 * scaled_terms)
        
        return result