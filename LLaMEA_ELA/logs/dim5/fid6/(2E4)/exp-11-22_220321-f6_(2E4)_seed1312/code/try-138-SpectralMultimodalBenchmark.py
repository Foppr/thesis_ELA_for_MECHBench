import numpy as np

class SpectralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_scale = 2.0
        self.gaussian_components = 3
        self.saddle_strength = 1.5
        self.oscillation_frequency = 3.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spectral component using discrete Fourier transform approximation
        spectral_term = 0.0
        for i in range(self.dim):
            coord = x[i]
            # Approximate DFT-like behavior with sine/cosine sums
            for k in range(1, 6):
                spectral_term += (np.sin(k * coord * self.frequency_scale) + 
                                np.cos(k * coord * self.frequency_scale)) / (k**1.5)
        
        # Gaussian mixture component with adaptive weights
        gaussian_term = 0.0
        for i in range(self.gaussian_components):
            # Dynamic centers and widths based on dimension
            center = 2.0 * np.sin(i * np.pi / self.gaussian_components)
            width = 1.0 + 0.5 * np.cos(i * np.pi / self.gaussian_components)
            gaussian_term += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Saddle-point interaction component
        saddle_term = 0.0
        for i in range(self.dim):
            # Dynamic saddle points with chaotic modulation
            chaos_mod = 1.0 + self.saddle_strength * np.sin(x[i] * (i + 1) * 0.5)
            saddle_term += chaos_mod * x[i]**2 * np.cos(x[i] * self.oscillation_frequency)
        
        # Cross-dimensional coupling with dynamic interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on coordinate magnitudes
                weight = 1.0 / (1.0 + np.exp(-0.5 * (np.abs(x[i]) - np.abs(x[j]))))
                interaction = np.sin(x[i] * x[j]) * np.tanh(x[i] + x[j])
                cross_term += weight * interaction
        
        # Dynamic scaling factor based on global coordinate structure
        norm_x = np.linalg.norm(x)
        dynamic_scale = 1.0 + 0.3 * np.sin(norm_x * 0.3) * np.cos(self.dim * 0.2)
        
        # Combine all terms with adaptive weights
        return dynamic_scale * (0.25 * spectral_term + 
                              0.3 * gaussian_term + 
                              0.25 * saddle_term + 
                              0.2 * cross_term)