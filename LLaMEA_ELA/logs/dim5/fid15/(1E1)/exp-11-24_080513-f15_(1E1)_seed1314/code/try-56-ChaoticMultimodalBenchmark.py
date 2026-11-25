import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic global basin with variable conditioning
        quadratic = np.sum(x_normalized**2) * (1 + 0.1 * np.sin(np.sum(x_normalized**2)))
        
        # Enhanced chaotic sinusoidal components with fractional frequencies and dynamic amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 7 + 1) + 0.5 * np.cos(i * 0.7)
            amp = 0.3 + 0.7 * np.sin(i * 0.9 + np.sum(x_normalized[:i%3+1]) if i%3+1 > 0 else 1)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Multi-scale radial basis function with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.3 * np.sin(i * 0.5 + np.sum(x_normalized[:i%4+1]) if i%4+1 > 0 else 1)
            width = 0.1 + 0.3 * np.cos(i * 0.6 + np.sum(x_normalized[:i%2+1]) if i%2+1 > 0 else 1)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional interaction with trigonometric coupling and variable strength
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin(3 * (x_normalized[i] + x_normalized[j]))
                cross += coupling_strength * np.sin(5 * (x_normalized[i] + x_normalized[j])) * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Non-separable polynomial interaction with higher degree and dynamic coefficients
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.5 + 0.5 * np.cos(i * 0.4 + j * 0.3)
                poly_interaction += coeff * (x_normalized[i] * x_normalized[j])**5
        
        # Noise-like perturbation using a coupled chaotic system
        noise = 0.0
        r1, r2 = 3.9, 3.7
        x_prev1, x_prev2 = 0.5, 0.3
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            noise += np.sin(x_prev1 * 10 * np.pi * x_normalized[i]) * np.sin(x_prev2 * 8 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Additional coupling with hyperbolic and exponential terms
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    additional_coupling += np.tanh(2 * (x_normalized[i] - x_normalized[j])) * (x_normalized[i]**4 + x_normalized[j]**4) * np.exp(-0.1 * (x_normalized[i] + x_normalized[j])**2)
        
        # Add a novel component with fractal-like behavior
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(10 * np.pi * x_normalized[i]) * np.cos(15 * np.pi * x_normalized[i]) * np.exp(-0.3 * np.abs(x_normalized[i]))
        
        # Combine all components with carefully tuned weights and dynamic scaling
        return 0.2 * quadratic + 0.4 * chaotic + 0.2 * radial + 0.08 * cross + 0.06 * poly_interaction + 0.07 * noise + 0.05 * additional_coupling + 0.04 * fractal