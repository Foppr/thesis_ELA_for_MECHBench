import numpy as np

class TrigonometricGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components
        self.n_components = 8
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        self.gauss_covariances = np.random.uniform(0.5, 2.0, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.1, 1.0, self.n_components)
        self.gauss_weights /= np.sum(self.gauss_weights)
        
        # Initialize trigonometric wave parameters
        self.wave_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.wave_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Initialize adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        
        # Initialize dynamic gradient modulation parameters
        self.modulation_freqs = np.random.uniform(0.5, 3.0, dim)
        self.modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute Gaussian mixture potential
        gaussian_potential = 0.0
        for i in range(self.n_components):
            diff = x - self.gauss_centers[i]
            exponent = -0.5 * np.sum((diff**2) / self.gauss_covariances[i])
            gaussian_potential += self.gauss_weights[i] * np.exp(exponent)
        
        # Compute trigonometric wave interference pattern
        wave_potential = 0.0
        for j in range(self.dim):
            wave_potential += self.wave_amplitudes[j] * np.sin(self.wave_frequencies[j] * x[j] + self.wave_phases[j])
        
        # Add cross-dimensional trigonometric interactions
        cross_wave = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_wave += np.sin(self.wave_frequencies[i] * x[i]) * np.cos(self.wave_frequencies[j] * x[j])
        
        # Apply adaptive conditioning
        conditioning = 0.0
        for j in range(self.dim):
            conditioning += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.3 * np.sin(0.5 * x[j]))
        
        # Add dynamic gradient modulation
        gradient_modulation = 0.0
        for j in range(self.dim):
            gradient_modulation += self.modulation_amplitudes[j] * np.cos(self.modulation_freqs[j] * x[j]) * np.sin(x[j])
        
        # Combine all components with appropriate weights
        total = 1.5 * gaussian_potential + 0.8 * wave_potential + 0.3 * cross_wave + 0.2 * conditioning + 0.1 * gradient_modulation
        
        # Add a complex interaction term between all dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
        
        total += 0.15 * interaction_term
        
        return total