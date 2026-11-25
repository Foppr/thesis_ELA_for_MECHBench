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
            # Enhanced chaotic interaction terms with higher-order polynomials and sinusoids
            result += (xi**15 - 30 * xi**13 + 270 * xi**11 - 900 * xi**9 + 1200 * xi**7 - 600 * xi**5 + 150 * xi**3 - 10 * xi) * np.sin(2.1 * xi) + 1.1 * xi**12 * np.cos(2.5 * xi)
            
        # Add enhanced cross-dimensional coupling with chaotic interaction patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+20, self.dim)):  # Increased coupling range for more complexity
                # Introduce chaotic dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 2.0 * np.exp(-0.4 * distance) * np.sin(11 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
                
        # Add global scaling term with enhanced conditioning difficulty
        result += 0.2 * np.sum(x**17) + 0.18 * np.sum(np.cos(15 * x)) + 0.12 * np.sum(np.sin(10 * x))
        
        # Add highly non-separable interaction term involving all dimensions with decic coupling
        result += 1.6 * np.exp(-0.4 * np.sum((x - np.mean(x))**2)) * np.cos(2.0 * np.sum(x**11))
        
        # Add novel high-order interaction terms for increased complexity
        result += 1.0 * np.sum(np.sin(7 * x) * np.cos(4 * x)) + 0.8 * np.sum(x**7 * np.exp(-0.3 * x**2))
        
        # Add additional non-linear coupling with nonic and decic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * (x[i]**11 + x[j]**11) * np.sin(6 * (x[i] - x[j])) * np.cos(3.0 * (x[i] + x[j]))
                
        # Add chaotic exponential decay term with multiple trigonometric components
        result += 0.7 * np.exp(-0.3 * np.sum(np.abs(x))) * np.sin(2.0 * np.sum(x**7)) * np.cos(1.0 * np.sum(x**12))
        
        # Add adaptive coupling strength based on dimensionality with chaotic variation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.4 * np.sin(1.0 * (i + j) + 0.5 * np.sin(0.7 * i))
                result += coupling_strength * (x[i]**3 + x[j]**3) * np.exp(-0.25 * (x[i] - x[j])**2)
                
        # Add penalty term near global optimum to increase convergence difficulty
        mean_x = np.mean(x)
        result += 1.2 * np.sum((x - mean_x)**8) + 1.0 * np.exp(-0.4 * np.sum((x - mean_x)**2))
        
        # Add enhanced conditioning term for high dimensions with chaotic scaling
        if self.dim > 10:
            result += 0.3 * np.sum(x**14) * np.exp(-0.1 * np.sum(x**2))
            
        return result