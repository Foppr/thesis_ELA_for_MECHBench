import numpy as np

class ChaoticSinusoidalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define the central attractor point
        self.attractor = np.ones(dim) * 2.5
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = (x - (-5.0)) / (5.0 - (-5.0)) * 2.0 - 1.0
        
        # Chaotic sinusoidal term with nested frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i + 1)
            chaotic_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Central attractor term pulling solutions towards the center
        attractor_distance = np.linalg.norm(x - self.attractor)
        attractor_term = 0.5 * attractor_distance ** 2
        
        # Add a multi-modal component with varying amplitudes
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(3 * x[i]) + np.cos(2 * x[i])) * (i + 1)
        
        # Combine all terms with a scaling factor to control difficulty
        total = 2.0 * chaotic_term + attractor_term + 0.3 * multimodal_term
        
        return total