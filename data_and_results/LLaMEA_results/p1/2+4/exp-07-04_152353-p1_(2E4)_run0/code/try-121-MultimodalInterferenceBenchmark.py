import numpy as np

class MultimodalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multimodal component with sinusoidal interference
        modal = 0
        for i in range(self.dim):
            # Sinusoidal interference patterns with varying frequencies
            freq = 2.0 + 0.5 * np.sin(i * 0.5)
            modal += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7)
        
        # Radial basis function component with varying centers and widths
        radial = 0
        for i in range(self.dim):
            # Asymmetric radial basis functions
            center = np.sin(i * 0.3) * 0.8
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            radial += np.exp(-width * (x_normalized[i] - center)**2)
        
        # Asymmetric gradient field component
        gradient = 0
        for i in range(self.dim):
            # Different exponents and asymmetry factors
            asymmetry = 1.0 + 0.3 * np.sin(i * 0.6)
            if x_normalized[i] >= 0:
                gradient += asymmetry * x_normalized[i]**2.5
            else:
                gradient += x_normalized[i]**1.8
            
        # Cross-term interference patterns
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupled sinusoidal interactions
                cross += np.sin(x_normalized[i] * x_normalized[j] * 3.0) * np.cos(x_normalized[i] + x_normalized[j])
        
        # Combine all components with modified weights
        result = 0.3 * f1 + 0.25 * modal + 0.2 * radial + 0.15 * gradient + 0.1 * cross
        
        # Add noise term to increase problem difficulty
        noise = 0.02 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 7))
        result += noise
        
        return result