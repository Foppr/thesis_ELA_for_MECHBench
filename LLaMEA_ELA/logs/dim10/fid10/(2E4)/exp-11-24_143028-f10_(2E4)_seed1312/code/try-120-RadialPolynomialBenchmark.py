import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with quartic decay and enhanced conditioning
        result = 0.4 * np.sum(x**4) * np.exp(-0.2 * np.sum(x**2))
        
        # Multi-frequency polynomial oscillations with increased complexity
        for i in range(self.dim):
            result += 2.2 * x[i]**6 * np.sin(15 * x[i]) * np.cos(11 * x[i]) + 1.5 * x[i]**3 * np.sin(8 * x[i])
        
        # Radial basis function components with varying widths, phases, and coupling
        for i in range(self.dim):
            result += 2.5 * np.exp(-0.5 * (x[i] - 2.0)**2) + 1.8 * np.exp(-0.3 * (x[i] + 4.0)**2) + 1.2 * np.exp(-0.7 * (x[i] - 1.5)**2)
        
        # Asymmetric boundary penalties with cubic and hyperbolic terms
        for i in range(self.dim):
            if x[i] < 0:
                result += 3.2 * np.exp(-0.5 * (x[i] + 5.0)**4) * (1 + 0.7 * np.sin(20 * x[i]))
            else:
                result += 2.8 * np.exp(-0.3 * (x[i] - 5.0)**4) * (1 + 0.6 * np.cos(16 * x[i]))
        
        # Coupling between dimensions with enhanced cosine modulation and interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 1.2 + 0.5 * np.cos(8 * (x[i] - x[j])) * np.sin(5 * (x[i] + x[j]))
                result += coupling * np.cos(10 * x[i]) * np.sin(12 * x[j]) * np.exp(-0.2 * (x[i] + x[j])**2)
        
        # High-frequency chaotic modulation with multiple sine waves and fractal components
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= np.sin(18 * x[i]) + np.cos(20 * x[i]) + 2.0
        result += 2.0 * chaos_factor
        
        # Fractal-like structure with recursive cosine and polynomial components
        for i in range(self.dim):
            result += 1.5 * np.cos(30 * x[i]) * np.sin(25 * x[i]) * np.cos(25 * x[i]**2) * (1 + 0.5 * np.abs(x[i]))
        
        # Weighted sum of polynomial and trigonometric terms with cubic interaction and enhanced coupling
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**6 + 0.7 * x[i]**5 - 0.4 * x[i]**4 + 0.2 * x[i]**3
        result += 1.8 * poly_term * np.sin(8 * np.sum(x))
        
        # Cross-dimensional exponential interaction with sine coupling and enhanced conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.9 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.4 * np.abs(x[i] + x[j]))) * np.cos(15 * (x[i] - x[j]))
        
        # Additional asymmetric wave pattern with hyperbolic tangent and complex modulation
        sum_x = np.sum(x)
        result += 2.8 * np.sin(35 * sum_x) * np.cos(30 * sum_x) * (1 + 0.6 * np.tanh(3 * sum_x))
        
        # Cross-dimensional polynomial coupling with quintic terms and enhanced interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                result += 0.8 * (x[i]**4 + x[j]**4) * np.sin(7 * (x[i] - x[j]))
        
        # Additional high-frequency noise component with enhanced chaotic behavior
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.sin(60 * x[i]) * np.cos(55 * x[i])
        result += noise
        
        # Improved conditioning and separation through modified exponential terms with enhanced coupling
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.4 * (x[i] - 2.0)**2) * np.sin(25 * x[i]) * np.cos(20 * x[i])
        
        # Additional dimension coupling with sine modulation, exponential decay, and enhanced interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.sin(9 * (x[i] + x[j])) * np.exp(-0.3 * (x[i] - x[j])**2) * (1 + 0.4 * np.cos(11 * x[i]))
        
        # Enhanced global structure with weighted harmonic components and additional fractal influence
        harmonic_sum = 0
        for i in range(self.dim):
            harmonic_sum += np.sin(7 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.15 * x[i]**2)
        result += 1.8 * harmonic_sum**2
        
        # Additional complexity through cross-dimensional polynomial interaction with higher order terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.6 * (x[i]**5 + x[j]**5) * np.cos(4 * (x[i] - x[j]))
        
        return result