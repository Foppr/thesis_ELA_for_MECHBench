import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add polynomial chaos expansion with random coefficients
        for i in range(self.dim):
            result += 1.2 * x[i]**6 + 0.8 * x[i]**5 - 1.5 * x[i]**4 + 2.0 * x[i]**3 - 0.5 * x[i]**2
            
        # Fractal-like sinusoidal components with varying frequencies
        for i in range(self.dim):
            fractal_component = 0.0
            for k in range(1, 10):
                fractal_component += (0.3 / k) * np.sin(k**1.5 * x[i])
            result += fractal_component
            
        # Adaptive cross-dimensional coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                result += weight * np.cos(2.0 * x[i]) * np.sin(1.5 * x[j])
                
        # Hyperbolic sine-polynomial interactions
        for i in range(self.dim):
            result += 0.9 * np.sinh(x[i]) * (x[i]**3 - x[i]**2 + 0.5 * x[i] - 0.2)
            
        # Multi-modal component with exponential oscillations
        for i in range(self.dim):
            result += 1.1 * np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i]) * np.cos(4.0 * x[i])
            
        # Cross-dimensional polynomial coupling with variable exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * (x[i]**2 + x[j]**2)**1.3 * np.sin(0.5 * x[i] * x[j])
                
        # Chaotic behavior through logistic map-like interactions
        for i in range(self.dim):
            result += 0.4 * np.sin(2.0 * np.pi * (x[i] + 0.1 * np.sin(x[i])))
            
        # Add a component with fractional dimensional interactions
        for i in range(self.dim):
            result += 0.6 * x[i]**1.7 * np.cos(2.5 * x[i])
            
        # Add penalty for large values with logarithmic scaling
        result += 0.3 * np.sum(np.log(np.abs(x) + 1.0))
        
        # Add a new component: complex multi-modal with adaptive peaks
        for i in range(self.dim):
            peak1 = 2.0 * np.sin(3.0 * x[i])
            peak2 = 1.5 * np.cos(4.0 * x[i])
            result += 0.8 * (peak1 + peak2) * np.exp(-0.1 * x[i]**2)
            
        # Add a new cross-dimensional coupling with radial basis functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.5 * np.exp(-distance) * np.sin(3.0 * (x[i] + x[j]))
                
        # Add a new chaotic component with nested trigonometric functions
        for i in range(self.dim):
            result += 0.5 * np.sin(np.pi * np.cos(np.pi * x[i])) * np.tan(0.5 * x[i])
            
        # Add a new polynomial interaction with varying degrees
        for i in range(self.dim):
            result += 0.4 * (x[i]**7 - x[i]**5 + x[i]**3 - x[i])
            
        # Add a component that scales with dimensionality for conditioning
        condition_factor = 1.0 + 0.8 * self.dim
        result *= condition_factor
        
        return result