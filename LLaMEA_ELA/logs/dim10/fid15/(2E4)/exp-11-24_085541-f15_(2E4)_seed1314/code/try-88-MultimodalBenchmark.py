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
            result += 12.0 * np.sin(11.0 * x[i]) * np.cos(13.0 * x[i]) + 9.0 * np.sin(15.0 * x[i])
            
        # Radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 4.5 * np.exp(-0.5 * (x[i] - 2.0)**2) + 3.5 * np.exp(-0.3 * (x[i] + 3.0)**2)
            
        # Multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 2.5 * x[i]**5 - 3.5 * x[i]**4 + 2.8 * x[i]**3 - 2.0 * x[i]**2
            
        # Stronger cross-dimensional coupling with trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 3.0 * np.sin(x[i] * x[j]) * np.cos(1.5 * (x[i]**2 + x[j]**2))
                
        # Conditioning component scaled with dimensionality
        condition_factor = 1.0 + 1.3 * self.dim
        result *= condition_factor
        
        # Chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 3.0 * np.sin(np.pi * np.sin(9.0 * x[i])) * np.cos(np.pi * np.cos(7.0 * x[i]))
            
        # Fractal-like component with recursive sine terms (more iterations)
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 25):
                recursive_term += 0.5**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Penalty for large values with exponential scaling
        result += 0.8 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Hyperbolic tangent oscillations (more intense)
        for i in range(self.dim):
            result += 1.8 * np.tanh(6.0 * x[i]) * np.sin(7.0 * x[i])
            
        # Multi-modal component with cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * (x[i]**2 + x[j]**2) * np.sin(1.5 * x[i] * x[j])
                
        # Enhanced chaotic component with fractional powers
        for i in range(self.dim):
            result += 1.5 * np.sin(np.pi * np.sqrt(np.abs(x[i])) * np.cos(9.0 * x[i]))
            
        # Cross-dimensional coupling with exponential decay (stronger)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(6.0 * (x[i] + x[j]))
                
        # Higher degree polynomial interaction (more complex)
        for i in range(self.dim):
            result += 0.7 * x[i]**7 - 0.9 * x[i]**6 + 0.7 * x[i]**5
            
        # Complex trigonometric interactions (more chaotic)
        for i in range(self.dim):
            result += 1.8 * np.sin(4.0 * x[i]) * np.cos(5.0 * x[i]) * np.tan(3.0 * x[i])
            
        # Cross-dimensional coupling with hyperbolic functions (stronger)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sinh(x[i] + x[j]) * np.cosh(1.5 * (x[i]**2 - x[j]**2))
                
        # Modified fractional exponents chaotic component (more intense)
        for i in range(self.dim):
            result += 0.8 * np.sin(np.pi * np.power(np.abs(x[i]), 1.4)) * np.cos(7.0 * x[i])
            
        # Slightly modified hyperbolic sine-polynomial interactions (stronger coupling)
        for i in range(self.dim):
            result += 1.5 * np.sinh(3.0 * x[i]) * (x[i]**3 - 2.0 * x[i]**2 + 1.0 * x[i] - 0.9)
            
        # Cross-dimensional coupling with complex polynomial interactions (stronger)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * (x[i]**3 + x[j]**3) * np.cos(1.5 * x[i] * x[j])
                
        # Nested logarithmic and trigonometric chaotic component (more complex)
        for i in range(self.dim):
            result += 0.7 * np.sin(np.log(np.abs(x[i]) + 1.5) * np.cos(8.0 * x[i]))
            
        return result