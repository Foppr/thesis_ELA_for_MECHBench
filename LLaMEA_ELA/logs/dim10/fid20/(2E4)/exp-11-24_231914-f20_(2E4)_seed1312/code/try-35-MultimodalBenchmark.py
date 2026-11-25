import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Periodic multimodal term with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(20 * np.pi * x[i]) ** 2 + 0.5 * np.cos(10 * np.pi * x[i]) ** 2
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**6 + 0.3 * (x[i] + x[i+1])**4
        
        # Add cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            cubic_interaction += (x[i] - x[i+2])**6 + 0.2 * (x[i] + x[i+2])**3
        
        # Add quartic interaction terms for even higher complexity
        quartic_interaction = 0.0
        for i in range(self.dim - 3):
            quartic_interaction += (x[i] - x[i+3])**8
        
        # Add chaotic component using logistic map with varying parameter for enhanced complexity
        chaotic = 0.0
        r_values = [3.95, 3.85, 3.75, 3.65]
        for i in range(self.dim):
            r = r_values[i % len(r_values)]
            if i == 0:
                chaotic += np.sin(r * x[i] * (1 - x[i])) ** 2
            else:
                chaotic += np.sin(r * x[i-1] * (1 - x[i-1])) ** 2
        
        # Add a dynamic shift based on sine and cosine functions for global minimum
        shift = 0.0
        for i in range(self.dim):
            shift += 0.5 * np.sin(5 * x[i]) + 0.3 * np.cos(7 * x[i])
        
        # Add a chaotic sine wave component with varying frequency and amplitude
        chaotic_sine = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * np.pi / self.dim)
            amp = 0.5 + 0.3 * np.cos(i * np.pi / self.dim)
            chaotic_sine += amp * np.sin(freq * x[i]) ** 3
        
        # Add a hyperbolic tangent component for additional non-linearity
        tanh_component = 0.0
        for i in range(self.dim):
            tanh_component += np.tanh(2 * x[i]) ** 4
        
        # Combine all terms to create challenging landscape
        return quadratic + 0.4 * periodic + 0.2 * interaction + 0.1 * cubic_interaction + 0.05 * quartic_interaction + 0.25 * chaotic + shift + 0.1 * chaotic_sine + 0.05 * tanh_component