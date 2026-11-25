import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sinusoidal oscillations with varied frequencies and amplitudes
        for i in range(self.dim):
            result += 7.0 * np.sin(8.0 * x[i]) * np.cos(10.0 * x[i]) + 5.0 * np.sin(12.0 * x[i])
            
        # Radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.3 * (x[i] - 2.0)**2) + 2.0 * np.exp(-0.15 * (x[i] + 3.0)**2)
            
        # Multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 1.5 * x[i]**5 - 2.0 * x[i]**4 + 1.8 * x[i]**3 - 1.2 * x[i]**2
            
        # Stronger cross-dimensional coupling with trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * np.sin(x[i] * x[j]) * np.cos(1.0 * (x[i]**2 + x[j]**2))
                
        # Conditioning component scaled with dimensionality
        condition_factor = 1.0 + 0.7 * self.dim
        result *= condition_factor
        
        # Chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 1.8 * np.sin(np.pi * np.sin(6.0 * x[i])) * np.cos(np.pi * np.cos(5.0 * x[i]))
            
        # Fractal-like component with recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 12):
                recursive_term += 0.3**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Penalty for large values with exponential scaling
        result += 0.4 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Hyperbolic tangent oscillations
        for i in range(self.dim):
            result += 0.9 * np.tanh(4.5 * x[i]) * np.sin(5.5 * x[i])
            
        # Multi-modal component with cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * (x[i]**2 + x[j]**2) * np.sin(0.9 * x[i] * x[j])
                
        # Enhanced chaotic component with fractional powers
        for i in range(self.dim):
            result += 0.8 * np.sin(np.pi * np.sqrt(np.abs(x[i])) * np.cos(7.0 * x[i]))
            
        # Cross-dimensional coupling with exponential decay - modified decay rate
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.exp(-0.25 * (x[i] - x[j])**2) * np.sin(4.5 * (x[i] + x[j]))
                
        # Higher degree polynomial interaction with modified coefficients
        for i in range(self.dim):
            result += 0.25 * x[i]**6 - 0.4 * x[i]**5 + 0.25 * x[i]**4
            
        # Complex trigonometric interactions with reduced amplitude
        for i in range(self.dim):
            result += 0.9 * np.sin(2.5 * x[i]) * np.cos(3.5 * x[i]) * np.tan(2.0 * x[i])
            
        # Cross-dimensional coupling with hyperbolic functions - modified coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sinh(x[i] + x[j]) * np.cosh(0.9 * (x[i]**2 - x[j]**2))
                
        # Modified fractional exponents chaotic component
        for i in range(self.dim):
            result += 0.35 * np.sin(np.pi * np.power(np.abs(x[i]), 1.25)) * np.cos(5.5 * x[i])
            
        # Slightly modified hyperbolic sine-polynomial interactions with reduced influence
        for i in range(self.dim):
            result += 0.5 * np.sinh(2.0 * x[i]) * (x[i]**3 - 1.5 * x[i]**2 + 0.7 * x[i] - 0.6)
            
        # Cross-dimensional coupling with complex polynomial interactions - reduced strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i]**3 + x[j]**3) * np.cos(0.9 * x[i] * x[j])
                
        # Nested logarithmic and trigonometric chaotic component with modified parameters
        for i in range(self.dim):
            result += 0.25 * np.sin(np.log(np.abs(x[i]) + 1.05) * np.cos(6.5 * x[i]))
            
        return result