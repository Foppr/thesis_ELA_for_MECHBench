import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Enhanced exponential terms with modified scaling and chaotic coupling
        for i in range(self.dim):
            # Base exponential term with adjusted scaling
            result += 0.55 * (np.exp(0.6 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 0.7 * (np.sin(4.0 * np.pi * x[i]) + 
                            0.6 * np.sin(8.0 * np.pi * x[i]) + 
                            0.4 * np.sin(12.0 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.6 * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(4.0 * (x[i] - x[i+1]) + 0.9 * np.cos(x[i]) + 0.3 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.3 * x[i]**3 * np.cos(0.6 * x[i]) + 0.15 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 6 + int(4 * np.sin(i * 0.7))
            sign = (-1)**(i % 4)
            result += 0.15 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.15 * distance**2) * np.sin(0.8 * (x[i] + x[j]) + 0.5 * distance)
                result += 0.3 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.05 * np.sum(np.abs(x)**2.1) + 0.03 * np.sum(np.sin(18.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(3.5 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.25 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(20.0 * x[i]) * np.cos(10.0 * x[i]) * np.exp(-0.08 * x[i]**2)
        result += 0.18 * fractal_perturbation
        
        return result