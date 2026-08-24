import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Enhanced exponential terms with chaotic coupling and multi-scale modulation
        for i in range(self.dim):
            # Base exponential term with variable scaling
            result += 0.35 * (np.exp(0.4 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with varying amplitudes
            result += 0.5 * (np.sin(2.5 * np.pi * x[i]) + 
                            0.4 * np.sin(6.0 * np.pi * x[i]) + 
                            0.2 * np.sin(9.0 * np.pi * x[i]))
            
            # Chaotic coupling with stronger and more complex phase relationships
            if i < self.dim - 1:
                coupling_strength = 0.4 * np.exp(-0.03 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(3.0 * (x[i] - x[i+1]) + 0.7 * np.cos(x[i]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.2 * x[i]**3 * np.cos(0.4 * x[i]) + 0.08 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 4 + int(4 * np.sin(i * 0.5))
            sign = (-1)**(i % 4)
            result += 0.1 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.08 * distance**2) * np.sin(0.6 * (x[i] + x[j]) + 0.3 * distance)
                result += 0.2 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.03 * np.sum(np.abs(x)**1.8) + 0.015 * np.sum(np.sin(12.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.12 * x[i]**2)
        result += 0.15 * chaotic_component
        
        return result