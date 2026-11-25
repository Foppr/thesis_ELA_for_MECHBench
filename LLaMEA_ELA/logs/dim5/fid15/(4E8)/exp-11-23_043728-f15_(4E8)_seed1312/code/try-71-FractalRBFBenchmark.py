import numpy as np

class FractalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.fractal_dim = 1.5 + np.random.rand() * 0.5
        self.scale_factor = 2.0 + np.random.rand() * 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Generate fractal-like structure using polynomial chaos expansion
        poly_chaos = np.zeros(self.dim)
        for i in range(self.dim):
            poly_chaos[i] = np.sum([np.sin((j+1) * x_norm[i]) * np.cos((j+1) * x_norm[(i+j) % self.dim]) 
                                  for j in range(1, 6)])
        
        # Radial basis function components with varying widths
        rbf_values = np.zeros(self.dim)
        centers = np.random.uniform(-1, 1, (5, self.dim))
        widths = np.random.uniform(0.1, 0.5, 5)
        
        for i in range(5):
            diff = x_norm - centers[i]
            rbf_values += widths[i] * np.exp(-np.sum(diff**2) / (2 * widths[i]**2))
        
        # Spectral decomposition component
        spectrum = np.fft.fft(x_norm)
        spectral_energy = np.real(np.sum(spectrum * np.conj(spectrum)))
        
        # Combine all components with adaptive weighting
        total = 0.3 * np.sum(poly_chaos**2) + 0.4 * np.sum(rbf_values) + 0.3 * spectral_energy
        
        # Add fractal scaling effect
        fractal_effect = self.scale_factor ** (np.log(self.dim + 1) / np.log(2))
        
        # Introduce multi-modal structure with sinusoidal modulation
        modal_structure = np.sin(5 * np.sum(x_norm**2)) * np.cos(3 * np.sum(x_norm**3))
        
        # Add dimensionality-dependent penalty
        penalty = 0.1 * self.dim * np.mean(x_norm**4)
        
        return fractal_effect * (total + modal_structure + penalty) + 0.01 * np.random.rand()