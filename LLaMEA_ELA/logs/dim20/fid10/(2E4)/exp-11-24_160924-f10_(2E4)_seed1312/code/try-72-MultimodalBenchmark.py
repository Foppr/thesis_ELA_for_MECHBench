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
            result += (xi**11 - 20 * xi**9 + 150 * xi**7 - 400 * xi**5 + 300 * xi**3 - 50 * xi) * np.sin(1.5 * xi) + 0.8 * xi**9 * np.cos(1.8 * xi)
            
        # Add enhanced cross-dimensional coupling with chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+20, self.dim)):  # Increased coupling range
                # Introduce chaotic dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 1.3 * np.exp(-0.4 * distance) * np.sin(8 * (x[i] + x[j])) * np.cos(1.1 * (x[i] - x[j]))
                
        # Add global scaling term with enhanced conditioning difficulty
        result += 0.12 * np.sum(x**13) + 0.11 * np.sum(np.cos(10 * x)) + 0.07 * np.sum(np.sin(7 * x))
        
        # Add highly non-separable interaction term involving all dimensions with septick coupling
        result += 1.1 * np.exp(-0.25 * np.sum((x - np.mean(x))**2)) * np.cos(1.3 * np.sum(x**8))
        
        # Add novel high-order interaction terms for increased complexity
        result += 0.7 * np.sum(np.sin(5 * x) * np.cos(2.5 * x)) + 0.5 * np.sum(x**4 * np.exp(-0.15 * x**2))
        
        # Add additional non-linear coupling with quintic and septic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * (x[i]**7 + x[j]**7) * np.sin(4 * (x[i] - x[j])) * np.cos(2.0 * (x[i] + x[j]))
                
        # Add chaotic exponential decay term with multiple trigonometric components
        result += 0.4 * np.exp(-0.2 * np.sum(np.abs(x))) * np.sin(1.5 * np.sum(x**5)) * np.cos(0.7 * np.sum(x**9))
        
        # Add adaptive coupling strength based on dimensionality with chaotic variation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.7 * (i + j) + 0.3 * np.sin(0.5 * i))
                result += coupling_strength * (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2)
                
        # Add penalty term near global optimum to increase convergence difficulty
        mean_x = np.mean(x)
        result += 0.8 * np.sum((x - mean_x)**5) + 0.6 * np.exp(-0.25 * np.sum((x - mean_x)**2))
        
        # Add enhanced conditioning term for high dimensions with chaotic scaling
        if self.dim > 10:
            result += 0.15 * np.sum(x**11) * np.exp(-0.07 * np.sum(x**2))
            
        return result