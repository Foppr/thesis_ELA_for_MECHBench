import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute some constants for performance
        self.constants = np.array([np.sin(i * 0.7) * np.cos(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Base quadratic term with dynamic curvature
        quadratic = np.sum(x_norm**2)
        
        # Add multi-modal potential with asymmetric basins
        modal_potential = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric basin terms with varying depths
            basin1 = (xi - 0.3)**2 * (1 + 0.5 * np.sin(3 * xi))
            basin2 = (xi + 0.4)**2 * (1 + 0.3 * np.cos(2 * xi))
            basin3 = xi**4 * (1 + 0.2 * np.sin(5 * xi))
            modal_potential += 0.5 * (basin1 + basin2 + basin3)
        
        # Introduce time-variant periodic forcing
        time_forcing = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic frequency modulation based on dimension
            freq = 2 + 0.5 * np.sin(i * 0.3) + 0.3 * np.cos(i * 0.4)
            time_forcing += np.sin(freq * xi + i * 0.1) * np.cos(freq * xi - i * 0.2)
        
        # Add non-linear coupling between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional interaction with dynamic strength
                strength = 0.3 + 0.2 * np.sin((i + j) * 0.2)
                coupling += strength * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Introduce chaotic resonance terms
        chaos = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chaotic modulation with multiple frequencies
            chaos += 0.1 * np.sin(13 * xi + 2.7 * i) * np.cos(7 * xi - 1.3 * i) + \
                     0.08 * np.sin(17 * xi + 3.1 * i) + \
                     0.06 * np.sin(23 * xi + 4.2 * i)
        
        # Add fractal interference patterns
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            fractal += 0.05 * np.sin(5 * xi + 0.2 * i) * np.cos(3 * xi - 0.1 * i) + \
                       0.03 * np.sin(7 * xi + 0.3 * i)
        
        # Add multi-scale interference patterns
        multiscale = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            multiscale += 0.04 * np.sin(11 * xi + 0.1 * i) * np.cos(9 * xi - 0.2 * i) * \
                          np.sin(5 * xi**3 + 0.1 * i)
        
        # Add adaptive dimensionality scaling
        dim_scaling = 1.0 + 0.1 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4)
        
        # Combine all components with appropriate weights
        total = quadratic + modal_potential + time_forcing + coupling + chaos + fractal + multiscale
        
        # Apply final transformation to create complex landscape
        result = (total**2) * dim_scaling
        
        return result