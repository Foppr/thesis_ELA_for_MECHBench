import numpy as np

class SinusoidalRadialHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize sinusoidal components with random frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 3.0, dim)
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        # Initialize harmonic components with time-varying parameters
        self.harm_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.harm_frequencies = np.random.uniform(0.5, 3.0, dim)
        # Initialize phase shifts for harmonic components
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize cross-dimensional interaction weights
        self.interaction_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute sinusoidal components
        sin_terms = 0.0
        for j in range(self.dim):
            sin_terms += self.sin_amplitudes[j] * np.sin(self.sin_frequencies[j] * x[j])
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for j in range(self.dim):
            rbf_sum = 0.0
            for i in range(self.dim):
                diff = x[i] - self.rbf_centers[j, i]
                rbf_sum += np.exp(-0.5 * (diff**2) / (self.rbf_widths[j]**2))
            rbf_terms += rbf_sum
        
        # Compute harmonic components with time-varying parameters
        harm_terms = 0.0
        for j in range(self.dim):
            harm_terms += self.harm_amplitudes[j] * np.cos(self.harm_frequencies[j] * x[j] + self.phases[j])
        
        # Compute cross-dimensional interaction terms
        interaction_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_terms += self.interaction_weights[i, j] * np.sin(x[i] * x[j])
        
        # Combine all components with appropriate weights
        total = 0.4 * sin_terms + 0.3 * rbf_terms + 0.2 * harm_terms + 0.1 * interaction_terms
        
        return total