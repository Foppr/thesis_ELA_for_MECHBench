import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic attractor parameters
        self.attractor_freq = [1.0 + 0.8 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.valley_asymmetry = [0.5 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.noise_scale = [0.2 * (1 + 0.3 * np.sin(i * np.pi / (dim + 3))) for i in range(dim)]
        # Add chaotic modulation parameters
        self.chaotic_params = [0.1 * np.sin(i * np.pi / (dim + 4)) for i in range(dim)]
        self.fractal_dim = 1.5 + 0.5 * np.cos(dim * np.pi / 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multimodal component with chaotic attractors
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            asym = self.valley_asymmetry[i]
            noise = self.noise_scale[i]
            chaotic_mod = self.chaotic_params[i] * np.sin(x[i]**3)
            # Create fractal-like valleys with chaotic modulation
            valley = np.cos(freq * x[i]) + asym * np.sin(2 * freq * x[i]) + chaotic_mod
            multimodal += valley * (x[i]**2 + 1) + noise * np.random.normal()
            
        # Fractal valley structure with dimensionally scaled features
        valley_structure = 0
        for i in range(self.dim):
            asym_factor = 1.0 + self.valley_asymmetry[i] * np.sin(x[i])
            fractal_term = np.sin(x[i]**self.fractal_dim) / (1 + x[i]**2)
            valley_structure += (x[i]**2 - 2 * x[i]) * asym_factor + fractal_term
            
        # Embedded chaotic noise for increased complexity
        chaotic_noise = 0
        for i in range(self.dim):
            chaotic_noise += np.sin(self.attractor_freq[i] * x[i] + i) * np.cos(x[i]**2) * np.exp(-x[i]**2/10)
            
        # Multi-scale scaling factor with fractal influence
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.15 * np.sin(self.dim * np.pi / 6) + 0.05 * np.cos(self.dim * np.pi / 4)
        
        # Combine all components
        result = scale_factor * (multimodal + valley_structure + chaotic_noise)
        
        return result