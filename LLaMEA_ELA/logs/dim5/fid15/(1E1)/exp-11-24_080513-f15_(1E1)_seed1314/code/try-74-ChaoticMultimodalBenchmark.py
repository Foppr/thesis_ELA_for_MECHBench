import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic global basin with dimension-dependent scaling
        quadratic = np.sum(x_normalized**2) * (1.0 + 0.1 * np.sin(self.dim * 0.5))
        
        # Highly chaotic sinusoidal components with fractional frequencies and dynamic amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 7 + 1) * (1.0 + 0.3 * np.cos(i * 0.7))
            amp = 0.5 + 0.5 * np.sin(i * 0.9) * np.cos(i * 0.4)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Multi-scale radial basis function components with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            width = 0.2 + 0.15 * np.sin(i * 0.5)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * (1.0 + 0.2 * np.cos(i * 0.3))
        
        # Advanced cross-dimensional interaction terms with variable coupling strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin((i + j) * 0.3)
                coupling = np.sin(4 * (x_normalized[i] + x_normalized[j])) * coupling_strength
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Higher-order non-separable polynomial interaction with dynamic exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent = 3 + int(np.sin(i * 0.6) * 2)
                poly_interaction += (x_normalized[i] * x_normalized[j])**exponent
        
        # Complex noise-like perturbation using multiple chaotic maps with varying parameters
        noise = 0.0
        r1, r2 = 3.8, 3.9
        x_prev1, x_prev2 = 0.5, 0.3
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            noise += np.sin(x_prev1 * 15 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2) + \
                     np.cos(x_prev2 * 10 * np.pi * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
        
        # Novel coupling mechanism with all dimensions interacting through a hyperbolic tangent function
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.tanh(2 * (x_normalized[i] - x_normalized[j]))
                    additional_coupling += coupling * (x_normalized[i]**4 + x_normalized[j]**4) * np.exp(-0.1 * (x_normalized[i] + x_normalized[j])**2)
        
        # Add a new component: fractal-like landscape with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = 0.3 + 0.7 * np.sin(i * 0.5)
            fractal += scale * np.sin(8 * x_normalized[i]) * np.cos(4 * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
        
        # Combine all components with new weights and add a dimension-dependent penalty
        penalty = 0.1 * self.dim * np.sum(np.abs(x_normalized)**3)
        return (0.3 * quadratic + 0.25 * chaotic + 0.2 * radial + 0.1 * cross + 
                0.08 * poly_interaction + 0.07 * noise + 0.05 * additional_coupling + 
                0.05 * fractal + penalty)