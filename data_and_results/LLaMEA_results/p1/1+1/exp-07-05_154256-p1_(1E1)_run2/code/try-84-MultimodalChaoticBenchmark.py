import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 1.5
        self.c4 = 0.8
        self.c5 = 3.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_poly = self.c1 * r**4 + self.c2 * r**2
        
        # Chaotic sine-cosine interaction terms
        chaotic_terms = 0
        for i in range(self.dim):
            chaotic_terms += np.sin(self.c3 * x[i]) * np.cos(self.c4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j]) * np.sin(self.c5 * (x[i]**2 + x[j]**2))
        
        # Additional multimodal component with polynomial and trigonometric mixing
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**6 - 15*x[i]**4 + 75*x[i]**2 - 125) * np.cos(0.5 * x[i])
        
        # Combine all components
        result = radial_poly + 0.5 * chaotic_terms + 0.3 * coupling + 0.2 * multimodal
        
        # Add a global scaling factor to ensure proper fitness range
        return result * (1.0 + 0.1 * np.sin(r))