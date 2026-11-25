import numpy as np

class QuantumInterferenceParabolicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.8, (10, dim))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, 10)
        # Initialize quantum-like interference parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, (8, dim))
        self.quantum_amplitudes = np.random.uniform(0.3, 3.0, (8, dim))
        # Initialize dynamic parabolic wells
        self.parabola_centers = np.random.uniform(-3.5, 3.5, (6, dim))
        self.parabola_coeffs = np.random.uniform(0.05, 1.2, (6, dim))
        self.parabola_weights = np.random.uniform(0.3, 2.5, 6)
        # Initialize stochastic resonance components
        self.resonance_frequencies = np.random.uniform(0.05, 1.5, dim)
        self.resonance_amplitudes = np.random.uniform(0.05, 0.8, dim)
        self.noise_level = np.random.uniform(0.005, 0.15, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function potential with higher-order interactions
        rbf_potential = 0.0
        for i in range(10):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2
            rbf_potential += self.rbf_weights[i] * np.exp(-0.3 * rbf_dist) * (1 + 0.1 * np.sin(rbf_dist))
        
        # Add quantum-like interference patterns with polynomial modulation
        quantum_interference = 0.0
        for i in range(8):
            interference_term = 0.0
            for j in range(self.dim):
                interference_term += self.quantum_amplitudes[i, j] * np.cos(
                    self.quantum_phases[i, j] + x[j] * (1.0 + 0.2 * np.sin(x[j]**2))
                )
            quantum_interference += np.sin(interference_term) * (1 + 0.05 * np.sum(x**4))
        
        # Add dynamic parabolic wells with adaptive coefficients
        parabola_potential = 0.0
        for i in range(6):
            parab_dist = 0.0
            for j in range(self.dim):
                parab_dist += self.parabola_coeffs[i, j] * (x[j] - self.parabola_centers[i, j])**2 + 0.01 * x[j]**4
            parabola_potential += self.parabola_weights[i] * np.exp(-0.4 * parab_dist) * (1 + 0.15 * np.cos(parab_dist))
        
        # Add stochastic resonance components with enhanced noise sensitivity
        resonance_terms = 0.0
        for j in range(self.dim):
            resonance_terms += self.resonance_amplitudes[j] * np.sin(
                self.resonance_frequencies[j] * x[j] + 
                self.noise_level[j] * np.random.randn() + 
                0.1 * np.sin(x[j]**3)
            )
        
        # Combine all components with adaptive weighting and enhanced non-separability
        total = 1.0 * rbf_potential + 0.8 * quantum_interference + 1.5 * parabola_potential + 0.6 * resonance_terms
        
        # Add a global scaling factor to increase the overall landscape complexity
        total *= (1.0 + 0.2 * np.sum(np.abs(x)**3) / self.dim)
        
        return total