import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal Brownian motion parameters
        self.hurst_exponents = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(1.0, 5.0, dim)
        # Dynamic harmonic oscillators
        self.oscillator_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.oscillator_phases = np.random.uniform(0, 2*np.pi, dim)
        self.damping_coefficients = np.random.uniform(0.1, 0.5, dim)
        # Basin conditioning parameters
        self.basin_strengths = np.random.uniform(0.5, 2.0, dim)
        self.basin_widths = np.random.uniform(0.2, 1.5, dim)
        # Entropy-based difficulty control
        self.difficulty_factors = np.random.uniform(0.8, 1.8, dim)
        # Adaptive noise scaling
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute fractal Brownian motion component
        fbm_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Simple approximation of FBm using sum of harmonics
            harmonic_sum = 0.0
            for k in range(1, 21):  # Sum first 20 harmonics
                freq = self.oscillator_frequencies[i] * k
                phase = self.oscillator_phases[i]
                amp = self.fractal_amplitudes[i] / (k ** (1 + self.hurst_exponents[i]))
                harmonic_sum += amp * np.sin(freq * x[i] + phase)
            fbm_values[i] = harmonic_sum
        
        # Add dynamic harmonic oscillator terms
        oscillator_terms = np.zeros(self.dim)
        for i in range(self.dim):
            oscillator_terms[i] = np.cos(self.oscillator_frequencies[i] * x[i] + self.oscillator_phases[i]) * \
                                 np.exp(-self.damping_coefficients[i] * np.abs(x[i]))
        
        # Compute basin attraction terms
        basin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Entropy-based basin conditioning
            entropy_factor = 1.0 / (1.0 + np.exp(-self.difficulty_factors[i] * (x[i] - np.mean(x))))
            basin_terms[i] = self.basin_strengths[i] * np.exp(-((x[i] - np.mean(x))**2) / (2 * self.basin_widths[i]**2)) * entropy_factor
        
        # Combine all components
        fitness = 0.0
        for i in range(self.dim):
            # Nonlinear interaction terms
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += np.sin(x[i] - x[j]) * (1 + 0.1 * np.sin(x[i] + x[j]))
            
            # Fractal energy term with harmonic mixing
            fractal_energy = fbm_values[i]**2 + 0.3 * fbm_values[i]**4 + 0.05 * fbm_values[i]**6
            
            # Harmonic oscillator contribution
            osc_contribution = oscillator_terms[i]**2
            
            # Basin attraction component
            basin_contribution = basin_terms[i]
            
            # Adaptive noise term
            noise_term = self.noise_levels[i] * np.random.normal(0, 1)
            
            # Combine all terms with cross-dimensional coupling
            fitness += fractal_energy + osc_contribution + basin_contribution + interaction + noise_term
        
        # Normalize and return
        fitness = fitness / self.dim
        return fitness