import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic global basin with dimension-dependent scaling
        quadratic = np.sum(x_normalized**2) * (1.0 + 0.1 * np.sin(self.dim * 0.5))
        
        # Chaotic sinusoidal components with fractional frequencies and dynamic amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 7 + 1) * (1.0 + 0.3 * np.cos(i * 0.7))
            amp = 0.3 + 0.7 * np.sin(i * 0.9 + self.dim * 0.2)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Multi-scale radial basis function components with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.7 + self.dim * 0.3)
            width = 0.1 + 0.3 * np.cos(i * 0.5 + self.dim * 0.4)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * (1.0 + 0.2 * np.sin(i * 0.6))
        
        # Enhanced cross-dimensional interaction terms with non-linear coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5 * (x_normalized[i] + x_normalized[j])) * np.cos(3 * (x_normalized[i] - x_normalized[j]))
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Higher-order non-separable polynomial interaction with dynamic exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_factor = 1 + 0.5 * np.sin(i * 0.4 + j * 0.3)
                poly_interaction += (x_normalized[i] * x_normalized[j])**(3 + exp_factor)
        
        # Advanced noise-like perturbation using a multi-chaotic map with time-varying parameters
        noise = 0.0
        r1, r2 = 3.8 + 0.1 * np.sin(self.dim * 0.3), 3.9 + 0.1 * np.cos(self.dim * 0.4)
        x_prev1, x_prev2 = 0.5, 0.6
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            noise += np.sin(x_prev1 * 15 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2) + \
                     np.cos(x_prev2 * 10 * np.pi * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**3)
        
        # Additional high-order coupling between all dimensions with exponential decay
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.sin(4 * (x_normalized[i] - x_normalized[j])) * np.cos(2 * (x_normalized[i] + x_normalized[j]))
                    decay = np.exp(-0.1 * abs(i - j))
                    additional_coupling += coupling * (x_normalized[i]**4 + x_normalized[j]**4) * decay
        
        # Novel fractal-like component with recursive structure
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_normalized[i] - x_normalized[j])
                fractal += np.sin(20 * dist) * np.exp(-5 * dist**2)
        
        # Combine all components with adaptive weights based on dimensionality
        weight_quad = 0.3 + 0.05 * np.sin(self.dim * 0.2)
        weight_chaotic = 0.4 + 0.05 * np.cos(self.dim * 0.3)
        weight_radial = 0.2 + 0.03 * np.sin(self.dim * 0.4)
        weight_cross = 0.1 + 0.02 * np.cos(self.dim * 0.5)
        weight_poly = 0.08 + 0.02 * np.sin(self.dim * 0.6)
        weight_noise = 0.07 + 0.01 * np.cos(self.dim * 0.7)
        weight_additional = 0.05 + 0.01 * np.sin(self.dim * 0.8)
        weight_fractal = 0.03 + 0.01 * np.cos(self.dim * 0.9)
        
        return (weight_quad * quadratic + 
                weight_chaotic * chaotic + 
                weight_radial * radial + 
                weight_cross * cross + 
                weight_poly * poly_interaction + 
                weight_noise * noise + 
                weight_additional * additional_coupling + 
                weight_fractal * fractal)