import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Sinusoidal components with adaptive frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 0.3 + 0.7 * np.cos(i * 0.5)
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Polynomial interaction terms with varying degrees
        polynomial = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                polynomial += (x_normalized[i] * x_normalized[j])**3
        
        # Radial basis functions with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.7)
            width = 0.2 + 0.3 * np.cos(i * 0.3)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional coupling with exponentially decaying weights
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                cross += weight * np.sin(3 * (x_normalized[i] - x_normalized[j])) * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Adaptive noise component using a chaotic system
        noise = 0.0
        r = 3.9
        x_prev = 0.3
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            noise += np.sin(x_prev * 8 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Combine components with dimensionality-dependent weights
        weights = [0.3, 0.25, 0.2, 0.15, 0.1]
        components = [sinusoidal, polynomial, radial, cross, noise]
        result = sum(w * comp for w, comp in zip(weights[:len(components)], components))
        
        # Add a global quadratic basin
        quadratic = 0.1 * np.sum(x_normalized**2)
        
        return result + quadratic