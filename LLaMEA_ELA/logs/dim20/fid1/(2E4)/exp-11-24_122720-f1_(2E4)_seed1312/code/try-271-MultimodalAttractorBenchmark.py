import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize periodic attractor parameters with slight modifications
        self.attractor_freq = [1.0 + 0.6 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.valley_asymmetry = [0.4 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.noise_scale = [0.15 * (1 + 0.3 * np.sin(i * np.pi / (dim + 3))) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multimodal component with periodic attractors
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            asym = self.valley_asymmetry[i]
            noise = self.noise_scale[i]
            # Create periodic valleys with asymmetric basins
            valley = np.cos(freq * x[i]) + asym * np.sin(2 * freq * x[i])
            multimodal += valley * (x[i]**2 + 1) + noise * np.random.normal()
            
        # Enhanced asymmetric valley structure with cross-dimensional interactions
        valley_structure = 0
        for i in range(self.dim):
            asym_factor = 1.0 + self.valley_asymmetry[i] * np.sin(x[i])
            # Add interaction term between dimensions
            interaction = 0
            for j in range(self.dim):
                if i != j:
                    interaction += 0.1 * np.sin(x[i] - x[j]) * (1 + 0.1 * np.cos(i * j))
            valley_structure += ((x[i]**2 - 2 * x[i]) * asym_factor + interaction)
            
        # Embedded periodic noise for increased complexity
        periodic_noise = 0
        for i in range(self.dim):
            periodic_noise += np.sin(self.attractor_freq[i] * x[i] + i) * np.cos(x[i])
            
        # Dimensionally scaled scaling factor with additional nonlinearity
        scale_factor = 1.0 + 0.25 * np.log(self.dim + 1) + 0.15 * np.sin(self.dim * np.pi / 6) + 0.05 * np.cos(self.dim * np.pi / 4)
        
        # Combine all components
        result = scale_factor * (multimodal + valley_structure + periodic_noise)
        
        return result