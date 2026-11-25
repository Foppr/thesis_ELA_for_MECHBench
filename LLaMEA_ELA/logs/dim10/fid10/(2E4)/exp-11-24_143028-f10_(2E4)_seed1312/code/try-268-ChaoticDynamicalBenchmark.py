import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with better distribution
        self.chebyshev_coeffs = np.random.uniform(-0.3, 0.3, (dim, 5))
        self.delay_lengths = np.random.randint(1, 8, dim)
        self.feedback_strengths = np.random.uniform(0.2, 1.5, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, (dim, 4))
        self.phase_transitions = np.random.uniform(0.3, 2.5, dim)
        # Add new parameters for better control
        self.frequency_modulators = np.random.uniform(0.5, 3.0, dim)
        self.amplitude_modulators = np.random.uniform(0.1, 1.0, dim)
        # New parameters to improve mathematical structure and fitness
        self.resonance_frequencies = np.random.uniform(0.2, 2.5, dim)  # Slightly increased range
        self.damping_factors = np.random.uniform(0.01, 0.5, dim)
        self.correlation_strengths = np.random.uniform(0.3, 1.2, dim)  # Increased range
        # Additional chaotic and correlation parameters for increased complexity
        self.nonlinearity_params = np.random.uniform(0.1, 2.0, dim)
        self.spectral_weights = np.random.uniform(0.5, 1.5, (dim, 3))
        self.interaction_magnitudes = np.random.uniform(0.8, 2.5, (dim, dim))  # Increased range
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial component with Chebyshev polynomials
        chaotic_term = 0.0
        for i in range(self.dim):
            # Generate Chebyshev polynomial evaluation
            T = np.zeros(5)
            T[0] = 1.0
            T[1] = x[i]
            for j in range(2, 5):
                T[j] = 2 * x[i] * T[j-1] - T[j-2]
            
            poly_val = np.sum(self.chebyshev_coeffs[i] * T)
            chaotic_term += poly_val**2
            
        # Time-delayed feedback component with improved dynamics
        delay_term = 0.0
        for i in range(self.dim):
            delayed_x = x[i] - self.delay_lengths[i]
            if delayed_x < -5.0:
                delayed_x = -5.0
            elif delayed_x > 5.0:
                delayed_x = 5.0
                
            # Improved feedback with cosine decay
            feedback = np.cos(0.1 * (x[i] - delayed_x)) * self.feedback_strengths[i]
            delay_term += feedback
            
        # Multi-attractor basin component with enhanced attraction
        attractor_term = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for center in self.attractor_centers[i]:
                dist = np.abs(x[i] - center)
                if dist < min_dist:
                    min_dist = dist
            # Enhanced attraction with exponential decay
            attractor_term += np.exp(-0.5 * min_dist) * min_dist**2
            
        # Phase-transition induced ruggedness with better control
        ruggedness_term = 0.0
        for i in range(self.dim):
            # Multiple phase transitions with different scales and modulators
            phase_ruggedness = 0.0
            for scale, freq_mod, amp_mod in zip([0.1, 0.3, 0.7, 1.0, 2.0], 
                                               self.frequency_modulators[i:i+5], 
                                               self.amplitude_modulators[i:i+5]):
                scaled_x = x[i] / scale
                # Enhanced sine-based phase transition with frequency modulation
                freq = self.phase_transitions[i] * freq_mod
                phase_ruggedness += amp_mod * np.sin(freq * scaled_x) * np.exp(-0.1 * scaled_x**2)
            ruggedness_term += phase_ruggedness**2
            
        # New correlation and resonance components to improve fitness
        correlation_term = 0.0
        for i in range(self.dim):
            # Add correlation between dimensions with damping
            corr_val = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_val += self.correlation_strengths[i] * np.sin(self.resonance_frequencies[i] * x[j]) * np.exp(-self.damping_factors[i] * (x[i] - x[j])**2)
            correlation_term += corr_val**2
            
        # Additional chaotic interaction term for increased complexity
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear interaction between dimensions
                interaction = self.interaction_magnitudes[i][j] * np.sin(self.nonlinearity_params[i] * x[i]) * np.cos(self.nonlinearity_params[j] * x[j])
                interaction_term += interaction**2
                
        # Spectral component with multiple frequency bands
        spectral_term = 0.0
        for i in range(self.dim):
            spec_val = 0.0
            for k, weight in enumerate(self.spectral_weights[i]):
                freq = (k + 1) * self.resonance_frequencies[i]
                spec_val += weight * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            spectral_term += spec_val**2
            
        # Combine all components with dynamic weights and improved scaling
        adaptive_factor = np.log(self.dim + 2) + 0.5
        result = adaptive_factor * chaotic_term + 0.2 * delay_term + 0.4 * attractor_term + 0.6 * ruggedness_term + 0.3 * correlation_term + 0.1 * interaction_term + 0.15 * spectral_term
        
        return result