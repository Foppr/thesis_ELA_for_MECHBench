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
            result += 12.0 * np.sin(11.0 * x[i]) * np.cos(15.0 * x[i]) + 8.0 * np.sin(17.0 * x[i])
            
        # Radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 5.0 * np.exp(-0.5 * (x[i] - 2.0)**2) + 4.0 * np.exp(-0.3 * (x[i] + 3.0)**2)
            
        # Multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 2.5 * x[i]**5 - 3.5 * x[i]**4 + 3.0 * x[i]**3 - 2.0 * x[i]**2
            
        # Stronger cross-dimensional coupling with trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 3.0 * np.sin(x[i] * x[j]) * np.cos(1.5 * (x[i]**2 + x[j]**2))
                
        # Conditioning component scaled with dimensionality
        condition_factor = 1.0 + 1.2 * self.dim
        result *= condition_factor
        
        # Chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 3.0 * np.sin(np.pi * np.sin(9.0 * x[i])) * np.cos(np.pi * np.cos(8.0 * x[i]))
            
        # Fractal-like component with recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 20):
                recursive_term += 0.5**k * np.sin(3**(k) * x[i])
            result += recursive_term
            
        # Penalty for large values with exponential scaling
        result += 0.8 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Hyperbolic tangent oscillations
        for i in range(self.dim):
            result += 1.5 * np.tanh(7.0 * x[i]) * np.sin(8.0 * x[i])
            
        # Multi-modal component with cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.2 * (x[i]**2 + x[j]**2) * np.sin(1.5 * x[i] * x[j])
                
        # Enhanced chaotic component with fractional powers
        for i in range(self.dim):
            result += 1.3 * np.sin(np.pi * np.sqrt(np.abs(x[i])) * np.cos(10.0 * x[i]))
            
        # Cross-dimensional coupling with exponential decay - modified decay rate
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(7.0 * (x[i] + x[j]))
                
        # Higher degree polynomial interaction with modified coefficients
        for i in range(self.dim):
            result += 0.5 * x[i]**6 - 0.7 * x[i]**5 + 0.5 * x[i]**4
            
        # Complex trigonometric interactions with reduced amplitude
        for i in range(self.dim):
            result += 1.5 * np.sin(4.0 * x[i]) * np.cos(5.0 * x[i]) * np.tan(3.0 * x[i])
            
        # Cross-dimensional coupling with hyperbolic functions - modified coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sinh(x[i] + x[j]) * np.cosh(1.5 * (x[i]**2 - x[j]**2))
                
        # Modified fractional exponents chaotic component
        for i in range(self.dim):
            result += 0.6 * np.sin(np.pi * np.power(np.abs(x[i]), 1.4)) * np.cos(8.0 * x[i])
            
        # Slightly modified hyperbolic sine-polynomial interactions with reduced influence
        for i in range(self.dim):
            result += 0.9 * np.sinh(3.0 * x[i]) * (x[i]**3 - 2.0 * x[i]**2 + 1.0 * x[i] - 0.8)
            
        # Cross-dimensional coupling with complex polynomial interactions - reduced strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**3 + x[j]**3) * np.cos(1.5 * x[i] * x[j])
                
        # Nested logarithmic and trigonometric chaotic component with modified parameters
        for i in range(self.dim):
            result += 0.5 * np.sin(np.log(np.abs(x[i]) + 1.2) * np.cos(9.0 * x[i]))
            
        return result