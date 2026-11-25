import numpy as np

class ChaoticHarmonicCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.5, 2.0, dim)
        self.tent_centers = np.random.uniform(-4.0, 4.0, dim)
        # Initialize radial harmonic components
        self.harmonic_amps = np.random.uniform(0.5, 3.0, dim)
        self.harmonic_freqs = np.random.uniform(1.0, 6.0, dim)
        self.harmonic_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize polynomial coupling coefficients
        self.poly_couplings = np.random.uniform(-1.0, 1.0, (dim, dim))
        np.fill_diagonal(self.poly_couplings, 0.0)
        # Initialize neural network-inspired weights
        self.nn_weights = np.random.uniform(0.1, 2.0, (dim, dim))
        self.nn_biases = np.random.uniform(-1.0, 1.0, dim)
        # Adaptive scaling factors
        self.adaptive_scale = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic tent map dynamics
        for i in range(self.dim):
            tent_val = self.tent_params[i] * np.abs(x[i] - self.tent_centers[i])
            if tent_val > 1.0:
                tent_val = 2.0 - tent_val
            result += tent_val
            
        # Radial harmonic oscillations
        for i in range(self.dim):
            radial_term = self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * np.sqrt(np.sum(x**2)) + self.harmonic_phases[i])
            result += radial_term
            
        # Cross-dimensional polynomial couplings
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    poly_term = self.poly_couplings[i][j] * (x[i] ** 2) * (x[j] ** 3)
                    poly_sum += poly_term
            result += poly_sum
            
        # Neural network-inspired weight adjustments
        for i in range(self.dim):
            nn_contribution = 0.0
            for j in range(self.dim):
                nn_contribution += self.nn_weights[i][j] * np.tanh(x[j] + self.nn_biases[j])
            result += nn_contribution * self.adaptive_scale[i]
            
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.2 * self.dim)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.05)
        
        return result