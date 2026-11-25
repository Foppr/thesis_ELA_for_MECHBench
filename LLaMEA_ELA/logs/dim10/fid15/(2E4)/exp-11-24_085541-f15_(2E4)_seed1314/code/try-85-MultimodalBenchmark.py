import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add enhanced polynomial chaos expansion with fractional exponents
        for i in range(self.dim):
            result += 0.8 * x[i]**7.5 + 0.6 * x[i]**4.2 - 0.5 * x[i]**3.8 + 0.3 * x[i]**2.1
            
        # Add highly chaotic trigonometric components with irrational frequencies
        for i in range(self.dim):
            result += 1.5 * np.sin(np.pi * x[i]) * np.cos(np.e * x[i]) * np.tan(np.sqrt(2) * x[i])
            
        # Add adaptive radial basis functions with dynamic widths and multiple peaks
        for i in range(self.dim):
            width = 0.3 + 0.2 * self.dim
            result += 2.5 * np.exp(-0.5 * ((x[i] - 1.5) / width)**2) + 2.0 * np.exp(-0.4 * ((x[i] + 1.8) / (width * 0.6))**2) + 1.2 * np.exp(-0.3 * ((x[i] - 2.2) / (width * 0.8))**2)
            
        # Add enhanced cross-dimensional coupling with exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.2 * np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(0.8 * x[i] * x[j])
                
        # Add fractional sine-polynomial interactions with varying exponents
        for i in range(self.dim):
            result += 1.1 * np.sin(x[i]**2.5) * np.cos(3.0 * x[i]) + 0.8 * np.sin(np.sqrt(np.abs(x[i])) * np.cos(5.0 * x[i]))
            
        # Add fractal-like recursive components with Fibonacci-based frequencies
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, 12):
                fib_k = (1.618**k - (-0.618)**k) / np.sqrt(5)  # Approximation of Fibonacci
                recursive_sum += (0.25**k) * np.sin(fib_k * x[i])
            result += recursive_sum
            
        # Add multi-modal component with enhanced hyperbolic tangent and polynomial interactions
        for i in range(self.dim):
            result += 1.0 * np.tanh(x[i]) * (x[i]**5 - 3.0 * x[i]**4 + 2.0 * x[i]**3 - x[i]**2)
            
        # Add enhanced cross-dimensional exponential coupling with variable scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.1 * np.sin(0.5 * (x[i] + x[j]))
                result += 0.6 * np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(4.0 * (x[i] + x[j])) * scale_factor
                
        # Add conditioning factor based on dimensionality with exponential growth
        condition_factor = 1.0 + 0.5 * self.dim**1.5
        result *= condition_factor
        
        # Add penalty for large values with hyperbolic scaling
        result += 0.3 * np.sum(np.log(1.0 + np.abs(x)**1.5))
        
        # Add novel fractional polynomial component to increase multimodality
        frac_poly = 0.0
        for i in range(self.dim):
            frac_poly += 0.4 * (x[i]**2.7 + x[i]**1.8) * np.sin(0.3 * x[i])
        result += frac_poly
        
        # Add ultra-high frequency trigonometric noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += 0.5 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i])
        result += noise_component
        
        return result