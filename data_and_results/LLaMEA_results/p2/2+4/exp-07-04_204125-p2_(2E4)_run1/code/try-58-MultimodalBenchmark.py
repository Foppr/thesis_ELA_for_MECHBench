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
            result += 0.4 * (np.exp(0.5 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with varying amplitudes
            result += 0.6 * (np.sin(3.0 * np.pi * x[i]) + 
                            0.5 * np.sin(7.0 * np.pi * x[i]) + 
                            0.3 * np.sin(10.0 * np.pi * x[i]))
            
            # Chaotic coupling with stronger and more complex phase relationships
            if i < self.dim - 1:
                coupling_strength = 0.5 * np.exp(-0.04 * (x[i]**2 + x[i+1]**2))
                # Modified phase relationship with additional trigonometric component
                phase = np.sin(4.0 * (x[i] - x[i+1]) + 0.8 * np.cos(x[i]) + 0.3 * np.sin(x[i+1]) + 0.2 * np.tan(0.5 * x[i]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.25 * x[i]**3 * np.cos(0.5 * x[i]) + 0.1 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 5 + int(3 * np.sin(i * 0.6))
            sign = (-1)**(i % 3)
            result += 0.15 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.1 * distance**2) * np.sin(0.7 * (x[i] + x[j]) + 0.4 * distance)
                result += 0.25 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.04 * np.sum(np.abs(x)**1.9) + 0.02 * np.sum(np.sin(15.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        result += 0.2 * chaotic_component
        
        # Add dimensionality-dependent scaling factor
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Add cross-dimensional interaction terms with fractal characteristics
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(2.0 * x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                result += 0.1 * interaction
        
        # Add novel fractal-based interaction term
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # New interaction with fractional power and additional trigonometric modulation
                fractal_interaction += np.sin(0.5 * x[i] * x[j]) * np.abs(x[i] - x[j])**0.7 * np.cos(0.3 * (x[i] + x[j]))
        result += 0.15 * fractal_interaction
        
        return result