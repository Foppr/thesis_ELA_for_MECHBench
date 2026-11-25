import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic sine wave components with modified frequencies
        self.chaotic_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.chaotic_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.chaotic_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize radial basis functions with modified parameters
        self.radial_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.radial_weights = np.random.uniform(0.5, 3.0, dim)
        self.radial_widths = np.random.uniform(0.3, 1.5, dim)
        # Initialize polynomial interactions
        self.poly_degrees = np.random.randint(2, 5, dim)
        self.poly_coefficients = np.random.uniform(-1.0, 1.0, dim)
        # Initialize quaternion-inspired harmonic components
        self.harmonic_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.harmonic_frequencies = np.random.uniform(0.8, 3.5, dim)
        self.harmonic_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize dynamic coupling weights
        self.coupling_weights = np.random.uniform(-1.5, 1.5, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0.0)
        # Fractal-like self-similarity parameters
        self.fractal_scaling = np.random.uniform(0.1, 0.5, dim)
        # Memory-dependent evolutionary terms
        self.memory_factors = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sine waves
        for i in range(self.dim):
            chaotic_term = self.chaotic_amplitudes[i] * np.sin(self.chaotic_frequencies[i] * x[i] + self.chaotic_phases[i])
            result += chaotic_term
            
        # Modified radial basis functions
        for i in range(self.dim):
            radial_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.radial_centers[i][j])**2
                radial_sum += self.radial_weights[i] * np.exp(-distance / (2 * self.radial_widths[i]**2))
            result += radial_sum
            
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            poly_term = self.poly_coefficients[i] * (x[i] ** self.poly_degrees[i])
            result += poly_term
            
        # Quaternion-inspired harmonic components
        for i in range(self.dim):
            harmonic_term = self.harmonic_amplitudes[i] * np.cos(self.harmonic_frequencies[i] * x[i] + self.harmonic_phases[i])
            result += harmonic_term
            
        # Dynamic dimensional coupling with memory effects
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_weights[i][j] * np.sin(x[i] * x[j]) * self.memory_factors[i]
                    coupling_sum += coupling_term
            result += coupling_sum
            
        # Fractal-like self-similarity enhancement
        for i in range(self.dim):
            fractal_term = self.fractal_scaling[i] * np.sin(10 * x[i])
            result += fractal_term
            
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.2 * self.dim)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.05)
        
        return result