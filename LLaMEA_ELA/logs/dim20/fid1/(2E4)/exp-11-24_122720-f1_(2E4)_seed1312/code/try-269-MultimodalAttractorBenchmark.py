import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for periodic attractors and asymmetric structures
        self.attractor_freq = [2.0 + 1.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.valley_asymmetry = [0.5 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.noise_scale = 0.1 + 0.05 * np.sin(dim * np.pi / 6)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multimodal component with periodic attractors
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            asym = self.valley_asymmetry[i]
            # Attractor potential with asymmetric valleys
            attractor = np.sin(freq * x[i]) * np.cos(x[i])
            valley = asym * x[i]**3
            multimodal += attractor + valley
            
        # Asymmetric valley structure with dimensionally scaled features
        valley_structure = 0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            # Asymmetric quadratic valley
            valley = scale * (x[i]**2 - 2 * x[i] + 1)
            # Add asymmetry through sine modulation
            asym_term = 0.3 * np.sin(x[i]) * scale
            valley_structure += valley + asym_term
            
        # Noise-like perturbation scaled by dimensionality
        noise_perturbation = self.noise_scale * np.sum([
            np.sin(x[i] * (i + 1) * np.pi / 4) + 
            0.1 * np.cos(x[i] * (i + 1) * np.pi / 3) 
            for i in range(self.dim)
        ])
        
        # Combine components with proper weighting
        result = 2.0 * multimodal + 1.5 * valley_structure + noise_perturbation
        
        # Add global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= scale_factor
        
        return result