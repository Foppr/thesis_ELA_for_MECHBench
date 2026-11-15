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
            result += 0.85 * (np.exp(0.9 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 1.0 * (np.sin(7.0 * np.pi * x[i]) + 
                            0.9 * np.sin(14.0 * np.pi * x[i]) + 
                            0.7 * np.sin(21.0 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.9 * np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(7.0 * (x[i] - x[i+1]) + 1.3 * np.cos(x[i]) + 0.6 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.5 * x[i]**3 * np.cos(0.9 * x[i]) + 0.3 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 9 + int(7 * np.sin(i * 1.1))
            sign = (-1)**(i % 8)
            result += 0.3 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.3 * distance**2) * np.sin(1.5 * (x[i] + x[j]) + 0.8 * distance)
                result += 0.5 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.1 * np.sum(np.abs(x)**2.5) + 0.08 * np.sum(np.sin(30.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(6.0 * x[i]) * np.exp(-0.35 * x[i]**2)
        result += 0.4 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations with recursive self-similarity
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(35.0 * x[i]) * np.cos(18.0 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.1 * np.sin(70.0 * x[i])
        result += 0.3 * fractal_perturbation
        
        # Add irregular perturbations to increase complexity with recursive patterns
        irregular_perturbation = 0.0
        for i in range(self.dim):
            irregular_perturbation += np.sin(40.0 * x[i]) * np.cos(20.0 * x[i]) * np.exp(-0.08 * x[i]**2) + 0.09 * np.sin(80.0 * x[i])
        result += 0.25 * irregular_perturbation
        
        # Add recursive fractal dimensionality scaling with increased impact
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * 0.5)
        result *= dim_factor
        
        # Add recursive self-similarity component
        self_similarity = 0.0
        for i in range(self.dim):
            self_similarity += np.sin(50.0 * x[i]) * np.cos(25.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.15 * self_similarity
        
        return result