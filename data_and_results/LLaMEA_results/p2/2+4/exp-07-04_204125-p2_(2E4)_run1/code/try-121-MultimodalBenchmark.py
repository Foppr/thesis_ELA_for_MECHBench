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
            result += 0.75 * (np.exp(0.8 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 0.9 * (np.sin(6.0 * np.pi * x[i]) + 
                            0.8 * np.sin(12.0 * np.pi * x[i]) + 
                            0.6 * np.sin(18.0 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.85 * np.exp(-0.07 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(6.0 * (x[i] - x[i+1]) + 1.2 * np.cos(x[i]) + 0.5 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.4 * x[i]**3 * np.cos(0.8 * x[i]) + 0.25 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 8 + int(6 * np.sin(i * 0.9))
            sign = (-1)**(i % 7)
            result += 0.25 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.25 * distance**2) * np.sin(1.2 * (x[i] + x[j]) + 0.7 * distance)
                result += 0.4 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.08 * np.sum(np.abs(x)**2.3) + 0.06 * np.sum(np.sin(25.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.3 * x[i]**2)
        result += 0.35 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations with modified parameters
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += 0.8 * np.sin(30.0 * x[i]) * np.cos(15.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        result += 0.25 * fractal_perturbation
        
        # Add irregular perturbations to increase complexity
        irregular_perturbation = 0.0
        for i in range(self.dim):
            irregular_perturbation += np.sin(35.0 * x[i]) * np.cos(18.0 * x[i]) * np.exp(-0.06 * x[i]**2) + 0.07 * np.sin(60.0 * x[i])
        result += 0.2 * irregular_perturbation
        
        # Add dimensionality-dependent scaling factor with increased impact
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result