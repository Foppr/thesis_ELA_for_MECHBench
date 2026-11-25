import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic global basin
        quadratic = np.sum(x_normalized**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1)
            amp = 0.3 + 0.7 * np.sin(i * 0.9)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Radial basis function components with varying centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.3 * np.sin(i * 0.7)
            width = 0.2 + 0.15 * np.cos(i * 0.5)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional interaction terms with enhanced coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(3 * (x_normalized[i] + x_normalized[j]))
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Non-separable polynomial interaction with higher degree terms
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_normalized[i] * x_normalized[j])**5
        
        # Add noise-like perturbation using a chaotic logistic map with different parameters
        noise = 0.0
        r = 3.9
        x_prev = 0.6
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            noise += np.sin(x_prev * 10 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Add additional coupling between all dimensions
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    additional_coupling += np.sin(4 * (x_normalized[i] - x_normalized[j])) * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Combine all components with carefully tuned weights
        return 0.3 * quadratic + 0.3 * chaotic + 0.2 * radial + 0.1 * cross + 0.04 * poly_interaction + 0.06 * noise + 0.05 * additional_coupling