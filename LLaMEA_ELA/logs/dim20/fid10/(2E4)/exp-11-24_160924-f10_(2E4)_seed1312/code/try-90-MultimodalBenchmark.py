import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic polynomial and sinusoidal components with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Chaotic interaction terms with high-order polynomials and sinusoids
            result += (xi**13 - 25 * xi**11 + 200 * xi**9 - 600 * xi**7 + 600 * xi**5 - 150 * xi**3 + 10 * xi) * np.sin(1.7 * xi) + 0.9 * xi**10 * np.cos(2.0 * xi)
            
        # Add enhanced cross-dimensional coupling with chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+15, self.dim)):  # Reduced coupling range for better conditioning
                # Introduce chaotic dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 1.5 * np.exp(-0.3 * distance) * np.sin(9 * (x[i] + x[j])) * np.cos(1.2 * (x[i] - x[j]))
                
        # Add global scaling term with enhanced conditioning difficulty
        result += 0.15 * np.sum(x**15) + 0.13 * np.sum(np.cos(12 * x)) + 0.09 * np.sum(np.sin(8 * x))
        
        # Add highly non-separable interaction term involving all dimensions with octic coupling
        result += 1.3 * np.exp(-0.3 * np.sum((x - np.mean(x))**2)) * np.cos(1.5 * np.sum(x**9))
        
        # Add novel high-order interaction terms for increased complexity
        result += 0.8 * np.sum(np.sin(6 * x) * np.cos(3 * x)) + 0.6 * np.sum(x**5 * np.exp(-0.2 * x**2))
        
        # Add additional non-linear coupling with septic and nonic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**9 + x[j]**9) * np.sin(5 * (x[i] - x[j])) * np.cos(2.5 * (x[i] + x[j]))
                
        # Add chaotic exponential decay term with multiple trigonometric components
        result += 0.5 * np.exp(-0.25 * np.sum(np.abs(x))) * np.sin(1.7 * np.sum(x**6)) * np.cos(0.8 * np.sum(x**10))
        
        # Add adaptive coupling strength based on dimensionality with chaotic variation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(0.8 * (i + j) + 0.4 * np.sin(0.6 * i))
                result += coupling_strength * (x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
                
        # Add penalty term near global optimum to increase convergence difficulty
        mean_x = np.mean(x)
        result += 1.0 * np.sum((x - mean_x)**6) + 0.8 * np.exp(-0.3 * np.sum((x - mean_x)**2))
        
        # Add enhanced conditioning term for high dimensions with chaotic scaling
        if self.dim > 10:
            result += 0.2 * np.sum(x**12) * np.exp(-0.08 * np.sum(x**2))
            
        return result