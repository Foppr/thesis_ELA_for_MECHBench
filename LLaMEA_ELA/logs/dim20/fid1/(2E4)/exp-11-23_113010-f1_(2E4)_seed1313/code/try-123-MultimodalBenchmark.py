import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced logarithmic spiral with modified scaling factors
        spiral_basin = np.sum(np.log(np.abs(x_norm) + 1e-8) * 
                             np.cos(np.log(np.abs(x_norm) + 1e-8)) * 
                             np.sin(2 * np.pi * x_norm))
        
        # Improved chaotic cosine modulations with frequency coupling
        chaotic_mod = np.sum(np.cos(2**(self.dim + 1) * np.pi * x_norm) * 
                            np.cos(3**(self.dim + 2) * np.pi * x_norm**2) * 
                            np.cos(5**(self.dim + 3) * np.pi * x_norm**3) * 
                            np.sin(np.pi * self.dim * x_norm))
        
        # Enhanced cross-dimensional interactions with adaptive coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified fractal coupling coefficient with different exponents and interaction strength
                coupling_coef = (i + 2) ** (-j - 2) * (j + 2) ** (-i - 2) * np.sin(np.pi * (i + j) / (self.dim + 1))
                cross_interaction += coupling_coef * (x_norm[i]**3 + x_norm[j]**3) * np.sin(2**(i+j+2) * np.pi * (x_norm[i] - x_norm[j]))
        
        # Refined multi-scale fractal basin with dynamic exponents
        fractal_basin = np.sum(np.abs(x_norm)**(1.7 + 0.3 * np.sin(self.dim * np.pi * x_norm)) + 
                              0.2 * np.abs(x_norm)**(2.2 + 0.5 * np.cos(self.dim * np.pi * x_norm)) + 
                              0.15 * np.abs(x_norm)**(1.2 + 0.4 * np.sin(2 * self.dim * np.pi * x_norm)))
        
        # Enhanced high-frequency chaotic noise with improved distribution
        noise_freq = 2**(self.dim + 6) * (1 + np.sin(np.sum(x_norm**2)))
        noise_amp = 0.12 / (1 + self.dim)
        noise = noise_amp * np.random.random() * np.sin(noise_freq * np.pi * np.sum(x_norm**2)) * np.cos(np.pi * np.sum(x_norm))
        
        # Dimensionality scaling factor with improved fractal properties
        scale_factor = 1.0 + 0.25 * np.log(self.dim + 1) / (1 + np.abs(np.log(self.dim + 1))) + 0.06 * np.sin(np.pi * self.dim / 3)
        
        # Combine all components with adjusted weights for better optimization behavior
        return scale_factor * (1.2 * spiral_basin + 1.3 * chaotic_mod + 0.8 * cross_interaction + 0.8 * fractal_basin + noise)