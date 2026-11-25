import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with stronger chaos and dimensionality dependence
        self.r_values = 3.95 + 0.2 * np.sin(np.arange(dim) * np.pi / (dim + 1)) + 0.1 * np.cos(np.arange(dim) * np.pi / (dim * 2))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal component using self-similar cosine patterns at multiple scales with enhanced dimensionality
        fractal_sum = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                xi = x_scaled[i]
                # Multi-scale cosine pattern with varying frequencies and amplitude modulation
                freq = scale * (i + 1) * np.pi / (self.dim + 1)
                amp_mod = 1.0 + 0.3 * np.sin(scale * xi)
                fractal_sum += amp_mod * np.cos(freq * xi) * np.exp(-0.3 * (xi**2) / scale)
        
        # Chaotic component using logistic maps with dimension-dependent parameters and increased iterations
        chaotic_sum = 0.0
        x_logistic = 0.5 * np.ones(self.dim)
        for t in range(50):  # Increased iterations for stronger chaos
            for i in range(self.dim):
                r = self.r_values[i]
                x_logistic[i] = r * x_logistic[i] * (1 - x_logistic[i])
        
        for i in range(self.dim):
            chaotic_sum += x_logistic[i] * np.sin((i + 1) * np.pi * x_scaled[i]) * np.exp(-0.1 * (i + 1))
        
        # Cross-dimensional interaction with enhanced coupling strength and modified weighting
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                # Enhanced fractal distance weighting with polynomial scaling
                weight = 1.0 / (1 + 0.5 * dist**5)
                interaction += weight * np.sin(12 * (x_scaled[i] + x_scaled[j])) * np.exp(-0.2 * (i + j))
        
        # Multi-modal component with significantly altered amplitudes, frequencies, and added harmonic terms
        modal_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Multiple sine waves with different amplitudes, frequencies, and harmonic components
            modal_component += (0.8 * np.sin(17 * xi) + 0.4 * np.sin(31 * xi) + 
                              0.3 * np.sin(43 * xi) + 0.2 * np.sin(59 * xi) + 
                              0.1 * np.sin(71 * xi)) * np.exp(-0.15 * xi**2)
        
        # Additional valley-forming component with radial symmetry
        valley_component = 0.0
        center = np.zeros(self.dim)
        for i in range(self.dim):
            valley_component += (np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[i]) + 
                               0.5 * np.sin(7 * x_scaled[i])) * np.exp(-0.1 * (x_scaled[i] - center[i])**2)
        
        # Combine all components with adjusted weights and dimensionality factor
        dim_factor = 1.0 + 0.7 * np.log(self.dim + 1)
        return dim_factor * (0.35 * fractal_sum + 0.25 * chaotic_sum + 
                           0.35 * interaction + 0.45 * modal_component + 0.15 * valley_component)