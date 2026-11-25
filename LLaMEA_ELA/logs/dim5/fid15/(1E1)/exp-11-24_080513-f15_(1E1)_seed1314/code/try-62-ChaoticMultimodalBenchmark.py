import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic global basin with dimension-dependent scaling
        quadratic = np.sum(x_normalized**2) * (1.0 + 0.1 * self.dim)
        
        # Multi-scale chaotic sinusoidal components with fractal-like frequency patterns
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1) + 0.5 * np.sin(i * 0.7)
            amp = 0.3 + 0.7 * np.cos(i * 0.9)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Multi-modal radial basis functions with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            width = 0.1 + 0.3 * np.sin(i * 0.5)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * (1.0 + 0.2 * np.sin(i * 0.4))
        
        # Enhanced cross-dimensional interaction with exponential coupling and multiple interaction types
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(5 * (x_normalized[i] + x_normalized[j]))
                coupling2 = np.cos(3 * (x_normalized[i] - x_normalized[j]))
                cross += (coupling1 * coupling2) * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Higher-order non-separable polynomial interaction with variable exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent = 3 + int((i + j) % 4)
                poly_interaction += (x_normalized[i] * x_normalized[j])**exponent
        
        # Fractal-like noise using multiple chaotic maps with varying parameters
        noise = 0.0
        r1, r2, r3 = 3.9, 3.85, 3.7
        x_prev1, x_prev2, x_prev3 = 0.5, 0.3, 0.7
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            x_prev3 = r3 * x_prev3 * (1 - x_prev3)
            noise += (np.sin(x_prev1 * 15 * np.pi * x_normalized[i]) + 
                     np.cos(x_prev2 * 10 * np.pi * x_normalized[i]) * 
                     np.sin(x_prev3 * 8 * np.pi * x_normalized[i])) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Additional high-order coupling between all dimensions with fractal characteristics
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.sin(5 * (x_normalized[i] - x_normalized[j])) * np.cos(4 * (x_normalized[i] + x_normalized[j]))
                    additional_coupling += coupling * (x_normalized[i]**4 + x_normalized[j]**4) * np.exp(-0.1 * (x_normalized[i] - x_normalized[j])**2)
        
        # Add a complex multi-peak component with irregular spacing and varying heights
        multi_peak = 0.0
        for i in range(self.dim):
            peak_positions = [0.3, -0.4, 0.7, -0.8, 0.1]
            for pos in peak_positions:
                multi_peak += np.exp(-0.5 * ((x_normalized[i] - pos) / 0.2)**2) * (1.0 + 0.3 * np.sin(i * 0.6))
        
        # Combine all components with modified weights and add a dimensionality-dependent penalty
        return (0.3 * quadratic + 
                0.4 * chaotic + 
                0.2 * radial + 
                0.15 * cross + 
                0.08 * poly_interaction + 
                0.05 * noise + 
                0.05 * additional_coupling + 
                0.02 * multi_peak + 
                0.05 * self.dim * np.mean(x_normalized**4))