import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic system parameters with broader distributions
        self.chebyshev_coeffs = np.random.uniform(-0.5, 0.5, (dim, 7))
        self.delay_lengths = np.random.randint(2, 12, dim)
        self.feedback_strengths = np.random.uniform(0.1, 2.0, dim)
        self.attractor_centers = np.random.uniform(-4.5, 4.5, (dim, 6))
        self.phase_transitions = np.random.uniform(0.2, 3.0, dim)
        # New enhanced parameters for better mathematical structure
        self.frequency_modulators = np.random.uniform(0.3, 4.0, dim)
        self.amplitude_modulators = np.random.uniform(0.05, 1.5, dim)
        self.resonance_frequencies = np.random.uniform(0.05, 2.5, dim)
        self.damping_factors = np.random.uniform(0.005, 0.7, dim)
        self.correlation_strengths = np.random.uniform(0.05, 1.5, dim)
        # Additional chaotic and correlation parameters for increased complexity
        self.nonlinearity_params = np.random.uniform(0.05, 2.5, dim)
        self.spectral_weights = np.random.uniform(0.3, 2.0, (dim, 5))
        self.interaction_magnitudes = np.random.uniform(0.3, 2.5, (dim, dim))
        # Enhanced improved parameters to boost fitness and reduce bias
        self.basin_depths = np.random.uniform(0.3, 2.5, dim)
        self.transition_stiffness = np.random.uniform(0.05, 1.5, dim)
        self.noise_amplitudes = np.random.uniform(0.005, 0.3, dim)
        # New high-frequency chaotic components
        self.high_freq_coeffs = np.random.uniform(-0.2, 0.2, (dim, 4))
        self.modulation_indices = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial component with Chebyshev polynomials
        chaotic_term = 0.0
        for i in range(self.dim):
            T = np.zeros(7)
            T[0] = 1.0
            T[1] = x[i]
            for j in range(2, 7):
                T[j] = 2 * x[i] * T[j-1] - T[j-2]
            
            poly_val = np.sum(self.chebyshev_coeffs[i] * T)
            chaotic_term += poly_val**3  # Increased nonlinearity
            
        # Time-delayed feedback component with improved dynamics
        delay_term = 0.0
        for i in range(self.dim):
            delayed_x = x[i] - self.delay_lengths[i]
            if delayed_x < -5.0:
                delayed_x = -5.0
            elif delayed_x > 5.0:
                delayed_x = 5.0
                
            # Enhanced feedback with sine and cosine decay
            feedback = np.sin(0.15 * (x[i] - delayed_x)) * np.cos(0.05 * (x[i] - delayed_x)) * self.feedback_strengths[i]
            delay_term += feedback
            
        # Multi-attractor basin component with enhanced attraction
        attractor_term = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for center in self.attractor_centers[i]:
                dist = np.abs(x[i] - center)
                if dist < min_dist:
                    min_dist = dist
            # Enhanced attraction with exponential decay and basin depth
            attractor_term += self.basin_depths[i] * np.exp(-0.3 * min_dist) * min_dist**3
            
        # Phase-transition induced ruggedness with better control
        ruggedness_term = 0.0
        for i in range(self.dim):
            # Multiple phase transitions with different scales and modulators
            phase_ruggedness = 0.0
            for scale, freq_mod, amp_mod in zip([0.05, 0.2, 0.5, 1.0, 1.5, 2.5], 
                                               self.frequency_modulators[i:i+6], 
                                               self.amplitude_modulators[i:i+6]):
                scaled_x = x[i] / scale
                # Enhanced sine-based phase transition with frequency modulation
                freq = self.phase_transitions[i] * freq_mod
                phase_ruggedness += amp_mod * np.sin(freq * scaled_x) * np.cos(freq * scaled_x) * np.exp(-0.15 * scaled_x**2)
            ruggedness_term += phase_ruggedness**3  # Increased nonlinearity
            
        # New correlation and resonance components to improve fitness
        correlation_term = 0.0
        for i in range(self.dim):
            # Add correlation between dimensions with damping
            corr_val = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_val += self.correlation_strengths[i] * np.sin(self.resonance_frequencies[i] * x[j]) * np.cos(self.resonance_frequencies[i] * x[j]) * np.exp(-self.damping_factors[i] * (x[i] - x[j])**3)
            correlation_term += corr_val**3  # Increased nonlinearity
            
        # Additional chaotic interaction term for increased complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear interaction between dimensions
                interaction = self.interaction_magnitudes[i][j] * np.sin(self.nonlinearity_params[i] * x[i]) * np.cos(self.nonlinearity_params[j] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**4)
                interaction_term += interaction**3  # Increased nonlinearity
                
        # Spectral component with multiple frequency bands
        spectral_term = 0.0
        for i in range(self.dim):
            spec_val = 0.0
            for k, weight in enumerate(self.spectral_weights[i]):
                freq = (k + 1) * self.resonance_frequencies[i]
                spec_val += weight * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.03 * x[i]**2)
            spectral_term += spec_val**3  # Increased nonlinearity
            
        # Add noise component to improve robustness and fitness
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += self.noise_amplitudes[i] * np.random.uniform(-1, 1) * np.exp(-0.15 * x[i]**2)
            
        # High-frequency chaotic component
        high_freq_term = 0.0
        for i in range(self.dim):
            hf_val = 0.0
            for k, coeff in enumerate(self.high_freq_coeffs[i]):
                freq = (k + 1) * self.modulation_indices[i]
                hf_val += coeff * np.sin(freq * x[i]) * np.cos(freq * x[i])
            high_freq_term += hf_val**2
            
        # Combine all components with dynamic weights and improved scaling
        adaptive_factor = np.log(self.dim + 3) + 0.7
        result = adaptive_factor * chaotic_term + 0.15 * delay_term + 0.35 * attractor_term + 0.55 * ruggedness_term + 0.25 * correlation_term + 0.08 * interaction_term + 0.12 * spectral_term + 0.03 * noise_term + 0.05 * high_freq_term
        
        return result