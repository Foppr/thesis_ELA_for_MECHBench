import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic attractor parameters with fractal scaling
        self.attractor_freq = [2.0 + 2.0 * np.sin(i * np.pi / (dim + 1)) + 0.5 * np.cos(i * np.pi / (dim + 3)) for i in range(dim)]
        self.valley_fractal = [0.3 * np.sin(i * np.pi / (dim + 2)) + 0.2 * np.cos(i * np.pi / (dim + 4)) for i in range(dim)]
        self.noise_scale = 0.15 + 0.08 * np.sin(dim * np.pi / 8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal component with fractal valley interactions
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            fractal = self.valley_fractal[i]
            # Chaotic attractor potential with fractal modulation
            attractor = np.sin(freq * x[i]) * np.cos(x[i] * (1 + 0.1 * np.sin(x[i])))
            fractal_valley = fractal * np.sin(x[i]**3) * np.cos(x[i])
            multimodal += attractor + fractal_valley
            
        # Fractal valley structure with adaptive scaling
        valley_structure = 0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            # Fractal quadratic valley with chaotic modulation
            valley = scale * (x[i]**2 - 2 * x[i] + 1) * (1 + 0.2 * np.sin(x[i] * (i + 1)))
            # Add fractal asymmetry through higher-order sine modulation
            asym_term = 0.4 * np.sin(x[i] * scale * np.pi) * np.cos(x[i] * scale * np.pi / 2)
            valley_structure += valley + asym_term
            
        # Adaptive noise perturbation with chaotic scaling
        noise_perturbation = self.noise_scale * np.sum([
            np.sin(x[i] * (i + 1) * np.pi / 3) * np.cos(x[i] * (i + 1) * np.pi / 5) + 
            0.15 * np.cos(x[i] * (i + 1) * np.pi / 4) * np.sin(x[i] * (i + 1) * np.pi / 6)
            for i in range(self.dim)
        ])
        
        # Combine components with chaotic weighting
        result = 2.5 * multimodal + 1.8 * valley_structure + noise_perturbation
        
        # Add fractal scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        result *= scale_factor
        
        return result