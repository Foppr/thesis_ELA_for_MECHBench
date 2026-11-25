import numpy as np

class QuantumFractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired fractal parameters
        self.quantum_hurst = np.random.uniform(0.05, 0.95, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 6.0, dim)
        self.quantum_phases = np.random.uniform(0, 4*np.pi, dim)
        # Dynamic harmonic oscillators with quantum coupling
        self.oscillator_frequencies = np.random.uniform(0.2, 4.0, dim)
        self.damping_coefficients = np.random.uniform(0.05, 0.8, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, dim)
        # Basin conditioning with quantum entropy
        self.basin_strengths = np.random.uniform(0.3, 2.5, dim)
        self.basin_widths = np.random.uniform(0.1, 2.0, dim)
        self.quantum_entropy_factors = np.random.uniform(0.6, 2.2, dim)
        # Spectral interference parameters
        self.interference_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.spectral_shifts = np.random.uniform(-0.5, 0.5, dim)
        # Adaptive noise with quantum scaling
        self.noise_levels = np.random.uniform(0.005, 0.15, dim)
        # Quantum phase coupling matrix
        self.phase_coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        np.fill_diagonal(self.phase_coupling_matrix, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute quantum-inspired fractal Brownian motion
        fbm_values = np.zeros(self.dim)
        for i in range(self.dim):
            harmonic_sum = 0.0
            for k in range(1, 31):  # Sum first 30 harmonics for richer structure
                freq = self.oscillator_frequencies[i] * k
                phase = self.quantum_phases[i] + np.sum(self.phase_coupling_matrix[i, :] * x)
                amp = self.fractal_amplitudes[i] / (k ** (1 + self.quantum_hurst[i]))
                harmonic_sum += amp * np.sin(freq * x[i] + phase)
            fbm_values[i] = harmonic_sum
        
        # Add quantum harmonic oscillator terms with coupling
        oscillator_terms = np.zeros(self.dim)
        for i in range(self.dim):
            osc_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_strengths[i] * np.sin(x[i] - x[j])
                    osc_term += coupling * np.cos(self.oscillator_frequencies[i] * x[i])
            oscillator_terms[i] = (np.cos(self.oscillator_frequencies[i] * x[i] + self.quantum_phases[i]) * 
                                 np.exp(-self.damping_coefficients[i] * np.abs(x[i])) + osc_term)
        
        # Compute quantum basin attraction terms
        basin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Quantum entropy-based basin conditioning
            mean_x = np.mean(x)
            entropy_factor = 1.0 / (1.0 + np.exp(-self.quantum_entropy_factors[i] * (x[i] - mean_x)))
            basin_terms[i] = self.basin_strengths[i] * np.exp(-((x[i] - mean_x)**2) / (2 * self.basin_widths[i]**2)) * entropy_factor
        
        # Spectral interference terms
        spectral_terms = np.zeros(self.dim)
        for i in range(self.dim):
            interference = 0.0
            for j in range(self.dim):
                if i != j:
                    interference += self.interference_amplitudes[i] * np.cos((x[i] - x[j]) * (1 + self.spectral_shifts[i]))
            spectral_terms[i] = interference
        
        # Combine all components with quantum interaction
        fitness = 0.0
        for i in range(self.dim):
            # Quantum interaction terms with phase coupling
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_diff = np.sin(x[i] - x[j]) + self.phase_coupling_matrix[i, j] * np.cos(x[i] + x[j])
                    interaction += phase_diff * (1 + 0.2 * np.sin(x[i] - x[j]))
            
            # Quantum fractal energy term with harmonic mixing
            fractal_energy = fbm_values[i]**2 + 0.4 * fbm_values[i]**4 + 0.08 * fbm_values[i]**6
            
            # Quantum oscillator contribution
            osc_contribution = oscillator_terms[i]**2
            
            # Basin attraction component
            basin_contribution = basin_terms[i]
            
            # Spectral interference component
            spectral_contribution = spectral_terms[i]**2
            
            # Adaptive quantum noise term
            noise_term = self.noise_levels[i] * np.random.normal(0, 1)
            
            # Combine all terms with quantum cross-dimensional coupling
            fitness += fractal_energy + osc_contribution + basin_contribution + spectral_contribution + interaction + noise_term
        
        # Normalize and return
        fitness = fitness / self.dim
        return fitness