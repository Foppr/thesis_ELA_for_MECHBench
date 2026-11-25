import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 7.0 * np.sin(8.0 * x[i]) * np.cos(10.0 * x[i]) + 5.0 * np.sin(12.0 * x[i])
            
        # Add radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.5 * (x[i] - 2.5)**2) + 2.0 * np.exp(-0.3 * (x[i] + 3.5)**2)
            
        # Add a multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 1.5 * x[i]**5 - 2.2 * x[i]**4 + 1.8 * x[i]**3 - 1.1 * x[i]**2
            
        # Add cross-dimensional coupling with stronger trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * np.sin(x[i] * x[j]) * np.cos(1.1 * (x[i]**2 + x[j]**2))
                
        # Add a conditioning component that scales with dimensionality
        condition_factor = 1.0 + 0.7 * self.dim
        result *= condition_factor
        
        # Add chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 1.5 * np.sin(np.pi * np.sin(6.0 * x[i])) * np.cos(np.pi * np.cos(5.0 * x[i]))
            
        # Add a fractal-like component with more recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 12):
                recursive_term += 0.5**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Add penalty for large values with exponential scaling
        result += 0.4 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Add a new component: hyperbolic tangent oscillations (slightly modified coefficients)
        for i in range(self.dim):
            result += 0.85 * np.tanh(4.0 * x[i]) * np.sin(5.0 * x[i])
            
        # Add a multi-modal component with cross-dimensional polynomial interactions (modified interaction strength)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.55 * (x[i]**2 + x[j]**2) * np.sin(0.9 * x[i] * x[j])
                
        # Add enhanced chaotic component with fractional powers (slightly different exponent)
        for i in range(self.dim):
            result += 0.7 * np.sin(np.pi * np.sqrt(np.abs(x[i])) * np.cos(7.0 * x[i]))
            
        # Add a new cross-dimensional coupling term with exponential decay (modified decay rate)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(4.0 * (x[i] + x[j]))
                
        # Add a new polynomial interaction term with higher degree (slightly modified coefficients)
        for i in range(self.dim):
            result += 0.32 * x[i]**6 - 0.52 * x[i]**5 + 0.37 * x[i]**4
            
        # Add a new multi-modal component with complex trigonometric interactions (modified frequencies)
        for i in range(self.dim):
            result += 0.92 * np.sin(2.6 * x[i]) * np.cos(3.6 * x[i]) * np.tan(2.1 * x[i])
            
        # Add a new cross-dimensional coupling with hyperbolic functions (modified coefficients)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.32 * np.sinh(x[i] + x[j]) * np.cosh(1.1 * (x[i]**2 - x[j]**2))
                
        # Add a new chaotic component with modified fractional exponents (different exponent)
        for i in range(self.dim):
            result += 0.42 * np.sin(np.pi * np.power(np.abs(x[i]), 1.35)) * np.cos(5.0 * x[i])
            
        # Add a new component: complex hyperbolic sine-polynomial interactions (modified polynomial)
        for i in range(self.dim):
            result += 0.62 * np.sinh(2.0 * x[i]) * (x[i]**3 - 1.9 * x[i]**2 + 0.9 * x[i] - 0.9)
            
        # Add a new cross-dimensional coupling with complex polynomial interactions (modified interaction)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.22 * (x[i]**3 + x[j]**3) * np.cos(0.75 * x[i] * x[j])
                
        # Add a new chaotic component with nested logarithmic and trigonometric functions (modified base)
        for i in range(self.dim):
            result += 0.36 * np.sin(np.log(np.abs(x[i]) + 1.1) * np.cos(6.0 * x[i]))
            
        # Add enhanced multi-modal interactions with modified interaction coefficients
        for i in range(self.dim):
            result += 1.2 * np.sin(3.0 * x[i])**3 * np.cos(4.0 * x[i]) + 0.9 * np.tan(2.5 * x[i])
            
        # Add a new cross-dimensional coupling with complex hyperbolic and trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sinh(x[i] * x[j]) * np.cos(2.0 * (x[i]**2 + x[j]**2)) + 0.3 * np.tanh(x[i] + x[j])
                
        # Add a new component with higher-order polynomial interactions and chaotic behavior
        for i in range(self.dim):
            result += 0.5 * x[i]**7 - 0.8 * x[i]**6 + 0.6 * x[i]**5 - 0.4 * x[i]**4
            
        # Add a new multi-modal component with nested sine and cosine oscillations
        for i in range(self.dim):
            result += 1.1 * np.sin(np.sin(3.0 * x[i])) * np.cos(np.cos(2.0 * x[i]))
            
        # Add an enhanced chaotic component with modified fractional powers and sinusoidal modulation
        for i in range(self.dim):
            result += 0.65 * np.sin(np.pi * np.power(x[i], 1.4)) * np.cos(8.0 * x[i])
            
        # Add a new component combining exponential and polynomial terms with cross-dimensional coupling
        for i in range(self.dim):
            result += 0.7 * np.exp(-0.2 * x[i]**2) * (x[i]**3 + 0.5 * x[i]**2 - 1.2)
            
        # Add a new cross-dimensional coupling term with higher-order polynomial interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**4 + x[j]**4) * np.sin(1.5 * x[i] * x[j])
                
        return result