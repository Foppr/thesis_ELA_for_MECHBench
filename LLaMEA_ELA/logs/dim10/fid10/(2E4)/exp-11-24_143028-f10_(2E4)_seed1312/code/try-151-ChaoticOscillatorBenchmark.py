import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.tent_map_a = 3.9
        self.oscillator_freq = 2.0 * np.pi
        self.gradient_strength = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_result = 0.0
        for i in range(self.dim):
            # Apply tent map dynamics
            xi = x[i]
            for _ in range(3):  # Iterate tent map 3 times for chaos
                if xi < 0.5:
                    xi = self.tent_map_a * xi
                else:
                    xi = self.tent_map_a * (1 - xi)
            tent_result += 0.5 * xi**2 + 0.3 * np.sin(5 * xi) + 0.2 * np.cos(3 * xi)
        
        # Harmonic oscillator component with adaptive frequencies
        harmonic_result = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freq * (1 + 0.2 * np.sin(x[i]))
            harmonic_result += 0.8 * np.sin(freq * x[i])**2 + 0.6 * np.cos(freq * x[i])**2
        
        # Cross-dimensional gradient fields with adaptive weights
        gradient_result = 0.0
        for i in range(self.dim):
            grad_weight = 1.0 + 0.5 * np.sin(x[i])
            for j in range(i+1, self.dim):
                dist = (x[i] - x[j])**2
                gradient_result += self.gradient_strength * grad_weight * np.exp(-dist/2.0) * np.sin(2 * (x[i] + x[j]))
        
        # Multi-scale fractal-like interference patterns
        fractal_result = 0.0
        for i in range(self.dim):
            fractal_result += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric boundary penalties with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_penalty += 1.2 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.4 * np.sin(8 * x[i]))
            else:
                boundary_penalty += 0.9 * np.exp(-0.2 * (x[i] - 5.0)**2) * (1 + 0.3 * np.cos(6 * x[i]))
        
        # Coupled sine-cosine components with time-varying coupling
        coupling_result = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.8 + 0.2 * np.sin(x[i] + x[j])
                coupling_result += coupling_strength * np.sin(3 * x[i]) * np.cos(2 * x[j])
        
        # Polynomial conditioning with chaotic modulation
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1 + 0.3 * x[i]**3 * np.sin(4 * x[i]))
        polynomial_result = 1.1 * condition_factor
        
        # Final combined function value
        result = tent_result + harmonic_result + gradient_result + fractal_result + boundary_penalty + coupling_result + polynomial_result
        
        return result