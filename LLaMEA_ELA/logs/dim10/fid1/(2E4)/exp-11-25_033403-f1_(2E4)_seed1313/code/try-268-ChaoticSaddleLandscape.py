import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.well_depths = np.random.uniform(1.0, 6.0, dim)
        self.well_positions = np.random.uniform(-4.5, 4.5, dim)
        self.well_widths = np.random.uniform(0.3, 2.5, dim)
        self.coupling_strength = np.random.uniform(0.8, 4.0, (dim, dim))
        self.hyperbolic_params = np.random.uniform(1.5, 5.0, dim)
        self.resonance_freq = np.random.uniform(0.5, 4.0, dim)
        self.stochastic_amplitude = np.random.uniform(0.05, 0.5, dim)
        self.saddle_indices = np.random.choice(dim, size=min(6, dim), replace=False)
        self.scale_factors = np.random.uniform(0.5, 3.0, dim)
        # Add enhanced cubic nonlinearities
        self.cubic_coefficients = np.random.uniform(0.2, 0.8, dim)
        # Add fractal scaling parameters
        self.fractal_exponents = np.random.uniform(1.2, 2.5, dim)
        # Add quantum-like resonance terms
        self.quantum_amplitudes = np.random.uniform(0.1, 0.7, dim)
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.quantum_frequencies = np.random.uniform(1.0, 6.0, dim)
        # Add chaotic logistic map components
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Add multi-scale harmonic terms
        self.harmonic_amplitudes = np.random.uniform(0.2, 1.0, dim)
        self.harmonic_frequencies = np.random.uniform(2.0, 8.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add exponential potential wells
        for i in range(self.dim):
            well_potential = self.well_depths[i] * np.exp(-0.5 * ((x[i] - self.well_positions[i]) / self.well_widths[i])**2)
            fitness -= well_potential
            
        # Add enhanced hyperbolic coupling between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strength[i, j] * np.tanh(self.hyperbolic_params[i] * x[i]) * np.tanh(self.hyperbolic_params[j] * x[j])
                coupling_terms += coupling
                
        # Add stochastic resonance terms
        stochastic_terms = 0.0
        for i in range(self.dim):
            stochastic = self.stochastic_amplitude[i] * np.sin(self.resonance_freq[i] * x[i] + np.random.uniform(0, 2*np.pi))
            stochastic_terms += stochastic
            
        # Add saddle-point contributions
        saddle_terms = 0.0
        for i in self.saddle_indices:
            saddle_term = x[i]**2 * (x[i]**2 - self.scale_factors[i]**2)
            saddle_terms += saddle_term
            
        # Add enhanced multi-scale fractal-like terms
        fractal_terms = 0.0
        for i in range(self.dim):
            scale_sum = 0.0
            for k in range(1, 10):
                scale = self.scale_factors[i] * (2.0**k)
                scale_sum += np.sin(scale * x[i]) / (k**self.fractal_exponents[i])
            fractal_terms += scale_sum
            
        # Add enhanced cubic nonlinear terms
        cubic_terms = 0.0
        for i in range(self.dim):
            cubic_terms += self.cubic_coefficients[i] * x[i]**3
            
        # Add quantum-like resonance terms
        quantum_terms = 0.0
        for i in range(self.dim):
            quantum_term = self.quantum_amplitudes[i] * np.sin(self.quantum_frequencies[i] * x[i] + self.quantum_phases[i]) * np.cos(self.quantum_frequencies[i] * x[i] + self.quantum_phases[i])
            quantum_terms += quantum_term
            
        # Add chaotic logistic map components
        logistic_terms = 0.0
        for i in range(self.dim):
            logistic_terms += self.logistic_r[i] * self.logistic_x[i] * (1 - self.logistic_x[i])
            
        # Add multi-scale harmonic terms
        harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_sum = 0.0
            for k in range(1, 6):
                harmonic_sum += self.harmonic_amplitudes[i] * np.sin(k * self.harmonic_frequencies[i] * x[i])
            harmonic_terms += harmonic_sum
            
        # Combine all components with adjusted weights
        total = 0.2 * fitness + 0.3 * coupling_terms + 0.15 * stochastic_terms + 0.1 * saddle_terms + 0.1 * fractal_terms + 0.05 * cubic_terms + 0.05 * quantum_terms + 0.03 * logistic_terms + 0.02 * harmonic_terms
        
        return total