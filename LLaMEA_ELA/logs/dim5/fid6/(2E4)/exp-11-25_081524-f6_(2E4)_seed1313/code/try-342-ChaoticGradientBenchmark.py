import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        result += (r**3) * np.sin(4.0 * r) * np.cos(3.0 * r) * np.exp(-r/10.0)
        
        # Intensified chaotic trigonometric terms with dynamic frequencies
        for i in range(self.dim):
            xi = x[i]
            freq1 = 2.5 + 1.8 * np.sin(0.4 * i + 0.2 * self.dim)
            freq2 = 1.8 + 0.9 * np.cos(0.5 * i + 0.3 * self.dim)
            result += 0.9 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.35 * np.sin(7.0 * xi))
            
        # Enhanced polynomial coupling with radial dependency
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * (xi**5 - 2*xi**3 + xi) * np.exp(-r/8.0)
            
        # Multi-scale harmonic interference with variable amplitudes
        for i in range(self.dim):
            xi = x[i]
            result += 0.45 * np.sin(12.0 * xi + 0.6 * r) * np.cos(9.0 * xi + 0.4 * r) * (1.0 + 0.25 * np.cos(4.0 * r))
            
        # Enhanced cross-dimensional coupling with sine-cosine combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.25 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.25 * np.sin(5.0 * r)) * np.exp(-abs(xi-xj)/5.0)
                
        # Nested polynomial structure with varying exponents and chaotic perturbations
        for i in range(self.dim):
            xi = x[i]
            result += 0.35 * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.exp(-xi**2/3.0)
            
        # Enhanced radial symmetry with chaotic perturbations and additional harmonics
        result += 0.45 * r**2 * np.sin(5.0 * r + 0.6 * self.dim) * np.cos(4.0 * r + 0.4 * self.dim) * np.exp(-r/15.0)
        
        # Additional high-frequency trigonometric interference terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.sin(20.0 * xi) * np.cos(12.0 * xi) * np.exp(-xi**2/4.0)
            
        # Cross-dimensional chaotic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.2 * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/3.0) * (1.0 + 0.15 * np.sin(6.0 * r))
                
        # High-order polynomial with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * (xi**8 - 5*xi**6 + 10*xi**4 - 10*xi**2 + 1) * np.exp(-xi**2/5.0)
            
        # Novel chaotic perturbation term to improve fitness
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += 0.15 * np.sin(15.0 * xi + 3.0 * r) * np.cos(8.0 * xi - 2.0 * r)
        result += chaotic_perturbation * np.exp(-r/20.0)
        
        # Additional harmonic interference with dynamic amplitude
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(25.0 * xi + 0.3 * r) * np.cos(18.0 * xi + 0.2 * r) * (1.0 + 0.2 * np.sin(3.0 * r))
            
        # Cross-dimensional coupling with variable decay rate
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.15 * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/4.0) * (1.0 + 0.1 * np.sin(7.0 * r))
                
        # Additional chaotic harmonic terms with higher frequencies and stronger coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.35 * np.sin(30.0 * xi + 2.0 * r) * np.cos(15.0 * xi - r) * np.exp(-xi**2/6.0)
            
        # Enhanced multi-modal structure with increased number of local minima
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(40.0 * xi) * np.cos(25.0 * xi) * (1.0 + 0.25 * np.sin(8.0 * r)) * np.exp(-abs(xi)/2.0)
            
        # Increased cross-dimensional coupling with fractal-like behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.3 * np.sin(3.0 * xi + 2.0 * xj) * np.cos(2.0 * xi - 3.0 * xj) * np.exp(-abs(xi-xj)/6.0) * (1.0 + 0.15 * np.sin(9.0 * r))
                
        # Higher-order polynomial with increased complexity and chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**9 - 6*xi**7 + 15*xi**5 - 20*xi**3 + 15*xi) * np.exp(-xi**2/4.0)
            
        # Novel perturbation term with fractal characteristics and increased dimensionality
        fractal_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            fractal_perturbation += 0.2 * np.sin(22.0 * xi + 4.0 * r) * np.cos(10.0 * xi - 3.0 * r) * np.exp(-r/25.0)
        result += fractal_perturbation
        
        # Multi-scale chaotic interference with variable coupling strength
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * np.sin(35.0 * xi + 1.5 * r) * np.cos(20.0 * xi - 1.0 * r) * (1.0 + 0.3 * np.sin(6.0 * r)) * np.exp(-xi**2/3.0)
        
        # Slight modification to increase difficulty: increased chaotic modulation coefficients
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(18.0 * xi + 2.5 * r) * np.cos(9.0 * xi - 1.5 * r) * (1.0 + 0.4 * np.sin(5.0 * r)) * np.exp(-xi**2/3.5)
            
        return result