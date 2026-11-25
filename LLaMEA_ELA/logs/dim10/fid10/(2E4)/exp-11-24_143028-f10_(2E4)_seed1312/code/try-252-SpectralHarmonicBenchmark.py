import numpy as np

class SpectralHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random matrix for spectral decomposition
        self.matrix = np.random.randn(dim, dim)
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(self.matrix)
        # Harmonic potential parameters
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Noise injection parameters
        self.noise_levels = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spectral decomposition based potential
        spectral_potential = 0.0
        for i in range(self.dim):
            # Project x onto eigenvector basis
            proj = np.dot(x, self.eigenvectors[:, i])
            # Apply frequency-dependent harmonic potential
            spectral_potential += self.amplitudes[i] * (self.frequencies[i] * proj)**2
            
        # Harmonic coupling between dimensions
        harmonic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.3 * (1.0 + np.sin(0.5 * (x[i] + x[j])))
                harmonic_coupling += coupling_strength * (x[i] - x[j])**2
                
        # Adaptive noise injection
        noise_term = 0.0
        for i in range(self.dim):
            noise_freq = self.noise_frequencies[i]
            noise_level = self.noise_levels[i]
            # Inject frequency-dependent noise
            noise_term += noise_level * np.sin(noise_freq * x[i])
            
        # Multi-modal landscape with periodic components
        periodic_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima using sine waves
            periodic_term += np.sin(2.0 * np.pi * x[i] / 3.0) + \
                           0.5 * np.sin(4.0 * np.pi * x[i] / 3.0) + \
                           0.3 * np.sin(6.0 * np.pi * x[i] / 3.0)
            
        # Combine all terms
        result = 0.4 * spectral_potential + 0.3 * harmonic_coupling + \
                 0.2 * noise_term + 0.1 * periodic_term
        
        return result