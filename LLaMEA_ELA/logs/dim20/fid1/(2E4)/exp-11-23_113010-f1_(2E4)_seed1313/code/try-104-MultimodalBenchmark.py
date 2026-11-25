import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logarithmic spiral basin structure with fractal scaling
        spiral_basin = np.sum(np.log(np.abs(x_norm) + 1e-8) * np.cos(np.log(np.abs(x_norm) + 1e-8)))
        
        # Chaotic cosine modulations with varying frequencies and amplitude scaling
        chaotic_mod = np.sum(np.cos(2**(self.dim + 1) * np.pi * x_norm) * 
                            np.cos(3**(self.dim + 2) * np.pi * x_norm**2) * 
                            np.cos(5**(self.dim + 3) * np.pi * x_norm**3))
        
        # Self-similar cross-dimensional interactions with fractal coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling coefficient based on dimension indices
                coupling_coef = (i + 1) ** (-j - 1) * (j + 1) ** (-i - 1)
                cross_interaction += coupling_coef * (x_norm[i]**3 + x_norm[j]**3) * np.sin(2**(i+j+1) * np.pi * (x_norm[i] - x_norm[j]))
        
        # Multi-scale fractal basin with varying exponents
        fractal_basin = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(self.dim * np.pi * x_norm)) + 
                              0.3 * np.abs(x_norm)**(2.0 + 0.7 * np.cos(self.dim * np.pi * x_norm)))
        
        # High-frequency chaotic noise with dimension-dependent frequency
        noise_freq = 2**(self.dim + 5) * (1 + np.sin(np.sum(x_norm**2)))
        noise_amp = 0.1 / (1 + self.dim)
        noise = noise_amp * np.random.random() * np.sin(noise_freq * np.pi * np.sum(x_norm**2))
        
        # Dimensionality scaling factor with fractal properties
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) / (1 + np.abs(np.log(self.dim + 1)))
        
        return scale_factor * (1.5 * spiral_basin + 1.0 * chaotic_mod + 0.8 * cross_interaction + 0.6 * fractal_basin + noise)