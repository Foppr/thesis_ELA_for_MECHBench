import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_coeffs = np.random.uniform(-0.5, 0.5, (dim, 4))
        self.delay_lengths = np.random.randint(1, 6, dim)
        self.feedback_strengths = np.random.uniform(0.1, 2.0, dim)
        self.attractor_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.phase_transitions = np.random.uniform(0.5, 2.0, dim)
        # Additional stochastic resonance parameters
        self.resonance_strengths = np.random.uniform(0.1, 1.0, dim)
        self.noise_levels = np.random.uniform(0.01, 0.5, dim)
        # Fractional Brownian motion parameters
        self.hurst_exponents = np.random.uniform(0.3, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial component with Chebyshev polynomials
        chaotic_term = 0.0
        for i in range(self.dim):
            # Generate Chebyshev polynomial evaluation
            T = np.zeros(4)
            T[0] = 1.0
            T[1] = x[i]
            for j in range(2, 4):
                T[j] = 2 * x[i] * T[j-1] - T[j-2]
            
            poly_val = np.sum(self.chebyshev_coeffs[i] * T)
            chaotic_term += poly_val**2
            
        # Time-delayed feedback component
        delay_term = 0.0
        for i in range(self.dim):
            delayed_x = x[i] - self.delay_lengths[i]
            if delayed_x < -5.0:
                delayed_x = -5.0
            elif delayed_x > 5.0:
                delayed_x = 5.0
                
            # Feedback with exponential decay
            feedback = np.exp(-0.1 * (x[i] - delayed_x)**2) * self.feedback_strengths[i]
            delay_term += feedback
            
        # Multi-attractor basin component
        attractor_term = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for center in self.attractor_centers[i]:
                dist = np.abs(x[i] - center)
                if dist < min_dist:
                    min_dist = dist
            attractor_term += min_dist**2
            
        # Phase-transition induced ruggedness
        ruggedness_term = 0.0
        for i in range(self.dim):
            # Multiple phase transitions with different scales
            phase_ruggedness = 0.0
            for scale in [0.1, 0.5, 1.0, 2.0]:
                scaled_x = x[i] / scale
                # Sine-based phase transition with varying frequency
                freq = self.phase_transitions[i] * scale
                phase_ruggedness += np.sin(freq * scaled_x) * np.exp(-0.05 * scaled_x**2)
            ruggedness_term += phase_ruggedness**2
            
        # Stochastic resonance component
        resonance_term = 0.0
        for i in range(self.dim):
            # Add noise and sinusoidal forcing
            noise = np.random.normal(0, self.noise_levels[i])
            forcing = self.resonance_strengths[i] * np.sin(x[i] * 2.0)
            resonance_term += (forcing + noise)**2
            
        # Fractional Brownian motion component for long-range dependence
        fbm_term = 0.0
        for i in range(self.dim):
            # Simple approximation of FBM using random walks with memory
            fbm_val = np.random.normal(0, 1) * (1.0 + self.hurst_exponents[i] * x[i])
            fbm_term += fbm_val**2
            
        # Combine all components with dynamic weights
        adaptive_factor = np.log(self.dim + 1) + 1.0
        result = adaptive_factor * chaotic_term + 0.3 * delay_term + 0.5 * attractor_term + 0.7 * ruggedness_term + 0.2 * resonance_term + 0.1 * fbm_term
        
        return result