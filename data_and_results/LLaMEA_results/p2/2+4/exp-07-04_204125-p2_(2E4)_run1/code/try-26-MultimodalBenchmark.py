import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Exponential terms with chaotic coupling and multi-scale modulation
        for i in range(self.dim):
            # Base exponential term with variable scaling
            result += np.exp(0.3 * x[i]**2) - 1.0
            
            # Multi-frequency sinusoidal modulations
            result += 0.4 * (np.sin(2.0 * np.pi * x[i]) + 
                            0.5 * np.sin(5.0 * np.pi * x[i]) + 
                            0.3 * np.sin(8.0 * np.pi * x[i]))
            
            # Chaotic coupling with varying strength and phase
            if i < self.dim - 1:
                coupling_strength = 0.3 * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(2.0 * (x[i] - x[i+1]) + 0.5)
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with cubic and quartic components
            result += 0.15 * x[i]**3 * np.cos(0.3 * x[i]) + 0.05 * x[i]**4
            
            # Higher-order polynomial with random sign flips and variable exponents
            exponent = 5 + int(3 * np.sin(i))
            sign = (-1)**(i % 3)
            result += 0.08 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.1 * distance**2) * np.sin(0.5 * (x[i] + x[j]) + 0.2 * distance)
                result += 0.15 * coupling
        
        # Add non-smooth, non-convex perturbations with fractal-like characteristics
        result += 0.02 * np.sum(np.abs(x)**1.7) + 0.01 * np.sum(np.sin(10.0 * x))
        
        # Add a chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.1 * chaotic_component
        
        return result