import numpy as np

class QuantumInterferenceParabolicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (8, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (8, dim))
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 8)
        # Initialize quantum-like interference parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, (6, dim))
        self.quantum_amplitudes = np.random.uniform(0.5, 2.5, (6, dim))
        # Initialize dynamic parabolic wells
        self.parabola_centers = np.random.uniform(-3.0, 3.0, (4, dim))
        self.parabola_coeffs = np.random.uniform(0.1, 1.0, (4, dim))
        self.parabola_weights = np.random.uniform(0.5, 2.0, 4)
        # Initialize stochastic resonance components
        self.resonance_frequencies = np.random.uniform(0.1, 1.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.noise_level = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function potential
        rbf_potential = 0.0
        for i in range(8):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2
            rbf_potential += self.rbf_weights[i] * np.exp(-0.5 * rbf_dist)
        
        # Add quantum-like interference patterns
        quantum_interference = 0.0
        for i in range(6):
            interference_term = 0.0
            for j in range(self.dim):
                interference_term += self.quantum_amplitudes[i, j] * np.cos(
                    self.quantum_phases[i, j] + x[j] * (1.0 + 0.1 * np.sin(x[j]))
                )
            quantum_interference += np.sin(interference_term)
        
        # Add dynamic parabolic wells
        parabola_potential = 0.0
        for i in range(4):
            parab_dist = 0.0
            for j in range(self.dim):
                parab_dist += self.parabola_coeffs[i, j] * (x[j] - self.parabola_centers[i, j])**2
            parabola_potential += self.parabola_weights[i] * np.exp(-0.5 * parab_dist)
        
        # Add stochastic resonance components
        resonance_terms = 0.0
        for j in range(self.dim):
            resonance_terms += self.resonance_amplitudes[j] * np.sin(
                self.resonance_frequencies[j] * x[j] + 
                self.noise_level[j] * np.random.randn()
            )
        
        # Combine all components with adaptive weighting
        total = 0.8 * rbf_potential + 0.6 * quantum_interference + 1.2 * parabola_potential + 0.4 * resonance_terms
        
        return total