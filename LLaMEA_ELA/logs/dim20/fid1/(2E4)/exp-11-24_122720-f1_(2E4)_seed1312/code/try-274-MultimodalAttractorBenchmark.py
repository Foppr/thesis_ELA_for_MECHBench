import numpy as np

class MultimodalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic attractors and dynamic structures
        self.attractor_freq = [3.0 + 2.0 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.valley_asymmetry = [0.7 * np.cos(i * np.pi / (dim + 3)) for i in range(dim)]
        self.coupling_strength = 0.2 + 0.1 * np.sin(dim * np.pi / 8)
        self.chaos_factor = 1.5 + 0.5 * np.cos(dim * np.pi / 5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal component with dynamic attractors
        multimodal = 0
        for i in range(self.dim):
            freq = self.attractor_freq[i]
            asym = self.valley_asymmetry[i]
            # Chaotic attractor potential with exponential modulation
            attractor = np.sin(freq * x[i]) * np.exp(-0.1 * abs(x[i])) + 0.3 * np.sin(2 * freq * x[i])
            valley = asym * x[i]**4
            multimodal += attractor + valley
            
        # Dynamic valley structure with cross-dimensional coupling
        valley_structure = 0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            # Dynamic quadratic valley with time-like modulation
            valley = scale * (x[i]**2 - 2 * x[i] + 1) * np.cos(0.5 * x[i])
            # Add dynamic asymmetry through cosine modulation
            asym_term = 0.4 * np.cos(x[i]) * scale * np.sin(0.3 * i)
            valley_structure += valley + asym_term
            
        # Cross-dimensional coupling with chaotic perturbations
        coupling_perturbation = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strength * np.sin(x[i] * x[j]) * (i + j)
                coupling_perturbation += coupling
                
        # Chaos-like noise with dynamic scaling
        chaos_noise = 0
        for i in range(self.dim):
            chaos_noise += self.chaos_factor * np.sin(x[i] * (i + 1) * np.pi / 3) * np.cos(x[i] * (i + 2) * np.pi / 4)
            
        # Combine components with proper weighting
        result = 2.5 * multimodal + 1.8 * valley_structure + coupling_perturbation + chaos_noise
        
        # Add global scaling factor based on dimensionality and chaos
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * self.chaos_factor
        result *= scale_factor
        
        return result