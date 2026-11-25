import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Adaptive conditioning with chaotic modulation
        condition = np.ones(self.dim)
        for i in range(self.dim):
            condition[i] = 1.0 + 0.5 * np.sin(7.0 * x_scaled[i]) * np.cos(4.0 * x_scaled[i])
        
        # Quadratic base with adaptive conditioning
        quadratic = np.sum(condition * x_scaled**2)
        
        # Chaotic gradient field with periodic attractors
        gradient_field = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(3.0 * x_scaled[i])
            amp = 1.0 + 0.3 * np.cos(5.0 * x_scaled[i])
            gradient_field += amp * np.sin(freq * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Dynamic harmonic coupling between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                coupling += np.sin(10.0 * dist) * np.cos(8.0 * dist) * np.exp(-dist**2)
        
        # Multi-scale periodic landscape with dynamic amplitude
        periodic = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.2 * np.sin(6.0 * x_scaled[i])
            freq = 3.0 + 2.0 * np.cos(4.0 * x_scaled[i])
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        
        # Adaptive radial component with chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_mod = 1.0 + 0.4 * np.sin(12.0 * r) * np.cos(8.0 * r)
        radial = radial_mod * np.exp(-r**2 / 2.0)
        
        # Cross-dimensional chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction = np.sin(5.0 * (x_scaled[i] + x_scaled[j])) * np.cos(3.0 * (x_scaled[i] - x_scaled[j]))
                    cross_term += interaction / (1.0 + 0.1 * np.abs(x_scaled[i] - x_scaled[j]))
        
        # Combine all components with dynamic weights
        result = quadratic + 0.5 * gradient_field + 0.3 * coupling + 0.4 * periodic + 0.2 * radial + 0.6 * cross_term
        
        # Add chaotic noise for increased complexity
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result