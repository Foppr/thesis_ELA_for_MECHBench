import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic global basin with adaptive weights
        quadratic = np.sum(x_normalized**2) * (1.0 + 0.1 * np.sin(self.dim * 0.5))
        
        # Chaotic sinusoidal components with higher frequency variations and dynamic amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 2)
            amp = 0.3 + 0.7 * np.sin(i * 0.9) * np.cos(i * 0.3)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Enhanced radial basis function components with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            width = 0.2 + 0.3 * np.sin(i * 0.5)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * (1.0 + 0.2 * np.cos(i * 0.8))
        
        # Stronger cross-dimensional interaction terms with multi-scale coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5 * (x_normalized[i] + x_normalized[j])) * np.cos(3 * (x_normalized[i] - x_normalized[j]))
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Higher-degree non-separable polynomial interaction
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_normalized[i] * x_normalized[j])**5
        
        # Enhanced noise-like perturbation using multiple chaotic maps
        noise = 0.0
        r1, r2 = 3.9, 3.7
        x_prev1, x_prev2 = 0.4, 0.6
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            noise += np.sin(x_prev1 * 15 * np.pi * x_normalized[i]) * np.cos(x_prev2 * 10 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Additional strong coupling between all dimensions with cubic interaction
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    additional_coupling += np.sin(4 * (x_normalized[i] - x_normalized[j])) * (x_normalized[i]**4 + x_normalized[j]**4) * np.exp(-0.1 * (x_normalized[i] + x_normalized[j])**2)
        
        # Add a new component: periodic wave interference pattern
        wave_pattern = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                wave_pattern += np.sin(6 * (x_normalized[i] + x_normalized[j])) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Combine all components with new weights
        return 0.3 * quadratic + 0.25 * chaotic + 0.2 * radial + 0.15 * cross + 0.08 * poly_interaction + 0.07 * noise + 0.05 * additional_coupling + 0.05 * wave_pattern